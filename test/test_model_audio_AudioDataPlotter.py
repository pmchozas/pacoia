import librosa
import src.model.audio.AudioDataPlotter as AudioDataPlotter
import src.model.audio.AudioAnalyzer as AudioAnalyzer
import numpy as np
import matplotlib.pyplot as plt

class TestAudioDataPlotter:
    def sample_rms(self):
        y, _ = librosa.load(librosa.ex('trumpet'))
        return librosa.feature.rms(y=y)[0]

    def test_get_rms_plot(self):
        plot = AudioDataPlotter.get_rms_plot(self.sample_rms())
        assert type(plot) == plt.Figure
        plt.close(plot)

    def test_get_snr_plot(self):
        plot = AudioDataPlotter.get_rms_plot(self.sample_rms())
        assert type(plot) == plt.Figure
        plt.close(plot)

    def test_get_speaking_rate_plot(self):
        speaking_rate = AudioAnalyzer.get_speaking_rate("Whisper", [{"text": "texto", "timestamp": (0, 1)}], 1)
        assert type(AudioDataPlotter.get_speaking_rate_plot(speaking_rate)) == plt.Figure