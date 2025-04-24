import re
from collections import Counter

import textstat

from src.model.text import TextAnalyzer


def get_words(text: str) -> list[str]:
    return re.findall(r"\b\w+(?:[-']\w+)*\b", text)


def get_word_frequencies(text: str) -> dict[str, int]:
    words = TextAnalyzer.get_words(text)
    lower_case_words = list()
    for word in words:
        lower_case_words.append(re.sub(r"[^\w\s']", "", word.lower()))
    frequencies = Counter(lower_case_words)
    return dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))


def get_flesch_reading_ease(text: str) -> float:
    return textstat.flesch_reading_ease(text)


def get_flesch_kincaid_grade(text: str) -> float:
    return textstat.flesch_kincaid_grade(text)


def get_smog_index(text: str) -> float:
    return textstat.smog_index(text)


def get_coleman_liau_index(text: str) -> float:
    return textstat.coleman_liau_index(text)


def get_automated_readability_index(text: str) -> float:
    return textstat.automated_readability_index(text)


def get_dale_chall_readability_score(text: str) -> float:
    return textstat.dale_chall_readability_score(text)


def get_difficult_words(text: str) -> int:
    return textstat.difficult_words(text)


def get_linsear_write_formula(text: str) -> float:
    return textstat.linsear_write_formula(text)


def get_gunning_fog(text: str) -> float:
    return textstat.gunning_fog(text)


def get_text_standard(text: str) -> float:
    return textstat.text_standard(text)
