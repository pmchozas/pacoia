from pydub import AudioSegment

class AudioManager:

  def split_audio(audio_path: str, chunk_length_ms: int = 90000) -> list:
    audio = AudioSegment.from_file(audio_path)
    chunks = [audio[i : i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks