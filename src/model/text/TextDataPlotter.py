

from matplotlib import pyplot as plt
from numpy import arange


def get_frequencies_plot(word_frequencies: dict[str, int]) -> plt.Figure:
    categories: list[str] = list(word_frequencies.keys())
    values: list[int] = list(word_frequencies.values())

    fig, ax = plt.subplots()
    ax.bar(categories, values, color="red")

    for i, c in enumerate(categories):
        ax.text(i - 0.05, word_frequencies[c] + 0.05, c, ha="center", fontsize=10, rotation=75)

        ax.set_xlabel("Words")
        ax.set_ylabel("Appearances")
        ax.set_title("Word Frequencies")

        ax.set_xticks([])
        ax.set_yticks(arange(0, max(values) + 1, 1))
        ax.set_ylim(0, max(values) * 1.2)

    return fig
