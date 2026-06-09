from fire_and_ice_adofai.models import AudioAnalysis


def analyze_audio(audio_path: str, max_beats: int = 256) -> AudioAnalysis:
    return AudioAnalysis(bpm=120.0, offset=0.0, beats=[])
