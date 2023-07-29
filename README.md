# 🎥 YTWS: YouTube Download and Subtitle Generation Tool 🔥

![YTWS](https://images.unsplash.com/photo-1511379938547-c1f69419868d)

YTWS is a command-line tool designed to download videos from YouTube and generate subtitles, all with the power of the efficient `faster-whisper`.

## 💽 Installation
You can easily install YTWS using the following commands:
```bash
git clone https://github.com/faker2048/youtube-whisper
cd youtube-whisper
pip install .
```

### Preparations Before Running

_Principle: Simplicity is key, and there should be no side effects._

#### ffmpeg
If you don't have ffmpeg installed, you can use the standard method to install ffmpeg in your computer's global environment (not detailed here), or you can use conda to install it in your Python virtual environment (recommended):
```
conda install ffmpeg
```
#### GPU Acceleration
If you have not installed the CUDA, cudnn suite, and are looking for a straightforward installation method, you may refer to the following:
- Linux
```
conda install cudnn
```
- Windows
```
pip3 install torch --index-url https://download.pytorch.org/whl/cu118

# Installing additional torch libraries may not be the best method, but it's currently the most 
# convenient ways I've found for Windows (compared to Nvidia's official CUDA installation). 
# If you know of a better ways, your contributions are welcome!
```

## 🪄 Available Model

Visit https://huggingface.co/guillaumekln for more details.

## 🚀 Quick Start
You can begin downloading YouTube videos and generating subtitles right away. Here's a simple example of how to use YTWS:

```bash
# To download videos from YouTube and generate subtitles.
ytws -m large-v2 -u https://www.youtube.com/watch?v=nWvCd8lC4_Q 
```

```bash
# To generate .srt subtitles only. (This will download only the audio and delete it after transcribing)
ytws -m large-v2 -u https://www.youtube.com/watch?v=nWvCd8lC4_Q --srt_only
```

```bash
# Runs on cpu
ytws -u https://www.youtube.com/watch?v=nWvCd8lC4_Q --cpu
```

Please replace `https://www.youtube.com/watch?v=nWvCd8lC4_Q` with the URL of the YouTube video you wish to download.

For more customized options like downloading only the video or generating only the subtitles, you can use the `--video_only` or `--srt_only` options.

## 🎛️ Custom Settings
For further details and customization options, please refer to the help information:

```bash
ytws --help
```

We hope you find this tool beneficial and should you require further assistance, feel free to reach out. Happy downloading!