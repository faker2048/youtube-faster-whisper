from loguru import logger
from faster_whisper import WhisperModel


def initialize_whisper_model(model_name: str = "tiny.en"):
    try:
        return WhisperModel(model_name, device="cuda", compute_type="float16")
    except RuntimeError:
        logger.info(
            "WhisperModel could not be initialized with CUDA device. Falling back to CPU device."
        )
        return WhisperModel(model_name, device="cpu")
