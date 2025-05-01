from typing import Union

import matplotlib.pyplot as plt

from src.model.llm.LLMPeer import LLMPeer
from src import Utils
from src.model.asr.CrisperWhisperManager import CrisperWhisperManager
from src.model.asr.WhisperManager import WhisperManager
from src.model.audio import AudioAnalyzer, AudioDataPlotter, AudioFeedback
from src.model.text import TextAnalyzer, TextDataPlotter, TextFeedback


class Controller:
    def __init__(self, model: str, llm_peer: LLMPeer) -> None:
        Utils.login_hf()
        device = Utils.default_device()
        torch_dtype = Utils.default_dtype()
        self.model = model
        self.llm_peer = llm_peer

        if model == "CrisperWhisper":
            self.asr_manager: Union[WhisperManager, CrisperWhisperManager] = \
                CrisperWhisperManager(torch_dtype, device)
        else:
            self.asr_manager = WhisperManager(torch_dtype, device)

    def generate_outputs_whisper(self, audio_path: str) -> list[Union[str, plt.Figure]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_word_frequencies(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)
        word_count = len(word_frequencies)
        length = speech_data["chunks"][len(speech_data["chunks"]) - 1]["timestamp"][1]
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

        punctuated_transcription = self.llm_peer.get_punctuated_transcription(speech_data["text"])
        
        output.append(self.llm_peer.get_introduction_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_background_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_innovation_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_description_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_organization_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_language_evaluation(punctuated_transcription))

        return output

    def generate_outputs_crisper_whisper(self, audio_path: str) -> list[Union[str, plt.Figure]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        word_frequencies = TextAnalyzer.get_word_frequencies(speech_data["text"])
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)
        word_count = len(word_frequencies)
        length = speech_data["chunks"][len(speech_data["chunks"]) - 1]["timestamp"][1]
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

        punctuated_transcription = self.llm_peer.get_punctuated_transcription(speech_data["text"])
        
        output.append(self.llm_peer.get_introduction_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_background_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_innovation_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_description_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_organization_evaluation(punctuated_transcription))
        output.append(self.llm_peer.get_language_evaluation(punctuated_transcription))

        return output
