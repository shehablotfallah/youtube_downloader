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

### 2️⃣ Install Python Packages (2 minutes)

```bash
pip install -r requirements.txt
```

### 3️⃣ Start Using It! 🎉

**No ffmpeg setup needed!** It's already included in the `ffmpeg/` folder.

Just run:
```bash
python main.py
```

Or with options:
```bash
python main.py --playlist "https://www.youtube.com/playlist?list=PLxxxxx" --max-resolution 720
```

**That's it! Videos will be saved in `downloads/` folder** ✅

---

### ⚙️ Optional: Add ffmpeg to System PATH

If you want `ffmpeg` available system-wide, run **once**:
```powershell
powershell -ExecutionPolicy Bypass -File setup-ffmpeg.ps1
```

This is **optional** - the script works fine without it!

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
- **ffmpeg** → **Already included in this project!** (in the `ffmpeg/` folder)

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

### Step 3: (Optional) Add ffmpeg to PATH

> **Note:** ffmpeg is **already bundled with this project**. You don't need to download or install it separately!

#### Option A: Automatic Setup (Recommended for Windows)

If you want ffmpeg to be available system-wide, run this **once**:

```powershell
powershell -ExecutionPolicy Bypass -File setup-ffmpeg.ps1
```

Then choose:
- **1** for current session only (temporary, useful for testing)
- **2** to add permanently to Windows PATH (requires admin, recommended)

**What this does:** Adds the bundled `ffmpeg/bin` folder to your system PATH so you can use `ffmpeg` command anywhere.

#### Option B: Use ffmpeg Without Adding to PATH

The script will automatically find ffmpeg in the `ffmpeg/` folder, so you **don't need** to run the setup script. Just use the program normally:

```bash
python main.py
```

#### Option C: External ffmpeg (If You Prefer)

If you already have ffmpeg installed on your system:
- Windows: It will be used automatically if in PATH
- Linux: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`

Or provide custom path:
```bash
python main.py --ffmpeg "C:\path\to\ffmpeg\bin"
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
└── ffmpeg/                      # Bundled ffmpeg executable
    ├── bin/
    │   ├── ffmpeg.exe
    │   ├── ffplay.exe
    │   └── ffprobe.exe
    └── doc/                     # Documentation
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

1. **ffmpeg is included**: The script automatically detects and uses the bundled ffmpeg in the `ffmpeg/` folder. No need to download or install separately!

2. **Copyright Notice**: Downloading copyrighted content may be illegal in your jurisdiction. Always check the platform's terms of service and respect copyright laws.

3. **Download Speed**: Speed depends on your internet connection and video resolution.

4. **Duplicate Prevention**: If a file already exists, the script skips downloading it.

5. **OAuth Cache**: The script uses OAuth caching for better YouTube access. Cache files are automatically stored.

---

## 🔧 Troubleshooting

### Error: ❌ ffmpeg not found

This should rarely happen since ffmpeg is bundled.

**Solution 1 - Verify ffmpeg folder exists:**
- Make sure the `ffmpeg/` folder is in the project root
- Check that `ffmpeg/bin/ffmpeg.exe` exists

**Solution 2 - Use the setup script:**
```powershell
powershell -ExecutionPolicy Bypass -File setup-ffmpeg.ps1
```

**Solution 3 - Specify ffmpeg path directly:**
```bash
python main.py --ffmpeg ".\ffmpeg\bin"
```

**Solution 4 - Install external ffmpeg:**
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
