from loguru import logger
from faster_whisper import WhisperModel


def initialize_whisper_model(
    model_name: str = "tiny.en", model_root: str | None = None
):
    logger.info(f"Initializing WhisperModel with model {model_name}.")
    try:
        return WhisperModel(
            model_name, device="cuda", compute_type="float16", download_root=model_root
        )
    except RuntimeError:
        logger.info(
            "WhisperModel could not be initialized with CUDA device.\
                  Falling back to CPU device."
        )
        return WhisperModel(model_name, device="cpu", download_root=model_root)
