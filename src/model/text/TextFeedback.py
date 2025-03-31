import math

class TextFeedback:

    @staticmethod
    def get_frequencies_feedback(word_frequencies: dict[str, int]) -> str:
        unique_words = len(word_frequencies.keys())
        total_words = sum(word_frequencies.values())

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