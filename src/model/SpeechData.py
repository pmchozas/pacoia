import matplotlib.pyplot as plt
import numpy as np
import librosa
import math

class SpeechData():
  def __init__(self, transcript: dict, audio: str):
    self.text: str = transcript["text"]
    self.y, self.sr = librosa.load(audio)
    self.rms: np.ndarray = librosa.feature.rms(y=self.y)[0]
    self.length: float = librosa.get_duration(y=self.y, sr=self.sr)
    self.snr: float = self._get_snr(self.rms)

  def get_speaking_rate(self, interval : int = 5) -> dict:
    pass

  def get_speaking_rate_plot(self, interval: int = 1):
    pass

  def get_speaking_rate_feedback(self) -> str:
    mean_rate = sum(self.word_frequencies.values()) / self.length

    if mean_rate < 70:
      return "Your speaking rate is quite slow, which may make the speech feel " \
        "overly drawn out. Consider increasing your pace slightly to maintain " \
        "engagement and improve fluidity."

    elif mean_rate < 110:
      return "Your speech is on the slower side, which could be beneficial for " \
        "clarity but might feel a bit sluggish. Consider speeding up a little to " \
        "maintain a more natural rhythm."

    elif mean_rate < 150:
      return "Your speaking rate is within the normal range, making your speech " \
        "clear and easy to follow. This is ideal for most conversational " \
        "and presentation settings."

    elif mean_rate < 190:
      return "You're speaking at a fast pace. While this shows enthusiasm, " \
        "it could make it harder for listeners to catch every word. Try slowing " \
        "down slightly to improve clarity."

    else:
      return "Your speaking rate is very fast, which might be overwhelming for " \
        "some listeners. Consider pausing occasionally to allow your audience to " \
        "absorb the information."

  def _set_word_frequencies(self):
    pass

  def get_frequencies_plot(self):
    pass

  def get_frequencies_feedback(self) -> str:
    unique_words = len(self.word_frequencies.keys())
    total_words = sum(self.word_frequencies.values())

    type_toke_ratio = unique_words / total_words
    measure_of_textual_lexical_richness = unique_words / math.sqrt(total_words)

    feedback = f"TTR: {type_toke_ratio:.2f}\n"

    if type_toke_ratio < 0.2:
      feedback += "Your speech is highly repetitive. Increase word variety " \
        "for better engagement and depth."

    elif type_toke_ratio < 0.4:
      feedback += "Vocabulary is somewhat repetitive. Consider expanding your " \
        "word choices to avoid redundancy."

    elif type_toke_ratio < 0.6:
      feedback += "Reasonable lexical diversity. Add more variety to improve " \
        "clarity and richness."

    elif type_toke_ratio < 0.8:
      feedback += "Excellent variety in word choice. This is ideal for more " \
        "formal or academic contexts."
    else:
      feedback += "Great diversity! Ensure balance between complexity and clarity."

    feedback += f"\n\nMTLR: {measure_of_textual_lexical_richness:.2f}\n"

    if measure_of_textual_lexical_richness < 0.5:
      feedback += "Limited lexical richness. Introduce more varied vocabulary " \
        "to avoid redundancy."

    elif measure_of_textual_lexical_richness < 1:
      feedback += "Room for improvement in lexical richness. Use more diverse " \
        "words to enhance engagement."

    elif measure_of_textual_lexical_richness < 1.5:
      feedback += "Moderate lexical richness. More variety can be added to make " \
       "the speech more engaging."

    elif measure_of_textual_lexical_richness < 2:
      feedback += "Solid lexical richness. Your vocabulary range is impressive " \
        "and engaging."
    else:
      feedback += "Highly lexically rich. Be mindful of clarity and balance " \
        "richness with simplicity."

    return feedback

  def get_rms_plot(self) -> plt.Figure:
    times = librosa.times_like(self.rms)
    fig, ax = plt.subplots()

    ax.plot(times, self.rms, label="RMS Energy", color='r')
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("RMS Energy")
    ax.set_title("RMS Energy Over Time")

    return fig

  def get_rms_feedback(self) -> str:
    mean_rms = np.mean(self.rms)

    if mean_rms < 0.05:
      return "Low mean RMS (soft speech, whispers): 0.01 - 0.05\n" \
        "Your speech is quite soft or whispered. Consider speaking a " \
        "bit louder to improve clarity, especially in environments" \
        "with background noise."

    elif mean_rms > 0.2:
      return "High mean RMS (loud speech, shouting): 0.2 - 0.5+\n" \
        "Your speech is loud or even close to shouting. Try to lower the " \
        "volume slightly to avoid straining your voice or overwhelming" \
        "the listener."

    else:
      return "Normal mean RMS (conversational speech): 0.05 - 0.2\n" \
        "Your speech is at a normal, conversational volume. This range is " \
        "ideal for clear communication in most environments."

  def _get_snr(self, rms: np.ndarray) -> float:
    noise_threshold = np.percentile(rms, 10)
    speech_energy = np.mean(rms[rms > noise_threshold])
    noise_energy = np.mean(rms[rms <= noise_threshold])

    return 10 * np.log10(speech_energy / noise_energy)

  def get_snr_plot(self) -> plt.Figure:
    window_size = 50
    noise_energy = np.array([np.percentile(self.rms[max(0, i-window_size):i+1], 10) for i in range(len(self.rms))])
    noise_energy[noise_energy == 0] = 1e-10
    snr_over_time = 10 * np.log10(self.rms / noise_energy)
    times = librosa.times_like(self.rms)
    fig, ax = plt.subplots()

    ax.plot(times, snr_over_time, label="SNR")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("SNR")
    ax.set_title("SNR Over Time")

    return fig

  def get_snr_feedback(self) -> str:
    if self.snr < 5:
      return "The audio is very hard to hear due to excessive background " \
        "noise. Speech is unclear, and it may be challenging to understand the " \
        "content. Significant improvements are needed for clarity."
    elif self.snr < 10:
      return "The audio quality is poor, with noticeable background noise. " \
        "While speech is still somewhat audible, the overall clarity is " \
        "affected, making it harder to follow the conversation."
    elif self.snr < 15:
      return "The audio is fairly clear, but there's noticeable background " \
        "noise. While the speech is still understandable, the quality can be " \
        "improved for a better listening experience."
    elif self.snr < 20:
      return "The speech is clear and easy to understand, though there might " \
        "be slight background noise. Overall, it's good quality for most uses, " \
        "though a little enhancement could make it perfect."
    else:
      return "The audio is very clear with no noticeable background noise. " \
        "Speech is easily understandable, and the quality is ideal for " \
        "communication or professional use."
