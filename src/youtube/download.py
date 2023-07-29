import yt_dlp


# audio only format: "worstaudio[tbr>100]/bestaudio/best"
# video only format: "bestvideo[height>=1080]/bestvideo"
# video and audio format: "bestvideo+bestaudio/best"
def download(
    url: str, threads: int = 8, format: str = "bestvideo+bestaudio/best"
) -> str:
    """Download a video from YouTube and return the file name."""
    file_name = ""

    def file_name_hook(d):
        nonlocal file_name
        if d["status"] == "finished":
            file_name = d["filename"]

    ydl_opts = {
        "format": format,
        "concurrent_fragment_downloads": threads,
        "progress_hooks": [file_name_hook],
        "retries": 10,
        "file_access_retries": 10,
        "fragment_retries": 10,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return file_name


def download_audio(
    url: str, threads: int = 8, format: str = "worstaudio[tbr>100]/bestaudio/best"
) -> str:
    return download(url, threads, format)
