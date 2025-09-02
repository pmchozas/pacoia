from typing import Any, Callable, Union

import gradio as gr
import pandas as pd


def show_group(arg) -> dict[str, Any]:
    return gr.update(visible=True)


def hide_group(arg) -> dict[str, Any]:
    return gr.update(visible=False)


def show_submit(selected: bool) -> dict[str, Any]:
    return gr.update(visible=True) if selected else gr.update(visible=False)


def handle_llm_checkbox(selected: str) -> tuple[dict[str, Any], dict[str, Any]]:
    if selected == "Yes":
        return gr.update(visible=True), gr.update(visible=False)
    return gr.update(visible=False), gr.update(visible=True)


def handle_base_checkbox(selected: str) -> tuple[dict[str, Any], dict[str, Any]]:
    if selected == "Transcription":
        return gr.update(visible=True), gr.update(visible=False)
    return gr.update(visible=False), gr.update(visible=True)


def reset() -> dict[str, Any]:
    return (gr.update(visible=False))


class WhisperInterface:
    def __init__(self, function_ptr: Callable[[str, str, list[str], list[str]], Union[tuple[str, str], list[Union[str, pd.DataFrame]]]]) -> None:
        title = "PACOIA: Plataforma Automatizada para la evaluación de Comunicación Oral en Inglés Académico"
        css = "footer{display:none !important}"

        with gr.Blocks(title=title, css=css, theme=gr.themes.Soft()) as self.blocks:
            with gr.Row():
                gr.Markdown("# 📄 Plataforma Automatizada para la evaluación de Comunicación Oral en Inglés Académico")
            with gr.Row():
                audio_box = gr.Audio(type="filepath", label="Upload a .wav or .mp3 file")

            with gr.Group(visible=False) as base_options_group:
                with gr.Row():
                    base_options = gr.Radio(["Transcription", "Audio"], label="Choose the way you want the platform to analyze your presentation")

            with gr.Group(visible=False) as llm_options_group:
                with gr.Row():
                    activate_llm = gr.Radio(["Yes", "No"], label="Do you want to use the AI advanced capabilities?")

            with gr.Group(visible=False) as options_group:
                with gr.Row():
                    sections_checkbox = gr.CheckboxGroup(
                        choices=[
                            "Introduction",
                            "Background",
                            "Innovation",
                            "Description",
                        ],
                        label="Choose the parts to be graded",
                    )
                    general_sections_checkbox = gr.CheckboxGroup(
                        choices=[
                            "Organization",
                            "Language",
                            "Highlight Words",
                            "Topic and Related Words",
                        ],
                        label="Choose additional features to be graded",
                    )

            with gr.Group(visible=False) as submit_group:
                with gr.Row():
                    submit_btn = gr.Button("Submit", variant="primary")

            with gr.Group(visible=False) as audio_submit_group:
                with gr.Row():
                    audio_submit_btn = gr.Button("Submit", variant="primary")

            with gr.Group(visible=False) as loading_group:
                with gr.Row():
                    gr.Image(value="https://i.sstatic.net/hzk6C.gif", label="Loading...")
                with gr.Row():
                    stop_btn = gr.Button("Stop Execution")

            with gr.Group(visible=False) as audio_results_group:
                with gr.Row():
                    audio_feedback = gr.Markdown(label="Feedback", line_breaks=True)
                with gr.Row():
                    audio_reset_btn = gr.Button("Clear results")
                with gr.Row():
                    audio_feedback_status = gr.Textbox(label="Status", visible=False)

            with gr.Group(visible=False) as results_group:
                with gr.Row():
                    transcription = gr.Textbox(label="Transcription")

                with gr.Row():
                    gr.Markdown("# 📃 Evaluation Results:")

                with gr.Row():
                    gr.Markdown("<br><br>")
                with gr.Row():
                    gr.Markdown("## 📊 Words Distribution")

                with gr.Row():
                    words_distribution_plot = gr.BarPlot(
                        label="Words Distribution",
                        x="Word",
                        y="Appearances",
                        title="Words Distribution",
                        x_title="Words",
                        y_title="Appearances",
                        x_axis_labels_visible=False,
                    )
                with gr.Row():
                    words_distribution_feedback = gr.Markdown(label="Words Distribution Feedback", line_breaks=True)

                with gr.Row():
                    gr.Markdown("<br><br>")
                with gr.Row():
                    gr.Markdown("## 🧠 Lexical Richness")

                with gr.Row():
                    gr.HTML("""
                    <details>
                        <summary>Lexical Richness Metrics Documentation</summary>
                            <div style="padding: 1em;">
                                <h2>What is Lexical Richness?</h2>
                                <p>
                                    Lexical richness refers to the diversity and sophistication of vocabulary used in a
                                    text. It is an important indicator in fields such as linguistics, education, and
                                    computational text analysis. A text with high lexical richness uses a wide range
                                    of vocabulary with less repetition.
                                </p>

                                <h3>1. Corrected Type-Token Ratio (CTTR)</h3>
                                <p>
                                    CTTR adjusts the traditional Type-Token Ratio (TTR) to minimize its sensitivity to text
                                    length. It measures vocabulary diversity by comparing the number of unique words (types)
                                    to the total number of words (tokens).
                                </p>
                                <p>
                                    <strong>Formula:</strong><br>
                                    <code>CTTR = (Types / √(2 x Tokens))</code>
                                </p>
                                <p>
                                    A higher CTTR value suggests greater lexical diversity.
                                </p>

                                <h3>2. Yule's K</h3>
                                <p>
                                    Yule's K measures lexical repetition in a text. Lower values indicate a higher diversity of
                                    vocabulary, while higher values reflect more repetition.
                                </p>
                                <p>
                                    <strong>Formula:</strong><br>
                                    <code>K = 10,000 x (Σ (f² x Vf) - N) / N²</code><br>
                                    Where:
                                    <ul>
                                        <li><strong>f</strong> = frequency of word</li>
                                        <li><strong>Vf</strong> = number of words with frequency f</li>
                                        <li><strong>N</strong> = total number of words</li>
                                    </ul>
                                </p>

                                <h3>3. Simpson's D</h3>
                                <p>
                                    Originally developed in ecology, Simpson's D measures the probability that two randomly selected
                                    words from a text are the same. It reflects lexical concentration.
                                </p>
                                <p>
                                    <strong>Formula:</strong><br>
                                    <code>D = Σ (ni x (ni - 1)) / (N x (N - 1))</code><br>
                                    Where:
                                    <ul>
                                        <li><strong>ni</strong> = frequency of each unique word</li>
                                        <li><strong>N</strong> = total number of words</li>
                                    </ul>
                                </p>
                                <p>
                                    A higher value of D indicates lower lexical diversity.
                                </p>

                                <h3>4. Herdan's C (also known as Herdan's VM)</h3>
                                <p>
                                    Herdan's C is another vocabulary diversity metric that is less sensitive to text length.
                                    It uses logarithmic scaling of types and tokens.
                                </p>
                                <p>
                                    <strong>Formula:</strong><br>
                                    <code>C = log(Types) / log(Tokens)</code>
                                </p>
                                <p>
                                    A higher Herdan's C value indicates richer vocabulary usage.
                                </p>
                            </div>
                        </details>
                    """)
                with gr.Row():
                    lexical_richness_feedback = gr.Markdown(label="Frequencies feedback", line_breaks=True)

                with gr.Row():
                    gr.Markdown("<br><br>")
                with gr.Row():
                    gr.Markdown("## 📚 Readability")
                with gr.Row():
                    gr.HTML("""
                    <details>
                        <summary>Readability Metrics Documentation</summary>
                            <div style="padding: 1em;">
                                <h2>What is Readability?</h2>
                                <p>
                                    Readability refers to how easy it is to read and understand a piece of text.
                                    It considers factors such as sentence length, word complexity, and vocabulary familiarity.
                                    Various formulas have been developed to estimate the readability of a text, often expressed
                                    as a U.S. school grade level or a score.
                                </p>

                                <h3>1. Flesch-Kincaid Reading Ease</h3>
                                <p>
                                    This test assigns a score from 0 to 100 to indicate how easy a text is to read. Higher scores
                                    indicate easier texts.
                                </p>
                                <p>
                                    <strong>Formula:</strong>
                                    <code>206.835 - (1.015 x ASL) - (84.6 x ASW)</code><br>
                                    Where:
                                    <ul>
                                        <li><strong>ASL</strong> = Average Sentence Length (words per sentence)</li>
                                        <li><strong>ASW</strong> = Average Syllables per Word</li>
                                    </ul>
                                </p>
                                <p>
                                    A score of 60-70 is considered easily understandable by 13- to 15-year-old students.
                                </p>

                                <h3>2. Flesch-Kincaid Grade Level</h3>
                                <p>
                                    This formula translates the reading ease score into a U.S. school grade level. For example,
                                    a score of 8.0 means the text is understandable by an 8th grader.
                                </p>
                                <p>
                                    <strong>Formula:</strong>
                                    <code>(0.39 x ASL) + (11.8 x ASW) - 15.59</code>
                                </p>

                                <h3>3. Dale-Chall Readability Formula</h3>
                                <p>
                                    The Dale-Chall Index considers the number of difficult words (i.e., words not on a list of 3,000 familiar words)
                                    and the average sentence length. It is particularly effective for assessing comprehension difficulty.
                                </p>
                                <p>
                                    <strong>Formula:</strong>
                                    <code>0.1579 x (PDW) + 0.0496 x ASL</code> + adjustment<br>
                                    Where:
                                    <ul>
                                        <li><strong>PDW</strong> = Percentage of Difficult Words</li>
                                        <li>If PDW > 5%, add 3.636 to the final score</li>
                                    </ul>
                                </p>
                                <p>
                                    The result corresponds to a grade level. Texts with fewer difficult words score lower (easier to read).
                                </p>

                                <h3>4. SMOG Index (Simple Measure of Gobbledygook)</h3>
                                <p>
                                    The SMOG Index estimates the years of education a person needs to understand a piece of writing.
                                    It focuses on the number of polysyllabic words (words with three or more syllables).
                                </p>
                                <p>
                                    <strong>Formula:</strong>
                                    <code>1.0430 x √(number of polysyllabic words x (30 / number of sentences)) + 3.1291</code>
                                </p>
                                <p>
                                    It is often used in healthcare and public communication to ensure materials are accessible.
                                </p>
                            </div>
                        </details>

                    """)
                with gr.Row():
                    readability_feedback = gr.Markdown(label="Frequencies feedback", line_breaks=True)

                with gr.Row():
                    gr.Markdown("<br><br>")
                with gr.Row():
                    gr.Markdown("## 🗣️ Acoustic metrics")
                with gr.Row():
                    gr.Markdown("<br>")
                with gr.Row():
                    gr.Markdown("### Root Mean Square (RMS)")
                with gr.Row():
                    gr.HTML("""
                    <details>
                        <summary>Root Mean Square Documentation</summary>
                        <div>
                            <h3>Definition</h3>
                            <p>
                                To measure intensity, we will use a metric known as the Root Mean Square (RMS).
                                This metric calculates the average energy level of an acoustic signal and is
                                considered one of the most accurate ways to quantify sound intensity. RMS works
                                by squaring all the amplitude values of the signal (which removes negative values),
                                averaging them, and then taking the square root of the result. This process provides
                                a single representative value that reflects the signal's overall power, making it
                                especially useful for analyzing complex audio signals where simple averaging would be misleading.
                            </p>
                        </div>
                    </details>
                    """)

                with gr.Row():
                    rms_plot = gr.LinePlot(
                        x="x",
                        y="y",
                        title="RMS Energy Over Time",
                        color="name",
                        x_title="Time (s)",
                        y_title="RMS Energy",
                        label="RMS Energy Plot",
                        overlay=True,
                    )
                with gr.Row():
                    rms_feedback = gr.Markdown(label="Intensity (RMS) feedback", line_breaks=True)

                with gr.Row():
                    gr.Markdown("<br>")

                with gr.Row():
                    gr.Markdown("### Signal-to-Noise Ratio (SNR)")
                with gr.Row():
                    gr.HTML("""
                    <details>
                        <summary>Signal-to-Noise Ratio Documentation</summary>
                        <div>
                            <h3>Definition</h3>
                            <p>
                                Signal-to-Noise Ratio (SNR) is a measure that compares the level of a
                                desired signal to the level of background noise. It is typically expressed
                                in decibels (dB). A higher SNR indicates a cleaner, clearer signal, while a
                                lower SNR means the signal is harder to distinguish from the noise.
                            </p>
                        </div>
                    </details>
                    """)
                with gr.Row():
                    snr_plot = gr.LinePlot(
                        x="x",
                        y="y",
                        title="SNR Over Time",
                        color="name",
                        x_title="Time (s)",
                        y_title="SNR",
                        label="SNR Plot",
                        overlay=True,
                    )
                with gr.Row():
                    snr_feedback = gr.Markdown(label="Noise (SNR) feedback", line_breaks=True)

                with gr.Row():
                    gr.Markdown("<br><br>")
                with gr.Row():
                    gr.Markdown("## 🤖 LLM Feedback")
                with gr.Row():
                    introduction_feedback = gr.Markdown(label="Introduction feedback")
                with gr.Row():
                    background_feedback = gr.Markdown(label="Background feedback")
                with gr.Row():
                    innovation_feedback = gr.Markdown(label="Innovation feedback")
                with gr.Row():
                    description_feedback = gr.Markdown(label="Description feedback")
                with gr.Row():
                    organization_feedback = gr.Markdown(label="Organization feedback")
                with gr.Row():
                    language_feedback = gr.Markdown(label="Language feedback")
                with gr.Row():
                    highlight_words = gr.Markdown(label="Highlight Words")
                with gr.Row():
                    topic_words = gr.Markdown(label="Topic and Related Words")

                with gr.Row():
                    reset_btn = gr.Button("Clear results")

            audio_box.change(fn=show_group, inputs=audio_box, outputs=base_options_group)
            base_options.change(fn=handle_base_checkbox, inputs=base_options, outputs=[llm_options_group, audio_submit_group])
            activate_llm.change(fn=handle_llm_checkbox, inputs=activate_llm, outputs=[options_group, submit_group])
            sections_checkbox.change(fn=show_submit, inputs=sections_checkbox, outputs=submit_group)
            general_sections_checkbox.change(fn=show_submit, inputs=general_sections_checkbox, outputs=submit_group)
            transcription.change(fn=show_group, inputs=transcription, outputs=results_group)
            transcription.change(fn=hide_group, inputs=transcription, outputs=loading_group)
            audio_feedback_status.change(fn=show_group, inputs=audio_feedback_status, outputs=audio_results_group)
            audio_feedback_status.change(fn=hide_group, inputs=audio_feedback_status, outputs=loading_group)

            submit_btn.click(fn=show_group, inputs=[], outputs=loading_group)
            exec_event = submit_btn.click(
                fn=function_ptr,
                inputs=[audio_box, base_options, sections_checkbox, general_sections_checkbox],
                outputs=[
                    transcription,
                    words_distribution_plot,
                    words_distribution_feedback,
                    lexical_richness_feedback,
                    readability_feedback,
                    rms_plot,
                    rms_feedback,
                    snr_plot,
                    snr_feedback,
                    introduction_feedback,
                    background_feedback,
                    innovation_feedback,
                    description_feedback,
                    organization_feedback,
                    language_feedback,
                    highlight_words,
                    topic_words,
                ],
            )

            audio_submit_btn.click(fn=show_group, inputs=[], outputs=loading_group)
            audio_exec_event = audio_submit_btn.click(
                fn=function_ptr,
                inputs=[audio_box, base_options, sections_checkbox, general_sections_checkbox],
                outputs=[
                    audio_feedback,
                    audio_feedback_status,
                ],
            )

            stop_btn.click(fn=None, cancels=[exec_event, audio_exec_event])
            stop_btn.click(fn=hide_group, inputs=[], outputs=loading_group)

            reset_btn.click(
                fn=reset,
                inputs=[],
                outputs=[
                    results_group,
                ],
            )

            audio_reset_btn.click(
                fn=reset,
                inputs=[],
                outputs=[
                    audio_results_group,
                ],
            )
