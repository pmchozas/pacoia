import src.model.text.TextDataPlotter as TextDataPlotter
import src.model.text.TextAnalyzer as TextAnalyzer
import matplotlib.pyplot as plt

class TestTextDataPlotter:

    def test_get_rms_plot(get_frequencies_plot):
        frequencies = TextAnalyzer.get_word_frequencies("hola")
        assert type(TextDataPlotter.get_frequencies_plot(frequencies)) == plt.Figure