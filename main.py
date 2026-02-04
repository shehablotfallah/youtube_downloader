import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from pytubefix import Playlist, YouTube
from tqdm import tqdm

INVALID_CHARS = r'[\\/:*?"<>|]'


def sanitize_windows_name(name: str) -> str:
    return re.sub(INVALID_CHARS, "_", name).strip()


def ask_max_resolution() -> int:
    while True:
        try:
            return int(input("🎥 Enter max resolution (e.g. 1080, 720, 480): "))
        except ValueError:
            print("❌ Please enter a valid number")


def download_with_tqdm(yt: YouTube, stream, output_dir: Path, filename: str):
    filesize = stream.filesize
    pbar = tqdm(
        total=filesize,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        desc=filename,
        leave=True,
    )

    last_bytes = 0

    def on_progress(_, __, bytes_remaining):
        nonlocal last_bytes
        downloaded = filesize - bytes_remaining
        delta = downloaded - last_bytes
        last_bytes = downloaded
        pbar.update(delta)

    yt.register_on_progress_callback(on_progress)
    stream.download(output_path=output_dir, filename=filename)
    pbar.close()


def find_ffmpeg(ffmpeg_path: str | None = None) -> str | None:
    # 1) explicit path (file or folder)
    if ffmpeg_path:
        p = Path(ffmpeg_path)
        if p.is_file():
            return str(p)
        # if path is folder, look for executable in it
        exe = p / "ffmpeg"
        if os.name == "nt":
            exe = exe.with_suffix(".exe")
        if exe.exists():
            return str(exe)

    # 2) on PATH
    which = shutil.which("ffmpeg")
    if which:
        return which

    # 3) bundled ffmpeg in repo (e.g. ffmpeg-*/bin/ffmpeg(.exe))
    for candidate in Path(".").glob("ffmpeg-*/bin/ffmpeg*"):
        if candidate.is_file():
            return str(candidate)

    return None


def download_playlist(playlist_url: str, base_dir: str = "downloads", ffmpeg_path: str | None = None):
    """Legacy function for backward compatibility."""
    max_resolution = ask_max_resolution()

    ffmpeg_exe = find_ffmpeg(ffmpeg_path)
    if not ffmpeg_exe:
        print("❌ ffmpeg not found. Please add ffmpeg to PATH or provide --ffmpeg path.")
        print("See README.md for instructions to add the bundled ffmpeg to your PATH.")
        sys.exit(1)

    playlist = Playlist(
        playlist_url,
        client="WEB",
        use_oauth=True,
        allow_oauth_cache=True,
    )

    playlist_title = sanitize_windows_name(playlist.title or "playlist")
    output_dir = Path(base_dir) / playlist_title
    output_dir.mkdir(parents=True, exist_ok=True)

    video_urls = playlist.video_urls
    total_videos = len(video_urls)
    padding = len(str(total_videos))

    print(f"\n📂 Playlist: {playlist_title}")
    print(f"🎬 Videos: {total_videos}")
    print(f"🎯 Max resolution: {max_resolution}p\n")

    for index, url in enumerate(video_urls, start=1):
        prefix = str(index).zfill(padding)

        try:
            yt = YouTube(
                url,
                client="WEB",
                use_oauth=True,
                allow_oauth_cache=True,
            )

            title = sanitize_windows_name(yt.title)
            final_file = output_dir / f"{prefix} - {title}.mp4"

            if final_file.exists():
                print(f"[SKIP] {final_file.name}")
                continue

            # 🎥 pick video-only stream
            video_streams = (
                yt.streams
                .filter(only_video=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
            )

            video_stream = None
            for s in video_streams:
                res = int(s.resolution.replace("p", ""))
                if res <= max_resolution:
                    video_stream = s
                    break

            if not video_stream:
                video_stream = video_streams.first()

            # 🔊 best audio
            audio_stream = (
                yt.streams
                .filter(only_audio=True, file_extension="mp4")
                .order_by("abr")
                .desc()
                .first()
            )

            if not video_stream or not audio_stream:
                print(f"[SKIP] No streams for {title}")
                continue

            print(f"⬇️  {prefix}/{total_videos} | {video_stream.resolution} + {audio_stream.abr}")

            temp_video = output_dir / f"temp_video_{prefix}.mp4"
            temp_audio = output_dir / f"temp_audio_{prefix}.mp4"

            download_with_tqdm(yt, video_stream, output_dir, temp_video.name)
            download_with_tqdm(yt, audio_stream, output_dir, temp_audio.name)

            # 🎬 merge with ffmpeg
            subprocess.run(
                [
                    ffmpeg_exe, "-y",
                    "-i", str(temp_video),
                    "-i", str(temp_audio),
                    "-c:v", "copy",
                    "-c:a", "aac",
                    str(final_file),
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            temp_video.unlink(missing_ok=True)
            temp_audio.unlink(missing_ok=True)

        except Exception as e:
            print(f"[ERROR] {url}: {e}")

    print("\n✅ Playlist download finished!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download YouTube playlists with custom resolution and ffmpeg support."
    )
    parser.add_argument(
        "--playlist", "-p",
        help="YouTube playlist URL (interactive prompt if not provided)",
        default=None
    )
    parser.add_argument(
        "--max-resolution", "-r",
        type=int,
        help="Maximum video resolution (e.g., 1080, 720, 480). Default: prompt user.",
        default=None
    )
    parser.add_argument(
        "--output", "-o",
        help="Output directory (default: downloads)",
        default="downloads"
    )
    parser.add_argument(
        "--ffmpeg",
        help="Path to ffmpeg executable or folder containing ffmpeg",
        default=None
    )

    args = parser.parse_args()

    # Get playlist URL
    playlist_url = args.playlist
    if not playlist_url:
        playlist_url = input("🔗 Enter YouTube playlist URL: ").strip()

    # Get max resolution
    max_resolution = args.max_resolution
    if max_resolution is None:
        max_resolution = ask_max_resolution()

    # Get ffmpeg
    ffmpeg_exe = find_ffmpeg(args.ffmpeg)
    if not ffmpeg_exe:
        print("❌ ffmpeg not found. Please add ffmpeg to PATH or provide --ffmpeg path.")
        print("📖 See README.md for instructions.")
        sys.exit(1)

    # Modified download_playlist to accept max_resolution
    playlist = Playlist(
        playlist_url,
        client="WEB",
        use_oauth=True,
        allow_oauth_cache=True,
    )

    playlist_title = sanitize_windows_name(playlist.title or "playlist")
    output_dir = Path(args.output) / playlist_title
    output_dir.mkdir(parents=True, exist_ok=True)

    video_urls = playlist.video_urls
    total_videos = len(video_urls)
    padding = len(str(total_videos))

    print(f"\n📂 Playlist: {playlist_title}")
    print(f"🎬 Videos: {total_videos}")
    print(f"🎯 Max resolution: {max_resolution}p\n")

    for index, url in enumerate(video_urls, start=1):
        prefix = str(index).zfill(padding)

        try:
            yt = YouTube(
                url,
                client="WEB",
                use_oauth=True,
                allow_oauth_cache=True,
            )

            title = sanitize_windows_name(yt.title)
            final_file = output_dir / f"{prefix} - {title}.mp4"

            if final_file.exists():
                print(f"[SKIP] {final_file.name}")
                continue

            # 🎥 pick video-only stream
            video_streams = (
                yt.streams
                .filter(only_video=True, file_extension="mp4")
                .order_by("resolution")
                .desc()
            )

            video_stream = None
            for s in video_streams:
                res = int(s.resolution.replace("p", ""))
                if res <= max_resolution:
                    video_stream = s
                    break

            if not video_stream:
                video_stream = video_streams.first()

            # 🔊 best audio
            audio_stream = (
                yt.streams
                .filter(only_audio=True, file_extension="mp4")
                .order_by("abr")
                .desc()
                .first()
            )

            if not video_stream or not audio_stream:
                print(f"[SKIP] No streams for {title}")
                continue

            print(f"⬇️  {prefix}/{total_videos} | {video_stream.resolution} + {audio_stream.abr}")

            temp_video = output_dir / f"temp_video_{prefix}.mp4"
            temp_audio = output_dir / f"temp_audio_{prefix}.mp4"

            download_with_tqdm(yt, video_stream, output_dir, temp_video.name)
            download_with_tqdm(yt, audio_stream, output_dir, temp_audio.name)

            # 🎬 merge with ffmpeg
            subprocess.run(
                [
                    ffmpeg_exe, "-y",
                    "-i", str(temp_video),
                    "-i", str(temp_audio),
                    "-c:v", "copy",
                    "-c:a", "aac",
                    str(final_file),
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            temp_video.unlink(missing_ok=True)
            temp_audio.unlink(missing_ok=True)

        except Exception as e:
            print(f"[ERROR] {url}: {e}")

    print("\n✅ Playlist download finished!")
