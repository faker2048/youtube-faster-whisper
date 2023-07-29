from src.youtube.download import download, download_audio
from src.whisper.transcribe import initialize_whisper_model
import asyncio
from concurrent.futures import ThreadPoolExecutor


async def main():
    executor = ThreadPoolExecutor(max_workers=2)
    loop = asyncio.get_event_loop()

    def task_audio():
        URL = "https://www.youtube.com/watch?v=3AtDnEC4zak"
        return download_audio(URL)

    model = initialize_whisper_model(model_name="tiny.en")
    file_name = task_audio()

    segs, info = model.transcribe(audio=file_name)

    for seg in segs:
        print(seg.text)


if __name__ == "__main__":
    asyncio.run(main())
