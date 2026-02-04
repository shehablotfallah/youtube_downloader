# PowerShell script to add bundled ffmpeg to PATH
# Run with: powershell -ExecutionPolicy Bypass -File setup-ffmpeg.ps1

$ErrorActionPreference = "Stop"

# Find ffmpeg folder (try 'ffmpeg' first, then 'ffmpeg-*' patterns)
$ffmpegFolder = Get-ChildItem -Path $PSScriptRoot -Directory -Filter "ffmpeg" -ErrorAction SilentlyContinue | Select-Object -First 1

if (-not $ffmpegFolder) {
    $ffmpegFolder = Get-ChildItem -Path $PSScriptRoot -Directory -Filter "ffmpeg-*" -ErrorAction SilentlyContinue | Select-Object -First 1
}

if (-not $ffmpegFolder) {
    Write-Host "❌ Error: ffmpeg folder not found in $PSScriptRoot" -ForegroundColor Red
    Write-Host "Make sure 'ffmpeg' or 'ffmpeg-*/' folder is in the same directory as this script." -ForegroundColor Yellow
    exit 1
}

$ffmpegBinPath = Join-Path $ffmpegFolder.FullName "bin"
if (-not (Test-Path $ffmpegBinPath)) {
    Write-Host "❌ Error: $ffmpegBinPath does not exist" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Found ffmpeg at: $ffmpegBinPath" -ForegroundColor Green

# Ask user: add for this session only or permanently?
Write-Host ""
Write-Host "Choose installation type:" -ForegroundColor Cyan
Write-Host "1. Current session only (temporary)" -ForegroundColor Yellow
Write-Host "2. Permanently (requires admin)" -ForegroundColor Yellow
$choice = Read-Host "Enter 1 or 2"

if ($choice -eq "1") {
    # Add to current session PATH only
    $env:PATH = "$ffmpegBinPath;$env:PATH"
    Write-Host "✅ Added ffmpeg to PATH for this session only." -ForegroundColor Green
    Write-Host "⚠️  This will be lost when you close this terminal." -ForegroundColor Yellow
    
    # Verify
    $ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
    if ($ffmpeg) {
        Write-Host "✅ ffmpeg is now available: $($ffmpeg.Source)" -ForegroundColor Green
    } else {
        Write-Host "❌ ffmpeg not found in PATH after setup" -ForegroundColor Red
    }
}
elseif ($choice -eq "2") {
    # Add to system PATH permanently (requires admin)
    if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
        Write-Host "❌ Administrator rights required for permanent setup" -ForegroundColor Red
        Write-Host "Please run this script as Administrator." -ForegroundColor Yellow
        exit 1
    }
    
    # Get current PATH
    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "Machine")
    if ($currentPath -like "*$ffmpegBinPath*") {
        Write-Host "⚠️  ffmpeg path is already in system PATH" -ForegroundColor Yellow
    } else {
        # Add to PATH
        $newPath = "$ffmpegBinPath;$currentPath"
        [Environment]::SetEnvironmentVariable("PATH", $newPath, "Machine")
        Write-Host "✅ Added ffmpeg to system PATH permanently" -ForegroundColor Green
        Write-Host "📝 Please restart PowerShell or cmd for changes to take effect." -ForegroundColor Yellow
    }
}
else {
    Write-Host "❌ Invalid choice. Exiting." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Setup complete! You can now run: python main.py" -ForegroundColor Cyan
