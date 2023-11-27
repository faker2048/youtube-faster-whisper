# YTWS: YouTube Download and Faster-Whisper Subtitle Generation Tool 🔥

YTWS, is a simple tool that downloads YouTube videos and creates subtitles quickly. It uses [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) for downloading and [`faster-whisper`](https://github.com/guillaumekln/faster-whisper) for transcribing, making it easy and efficient to use.

Essentially, YTWS is a **user-friendly** wrapper integrating yt-dlp and faster-whisper, simplifying the user experience.  

YTWS is short for YouTube Whisper.  

## ⭐ Features

- **Easy to Use**: Start without any hassle.
- **Fast Subtitle Generation**: Harness the speed of `faster-whisper`.
- **GPU Acceleration**: A simple guide for harnessing GPU power.

## 🪄 Functional
-  Downloading and Transcribing YouTube Videos/Audios
-  Only Downloading YouTube Videos/Audios
-  Only Transcribing Videos/Audios

## ⚙ Requirements


#### ffmpeg

For Ubuntu:
```bash
sudo apt install ffmpeg
```

For Python virtual environment (recommended):
```bash
conda install ffmpeg
```

For Windows scoop users:
```bash
scoop install ffmpeg
```

## Installation

Install YTWS easily with these commands:

```bash
pip install ytws
```
or
```bash
pip install git+https://github.com/faker2048/youtube-whisper.git
```

## 🚀 Usage

### Downloading and Transcribing YouTube Videos/Audios
To download and transcribe a video, simply run:

```bash
❯ ytws dt --help
Usage: ytws dt [OPTIONS]

  Download video/audio from Youtube and generate subtitles.

Options:
  -u, --url TEXT         Youtube URL.  [required]
  -n, --threads INTEGER  Number of threads to use.
  -f, --format TEXT      Download format. See: https://github.com/yt-dlp/yt-
                         dlp#format-selection-examples
  -t, --translate        Translate the subtitles to English.
  -m, --model_name TEXT  Name of the model to use. e.g.  (tiny, tiny.en, base,
                         base.en, small, small.en,          medium, medium.en,
                         large-v1, or large-v2, or large-v3), recommended: (large-v3)
  -r, --model_root TEXT  Root directory for the models.
  --cpu                  Use CPU instead of GPU. This is useful if you do not
                         have a GPU.
  -s, --srt_only         Only generate subtitles. Do not download video.
  -v, --video_only       Only download video. Do not generate subtitles.
  --help                 Show this message and exit.
```

Example:
```bash
ytws dt -u "https://www.youtube.com/watch?v=XXXXXXXX" -m large-v3 # Download and transcribe the video
ytws dt -u "https://www.youtube.com/watch?v=XXXXXXXX" -f "bestvideo+bestaudio/best" 
```

After running the command, the media file and the generated subtitles will be saved in the same directory as the video file.

### Only Downloading YouTube Videos/Audios

To download a video, simply run:

```bash
❯ ytws d --help
Usage: ytws d [OPTIONS]

  Download a video/audio from YouTube.

Options:
  -u, --url TEXT         The URL of the YouTube video or the filename to be
                         downloaded.  [required]
  -n, --threads INTEGER  The number of threads to use for downloading. Default
                         is 16.
  -f, --format TEXT      The download format. Options include:
                         'worstaudio[tbr>100]/bestaudio/best' for audio only,
                         'bestvideo[height>=1080]/bestvideo' for video only,
                         'bestvideo+bestaudio/best' for both video and audio
                         (default). Use 'best' for the best quality or specify
                         particular formats.
  --help                 Show this message and exit.
```

### Only Transcribing Videos/Audios

To transcribe a video, simply run:

```bash
❯ ytws t --help
Usage: ytws t [OPTIONS]

  Transcribe a video/audio file.

Options:
  -f, --file TEXT        The media file to be transcribed.  [required]
  -t, --translate        Translate the subtitles to English.
  -m, --model_name TEXT  Name of the model to use. e.g.  (tiny, tiny.en, base,
                         base.en, small, small.en,          medium, medium.en,
                         large-v1, or large-v2), recommended: (large-v2)
  -r, --model_root TEXT  Root directory for the models.
  --cpu                  Use CPU instead of GPU. This is useful if you do not
                         have a GPU.
  --help                 Show this message and exit.
```

Example:
```bash
ytws t -f "video.mp4" -m large-v3
```

After running the command, the generated subtitles will be saved in the same directory as the video file.



## 🛫 GPU Acceleration

For easy CUDA and cuDNN installation:
- Linux:
```bash
conda install cudnn
```

- Windows:

_Although using additional torch libraries may not be ideal, it's a straightforward approach for Windows (compared to Nvidia's official CUDA installation). Any alternative methods or suggestions are welcome!_
```bash
pip3 install torch --index-url https://download.pytorch.org/whl/cu118
```

After these settings, YTWS should work with a GPU.

## 🪄 Available Models

Visit [here](https://huggingface.co/guillaumekln) for more details.

## 🌟 Contributing to YTWS

We welcome contributions to YTWS! Your support makes a difference.

### How to Contribute
- **Fork, Clone, Branch**: Start by forking and cloning the repository, then work in separate branches.
- **Commit**: Follow the project standards and commit your changes.
- **Pull Request**: Submit a concise pull request (PR) to the main branch.

### Using Pre-Commit
To maintain code format:

```bash
pip install pre-commit
pre-commit install
```

Pre-commit will guide you through necessary checks and corrections. Feel free to reach out if you have any questions or suggestions!
