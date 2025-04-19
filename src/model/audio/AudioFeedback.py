from numpy import ndarray, mean
import src.model.audio.AudioMessages as AudioMessages

def get_rms_feedback(rms: ndarray) -> str:
    mean_rms = mean(rms)

    if mean_rms < 0.05:
        return AudioMessages.low_mean_rms
    
    elif mean_rms > 0.2:
        return AudioMessages.high_mean_rms
    
    else:
        return AudioMessages.normal_mean_rms


def get_snr_feedback(mean_snr: float) -> str:
    if mean_snr < 5:
        return AudioMessages.very_low_mean_snr
    
    elif mean_snr < 10:
        return AudioMessages.low_mean_snr
    
    elif mean_snr < 15:
        return AudioMessages.normal_mean_snr
    
    elif mean_snr < 20:
        return AudioMessages.high_mean_snr

    else:
        return AudioMessages.very_high_snr


def get_speaking_rate_feedback(word_count: int, length: int) -> str:
    mean_rate = word_count / length

    if mean_rate < 70:
        return AudioMessages.very_slow_speaking_rate

    elif mean_rate < 110:
        return AudioMessages.slow_speaking_rate

    elif mean_rate < 150:
        return AudioMessages.normal_speaking_rate

    elif mean_rate < 190:
        return AudioMessages.fast_speaking_rate

    else:
        return AudioMessages.very_fast_speaking_rate