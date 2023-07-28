from src.youtube_whisper.youtube_whisper import WhisperWrapper


def test_base_audio_to_text():
    yw = WhisperWrapper()
    segments, info = yw.model.transcribe(audio="data/jfk.flac")
    segments = list(segments)
    assert len(segments) > 0
    assert segments[0].no_speech_prob < 1
    assert info.language == "en"
    assert 20 > info.duration > 5  # about 11
