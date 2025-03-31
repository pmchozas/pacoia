from collections import Counter
import re

class TextAnalyzer:
    
    @staticmethod
    def get_words(text: str) -> list[str]:
        return re.findall(r"\b\w+(?:[-']\w+)*\b", text)
    

    @staticmethod
    def get_word_frequencies(text: str) -> dict[str, int]:
        words = TextAnalyzer.get_words(text)
        lower_case_words = list()
        for word in words:
            lower_case_words.append(re.sub(r"[^\w\s']", "", word.lower()))
        frequencies = Counter(lower_case_words)
        return dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
    