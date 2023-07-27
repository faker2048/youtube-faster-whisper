import time

from faster_whisper import WhisperModel


def main():
    start_init = time.time()
    model = WhisperModel("tiny.en", device="cuda", compute_type="float16")
    end_init = time.time()
    print(f"Initialization took {end_init - start_init} seconds")

    start_inference = time.time()
    segments, info = model.transcribe("data/jfk.flac", "en", beam_size=5)

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    end_inference = time.time()
    print(f"Inference took {end_inference - start_inference} seconds")


if __name__ == "__main__":
    main()
