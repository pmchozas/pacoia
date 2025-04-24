import librosa
import numpy as np


def get_rms(audio_path: str) -> np.ndarray:
    y, _ = librosa.load(audio_path)
    return librosa.feature.rms(y=y)[0]


def get_snr(rms: np.ndarray) -> float:
    noise_threshold = np.percentile(rms, 10)
    speech_energy = np.mean(rms[rms > noise_threshold])
    noise_energy = np.mean(rms[rms <= noise_threshold])

    return 10 * np.log10(speech_energy / noise_energy)


def get_speaking_rate(model: str, chunks: list, length: int, interval: int = 5) -> dict:
    rates = dict()

    if model == "CrisperWhisper":
        for i in range(0, round(length), interval):
            rates[i] = (sum([c["timestamp"][1] > i and c["timestamp"][1] < i + interval for c in chunks]) / interval) * 60

        return dict(sorted(rates.items(), key=lambda item: item[0]))
    for i in range(len(chunks)):
        c = chunks[i]
        inter = c["timestamp"][1] - c["timestamp"][0]
        rates[i] = (len(c["text"].split(" ")) / inter) * 60

    return dict(sorted(rates.items(), key=lambda item: item[0]))
