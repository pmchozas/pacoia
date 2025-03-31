from typing import Union
from model.audio.AudioAnalyzer import AudioAnalyzer
from model.audio.AudioDataPlotter import AudioDataPlotter
from model.audio.AudioFeedback import AudioFeedback
from model.asr.WhisperManager import WhisperManager 
from Utils import Utils
import matplotlib.pyplot as plt

class Controller:
  
    def __init__(self) -> None:
        Utils.login_hf()
        model_id, device, torch_dtype = Utils.default_config()

        self.asr_manager = WhisperManager(model_id, torch_dtype, device)


    def generate_outputs(self, audio_path: str) -> list[Union[str, plt.Figure]]:
        speech_data = self.asr_manager.transcribe(audio_path)
        rms = AudioAnalyzer.get_rms(audio_path)
        mean_snr = AudioAnalyzer.get_snr(rms)

        output = list()
        output.append(speech_data["text"])
        output.append(AudioDataPlotter.get_rms_plot(rms))
        output.append(AudioDataPlotter.get_snr_plot(rms))
        output.append(AudioFeedback.get_rms_feedback(rms))
        output.append(AudioFeedback.get_snr_feedback(mean_snr))

        output.append("Here will go LLM feedback")

        return output