import librosa
import numpy as np
import pandas as pd


def get_rms_plot(rms: np.ndarray) -> pd.DataFrame:
    low_threshold = 0.05
    high_threshold = 0.2
    rms_ds, times_ds = downsample(rms, librosa.times_like(rms))

    return pd.DataFrame({
        "x": list(times_ds) * 3,
        "y": list(rms_ds) + [low_threshold] * len(times_ds) + [high_threshold] * len(times_ds),
        "name": ["RMS"] * len(times_ds) +
                ["Low RMS"] * len(times_ds) +
                ["High RMS"] * len(times_ds),
    })


def get_snr_plot(rms: np.ndarray) -> pd.DataFrame:
    window_size = 50
    noise_energy = np.array([np.percentile(rms[max(0, i - window_size):i + 1], 10) for i in range(len(rms))])
    noise_energy[noise_energy == 0] = 1e-10
    snr_over_time = 10 * np.log10(rms / noise_energy)
    times = librosa.times_like(rms)
    low_threshold = 10
    high_threshold = 20

    snr_ds, times_ds = downsample(snr_over_time, times)
    return pd.DataFrame({
        "x": list(times_ds) * 3,
        "y": list(snr_ds) + [low_threshold] * len(times_ds) + [high_threshold] * len(times_ds),
        "name": ["SNR"] * len(times_ds) +
                ["Low SNR"] * len(times_ds) +
                ["High SNR"] * len(times_ds),
    })


def get_speaking_rate_plot(rates: dict) -> pd.DataFrame:
    return pd.DataFrame({
        "Time (s)": list(rates.keys()),
        "Words per minute": list(rates.values()),
    })


def downsample(array: np.ndarray,
               times: np.ndarray,
               max_points: int = 500) -> tuple[np.ndarray, np.ndarray]:

    step = max(1, len(array) // max_points)
    rms_ds = array[::step]
    times_ds = times[::step]
    return rms_ds, times_ds
