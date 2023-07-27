import time

from faster_whisper import WhisperModel


def main():
    start_init = time.time()  # 开始初始化的时间
    model = WhisperModel("tiny.en", device="cuda", compute_type="float16")
    end_init = time.time()  # 结束初始化的时间
    print(f"Initialization took {end_init - start_init} seconds")

    start_inference = time.time()  # 开始推理的时间
    segments, info = model.transcribe("data/jfk.flac", "en", beam_size=5)

    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
    end_inference = time.time()  # 结束推理的时间
    print(f"Inference took {end_inference - start_inference} seconds")


if __name__ == "__main__":
    main()
