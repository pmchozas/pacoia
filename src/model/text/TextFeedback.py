from math import sqrt

from src.model.text import TextConstants


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
    feedback = ""

    if type_token_ratio < TextConstants.very_low_type_token_ratio_value:
        feedback = TextConstants.very_low_type_token_ratio

    elif type_token_ratio < TextConstants.low_type_token_ratio_value:
        feedback = TextConstants.low_type_token_ratio

    elif type_token_ratio < TextConstants.normal_type_token_ratio_value:
        feedback = TextConstants.normal_type_token_ratio

    elif type_token_ratio < TextConstants.high_type_token_ratio_value:
        feedback = TextConstants.high_type_token_ratio

    else:
        feedback = TextConstants.very_high_type_token_ratio

    return feedback


def _get_lexical_richness_feedback(measure_of_textual_lexical_richness: float) -> str:
    feedback = ""

    if measure_of_textual_lexical_richness < TextConstants.very_low_lexical_richness_value:
        feedback = TextConstants.very_low_lexical_richness

    elif measure_of_textual_lexical_richness < TextConstants.low_lexical_richness_value:
        feedback = TextConstants.low_lexical_richness

    elif measure_of_textual_lexical_richness < TextConstants.normal_lexical_richness_value:
        feedback = TextConstants.normal_lexical_richness

    elif measure_of_textual_lexical_richness < TextConstants.high_lexical_richness_value:
        feedback = TextConstants.high_lexical_richness

    else:
        feedback = TextConstants.very_high_type_token_ratio

    return feedback
