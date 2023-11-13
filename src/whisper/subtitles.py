import os
from typing import Iterable
from loguru import logger
from faster_whisper.transcribe import Segment


def format_timestamp(seconds: float) -> str:
    milliseconds = round(seconds * 1000)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def write_srt(segments: Iterable[Segment], file: str) -> None:
    """Write segments to a SRT file."""
    if not file.endswith(".srt"):
        file += ".srt"

    if os.path.exists(file):
        logger.info(f"File {file} already exists. Skipping.")
        return

    with open(file=file + ".tmp", mode="w", encoding="utf-8") as f:
        for i, segment in enumerate(segments, start=1):
            text = segment.text.strip()

            s: str = f"""
{i}
{format_timestamp(segment.start)} --> {format_timestamp(segment.end)}
{text}

"""
            f.write(s)
            print(s)


    os.rename(file + ".tmp", file)
