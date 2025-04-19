from typing import Union
from src.model.asr.CrisperWhisperManager import CrisperWhisperManager
import src.model.audio.AudioAnalyzer as AudioAnalyzer
import src.model.audio.AudioDataPlotter as AudioDataPlotter
import src.model.audio.AudioFeedback as AudioFeedback
from src.model.asr.WhisperManager import WhisperManager 
import src.Utils as Utils
import matplotlib.pyplot as plt
import src.model.text.TextAnalyzer as TextAnalyzer
import src.model.text.TextDataPlotter as TextDataPlotter
import src.model.text.TextFeedback as TextFeedback

class Controller:
    def __init__(self, model: str) -> None:
        Utils.login_hf()
        device, torch_dtype = Utils.default_config()
        self.model = model

        if model == "CrisperWhisper":
            self.asr_manager: Union[WhisperManager,CrisperWhisperManager] = \
                CrisperWhisperManager(torch_dtype, device)
        else:
            self.asr_manager = WhisperManager(torch_dtype, device)


    def generate_outputs_whisper(self, audio_path: str) -> list[Union[str, plt.Figure]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_word_frequencies(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)
        word_count = len(word_frequencies)
        length = speech_data["chunks"][len(speech_data["chunks"])-1]["timestamp"][1]
        rates = AudioAnalyzer.get_speaking_rate(self.model, speech_data["chunks"], length)

        output = list()
        output.append(speech_data["text"])
        output.append(TextDataPlotter.get_frequencies_plot(word_frequencies))
        output.append(TextFeedback.get_frequencies_feedback(word_frequencies))

        output.append(AudioDataPlotter.get_speaking_rate_plot(rates, length))
        output.append(AudioFeedback.get_speaking_rate_feedback(word_count, length))

        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioFeedback.get_rms_feedback(rms))

        output.append(AudioDataPlotter.get_snr_plot(rms))
        output.append(AudioFeedback.get_snr_feedback(mean_snr))


        output.append("Here will go LLM feedback")

        return output
    

    def generate_outputs_crisper_whisper(self, audio_path: str) -> list[Union[str, plt.Figure]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_word_frequencies(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)
        word_count = len(word_frequencies)
        length = speech_data["chunks"][len(speech_data["chunks"])-1]["timestamp"][1]
        rates = AudioAnalyzer.get_speaking_rate(self.model, speech_data["chunks"], length)

        output = list()
        output.append(speech_data["text"])
        output.append(TextDataPlotter.get_frequencies_plot(word_frequencies))
        output.append(TextFeedback.get_frequencies_feedback(word_frequencies))

        output.append(AudioDataPlotter.get_speaking_rate_plot(rates, length))
        output.append(AudioFeedback.get_speaking_rate_feedback(word_count, length))

        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioFeedback.get_rms_feedback(rms))

        output.append(AudioDataPlotter.get_snr_plot(rms))
        output.append(AudioFeedback.get_snr_feedback(mean_snr))

        output.append("Here will go LLM feedback")

        return output