from math import sqrt
import src.model.text.TextMessages as TextMessages

def get_frequencies_feedback(word_frequencies: dict[str, int]) -> str:
    unique_words = len(word_frequencies.keys())
    total_words = sum(word_frequencies.values())

    type_token_ratio = unique_words / total_words
    measure_of_textual_lexical_richness = unique_words / sqrt(total_words)

    feedback = f"TTR: {type_token_ratio:.2f}\n"
    feedback += _get_type_token_ratio_feedback(type_token_ratio)

    feedback += f"\n\nMTLR: {measure_of_textual_lexical_richness:.2f}\n"
    feedback += _get_lexical_richness_feedback(measure_of_textual_lexical_richness)

    return feedback


def _get_type_token_ratio_feedback(type_token_ratio: float) -> str:
    feedback = str()

    if type_token_ratio < 0.2:
        feedback = TextMessages.very_low_type_token_ratio

    elif type_token_ratio < 0.4:
        feedback = TextMessages.low_type_token_ratio

    elif type_token_ratio < 0.6:
        feedback = TextMessages.normal_type_token_ratio

    elif type_token_ratio < 0.8:
        feedback = TextMessages.high_type_token_ratio
    
    else:
        feedback = TextMessages.very_high_type_token_ratio
    
    return feedback


def _get_lexical_richness_feedback(measure_of_textual_lexical_richness: float) -> str:
    feedback = str()

    if measure_of_textual_lexical_richness < 0.5:
        feedback = TextMessages.very_low_lexical_richness

    elif measure_of_textual_lexical_richness < 1:
        feedback = TextMessages.low_lexical_richness

    elif measure_of_textual_lexical_richness < 1.5:
        feedback = TextMessages.normal_lexical_richness

    elif measure_of_textual_lexical_richness < 2:
        feedback = TextMessages.high_lexical_richness
    else:
        feedback = TextMessages.very_high_type_token_ratio
    
    return feedback