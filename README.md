# 🎥 YouTube Playlist Downloader

A professional Python script to download complete YouTube playlists with custom video resolution and automatic audio-video merging using ffmpeg.

---

## ⚡ Quick Start

### 1️⃣ Download the Project

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/shehablotfallah/youtube_downloader.git
cd youtube_downloader
```

**Option B: Direct Download**
- Click **Code** → **Download ZIP** on GitHub
- Extract the ZIP file
- Open terminal/PowerShell in the extracted folder

### 2️⃣ Install Dependencies (2 minutes)

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up ffmpeg (Optional but Recommended)

**Windows (Easy):**
```powershell
powershell -ExecutionPolicy Bypass -File setup-ffmpeg.ps1
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

### 4️⃣ Download Your First Playlist

```bash
python main.py --playlist "https://www.youtube.com/playlist?list=PLxxxxx" --max-resolution 720
```

Or interactive mode:
```bash
python main.py
```

**That's it! Videos will be saved in `downloads/` folder** ✅

---

## ✨ Features

- ✅ Download entire playlists automatically
- ✅ Choose maximum video resolution (1080p, 720p, 480p, etc.)
- ✅ Merge video and audio into a single MP4 file
- ✅ Progress bar for each download
- ✅ Skip already downloaded videos
- ✅ CLI support with multiple options
- ✅ Smart ffmpeg detection (bundled, PATH, or custom path)

---

## 📋 Requirements

- **Python 3.8+** → [Download Python](https://www.python.org/downloads/)
- **ffmpeg** (included in the project or can be installed separately)

---

## 🚀 Installation

### Step 1: Get the Project

#### Using Git (Recommended)
```bash
git clone https://github.com/shehablotfallah/youtube_downloader.git
cd youtube_downloader
```

#### Direct Download from GitHub
1. Go to: https://github.com/shehablotfallah/youtube_downloader
2. Click **Code** button (green)
3. Click **Download ZIP**
4. Extract the ZIP file
5. Open PowerShell or Command Prompt in the extracted folder

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `pytubefix` - YouTube video extraction
- `tqdm` - Progress bars

### Step 3: Set up ffmpeg

#### Option A: Quick Setup Script (Recommended for Windows)

```powershell
powershell -ExecutionPolicy Bypass -File setup-ffmpeg.ps1
```

Then choose:
- **1** for current session only (temporary)
- **2** to add permanently (requires administrator)

#### Option B: Manual Setup

**Windows:**
- Add the ffmpeg executable path to your system `PATH` environment variable

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

---

## 💻 Usage

### Interactive Mode (Simplest)

```bash
python main.py
```

You'll be prompted for:
1. YouTube playlist URL
2. Maximum video resolution (e.g., 1080, 720, 480)

**Example:**
```
🔗 Enter YouTube playlist URL: https://www.youtube.com/playlist?list=PLxxxxx
🎥 Enter max resolution (e.g. 1080, 720, 480): 720
```

### CLI Mode (Command Line)

Basic usage:
```bash
python main.py --playlist "https://www.youtube.com/playlist?list=PLxxxxx" --max-resolution 720
```

With custom output directory:
```bash
python main.py -p "https://www.youtube.com/playlist?list=PLxxxxx" -r 1080 -o my_videos
```

#### Available Options

| Option | Short | Description | Example |
|--------|-------|-------------|---------|
| `--playlist` | `-p` | YouTube playlist URL | `--playlist "https://..."` |
| `--max-resolution` | `-r` | Maximum video resolution | `--max-resolution 720` |
| `--output` | `-o` | Output directory | `--output downloads` |
| `--ffmpeg` | | Path to ffmpeg executable | `--ffmpeg "C:\ffmpeg\bin"` |

---

## 📁 Project Structure

```
youtube_downloader/
├── main.py                      # Main script
├── setup-ffmpeg.ps1             # ffmpeg setup script (Windows)
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── LICENSE                      # MIT License
├── .gitignore                   # Git ignore rules
├── downloads/                   # Output folder (auto-created)
└── ffmpeg-*/                    # Bundled ffmpeg (optional)
```

---

## 🎬 Examples

### Download a playlist with 720p resolution

```bash
python main.py --playlist "https://www.youtube.com/playlist?list=PL1234567890" --max-resolution 720
```

**Output:**
```
📂 Playlist: Playlist Name
🎬 Videos: 50
🎯 Max resolution: 720p

⬇️  01/50 | 720p + 128kbps
[████████████████████████████] 45.5MB
⬇️  02/50 | 720p + 128kbps
...
✅ Playlist download finished!
```

Downloaded files are saved to: `downloads/Playlist Name/`

### Download with custom ffmpeg path

```bash
python main.py -p "https://www.youtube.com/playlist?list=PLxxxxx" -r 480 --ffmpeg "C:\custom\ffmpeg\bin"
```

### Save to custom directory

```bash
python main.py -p "https://www.youtube.com/playlist?list=PLxxxxx" -o "D:\Videos"
```

---

## ⚠️ Important Notes

1. **ffmpeg is required**: The script needs ffmpeg to merge video and audio streams. Make sure it's installed and accessible.

2. **Copyright Notice**: Downloading copyrighted content may be illegal in your jurisdiction. Always check the platform's terms of service and respect copyright laws.

3. **Download Speed**: Speed depends on your internet connection and video resolution.

4. **Duplicate Prevention**: If a file already exists, the script skips downloading it.

5. **OAuth Cache**: The script uses OAuth caching for better YouTube access. Cache files are automatically stored.

---

## 🔧 Troubleshooting

### Error: ❌ ffmpeg not found

**Solution 1 - Use the setup script:**
```powershell
powershell -ExecutionPolicy Bypass -File setup-ffmpeg.ps1
```

**Solution 2 - Specify ffmpeg path directly:**
```bash
python main.py --ffmpeg "C:\path\to\ffmpeg\bin"
```

**Solution 3 - Install ffmpeg manually:**
- Windows: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
- Linux: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`

### Error: Module not found (pytubefix, tqdm)

```bash
pip install --upgrade -r requirements.txt
```

### Slow downloads

Try reducing resolution:
```bash
python main.py -r 480
```

---

## 📦 Dependencies

- **pytubefix**: YouTube video extraction and streaming
- **tqdm**: Progress bar for downloads

See `requirements.txt` for exact versions.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! You can:
- Report bugs
- Suggest new features
- Improve documentation
- Submit pull requests

---

## 📞 Support

If you encounter any issues:
1. Check the Troubleshooting section above
2. Verify ffmpeg is properly installed
3. Ensure you have the latest Python version (3.8+)
4. Try running with `-r 480` for lower resolution if downloads fail

---

**Happy downloading! 🎉**
