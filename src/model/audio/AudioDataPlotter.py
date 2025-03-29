import matplotlib.pyplot as plt
import librosa
import numpy as np

class AudioDataPlotter:

    @staticmethod
    def get_rms_plot(rms: np.ndarray) -> plt.Figure:
        times = librosa.times_like(rms)
        fig, ax = plt.subplots()

        ax.plot(times, rms, label="RMS Energy", color='r')
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("RMS Energy")
        ax.set_title("RMS Energy Over Time")

        return fig


    @staticmethod
    def get_snr_plot(rms: np.ndarray) -> plt.Figure:
        window_size = 50
        noise_energy = np.array([np.percentile(rms[max(0, i-window_size):i+1], 10) for i in range(len(rms))])
        noise_energy[noise_energy == 0] = 1e-10
        snr_over_time = 10 * np.log10(rms / noise_energy)
        times = librosa.times_like(rms)
        fig, ax = plt.subplots()

        ax.plot(times, snr_over_time, label="SNR")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("SNR")
        ax.set_title("SNR Over Time")

        return fig


    @staticmethod
    def get_speaking_rate_plot():
        pass