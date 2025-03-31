from typing import Union
from model.asr.CrisperWhisperManager import CrisperWhisperManager
from model.audio.AudioAnalyzer import AudioAnalyzer
from model.audio.AudioDataPlotter import AudioDataPlotter
from model.audio.AudioFeedback import AudioFeedback
from model.asr.WhisperManager import WhisperManager 
from Utils import Utils
import matplotlib.pyplot as plt

from model.text.TextAnalyzer import TextAnalyzer
from model.text.TextDataPlotter import TextDataPlotter
from model.text.TextFeedback import TextFeedback

class Controller:
  
    def __init__(self) -> None:
        Utils.login_hf()
        device, torch_dtype = Utils.default_config()

        self.asr_manager = WhisperManager(torch_dtype, device)
        # self.asr_manager = CrisperWhisperManager(torch_dtype, device)


    def generate_outputs_whisper(self, audio_path: str) -> list[Union[str, plt.Figure]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_word_frequencies(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)

        output = list()
        output.append(speech_data["text"])
        output.append(TextDataPlotter.get_frequencies_plot(word_frequencies))
        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(TextFeedback.get_frequencies_feedback(word_frequencies))
        output.append(AudioFeedback.get_rms_feedback(rms))
        output.append(AudioFeedback.get_snr_feedback(mean_snr))

        output.append("Here will go LLM feedback")

        return output
    

    def generate_outputs_crisper_whisper(self, audio_path: str) -> list[Union[str, plt.Figure]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_word_frequencies(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)
        word_count = len(word_frequencies)
        length = speech_data["chunks"][len(speech_data["chunks"]-1)]["timestamps"][1]

        output = list()
        output.append(speech_data["text"])
        output.append(TextDataPlotter.get_frequencies_plot(word_frequencies))
        output.append(TextFeedback.get_frequencies_feedback(word_frequencies))

        output.append(AudioDataPlotter.get_speaking_rate_plot(speech_data["chunks"], length))
        output.append(AudioFeedback.get_speaking_rate_feedback(word_count, length))

        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioFeedback.get_rms_feedback(rms))

        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioFeedback.get_snr_feedback(mean_snr))

        output.append("Here will go LLM feedback")

        return output