import yt_dlp


def best_format_selector(ctx: dict):
    """Select the best video and the best audio that won't result in an mkv.
    NOTE: This is just an example and does not handle all cases"""

    # formats are already sorted worst to best
    formats = ctx.get("formats")[::-1]

    # acodec='none' means there is no audio
    best_video = next(
        f for f in formats if f["vcodec"] != "none" and f["acodec"] == "none"
    )

    # find compatible audio extension
    audio_ext = {"mp4": "m4a", "webm": "webm"}[best_video["ext"]]
    # vcodec='none' means there is no video
    best_audio = next(
        f
        for f in formats
        if (f["acodec"] != "none" and f["vcodec"] == "none" and f["ext"] == audio_ext)
    )

    # These are the minimum required fields for a merged format
    yield {
        "format_id": f'{best_video["format_id"]}+{best_audio["format_id"]}',
        "ext": best_video["ext"],
        "requested_formats": [best_video, best_audio],
        # Must be + separated list of protocols
        "protocol": f'{best_video["protocol"]}+{best_audio["protocol"]}',
    }


def main():
    URL = "https://www.youtube.com/watch?v=BaW_jenozKc"
    # retries, file_access_retries, fragment_retries,
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    file_name = None

    def file_name_hook(d):
        nonlocal file_name
        if d["status"] == "finished":
            file_name = d["filename"]

    ydl_opts = {
        "format": best_format_selector,
        "concurrent_fragment_downloads": 8,
        "progress_hooks": [file_name_hook],
        "retries": 10,
        "file_access_retries": 10,
        "fragment_retries": 10,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
    print(file_name)


if __name__ == "__main__":
    main()
