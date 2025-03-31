import librosa
import numpy as np

class AudioAnalyzer:
  
    @staticmethod
    def get_rms(audio_path: str) -> np.ndarray:
        y, _ = librosa.load(audio_path)
        return librosa.feature.rms(y=y)[0]
    

    @staticmethod
    def get_snr(rms: np.ndarray) -> float:
        noise_threshold = np.percentile(rms, 10)
        speech_energy = np.mean(rms[rms > noise_threshold])
        noise_energy = np.mean(rms[rms <= noise_threshold])

        return 10 * np.log10(speech_energy / noise_energy)


    @staticmethod
    def get_speaking_rate() -> None:
        pass