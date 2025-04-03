import numpy as np

def get_rms_feedback(rms: np.ndarray) -> str:
    mean_rms = np.mean(rms)

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


def get_snr_feedback(mean_snr: float) -> str:
    if mean_snr < 5:
        return "The audio is very hard to hear due to excessive background " \
            "noise. Speech is unclear, and it may be challenging to understand the " \
            "content. Significant improvements are needed for clarity."
    elif mean_snr < 10:
        return "The audio quality is poor, with noticeable background noise. " \
            "While speech is still somewhat audible, the overall clarity is " \
            "affected, making it harder to follow the conversation."
    elif mean_snr < 15:
        return "The audio is fairly clear, but there's noticeable background " \
            "noise. While the speech is still understandable, the quality can be " \
            "improved for a better listening experience."
    elif mean_snr < 20:
        return "The speech is clear and easy to understand, though there might " \
            "be slight background noise. Overall, it's good quality for most uses, " \
            "though a little enhancement could make it perfect."
    else:
        return "The audio is very clear with no noticeable background noise. " \
            "Speech is easily understandable, and the quality is ideal for " \
            "communication or professional use."


def get_speaking_rate_feedback(word_count: int, length: int) -> str:
    mean_rate = word_count / length

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