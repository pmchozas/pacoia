from typing import Callable, Union

import gradio as gr
from matplotlib import pyplot as plt


class WhisperInterface:
    def __init__(self, function_ptr: Callable[[str, list[str]], list[Union[str, plt.Figure]]]) -> None:
        title = "Speech to Text App"
        css = "footer{display:none !important}"

        with gr.Blocks(title=title, css=css) as self.blocks:
            with gr.Row():
                gr.Markdown("# Speech to Text App")
            with gr.Row():
                audio_box = gr.Audio(type="filepath")
                transcription = gr.Textbox(label="Transcription")
            with gr.Row():
                checkbox_group = gr.CheckboxGroup(
                    choices=[
                        "Introduction",
                        "Background",
                        "Innovation",
                        "Description",
                        "Organization",
                        "Language",
                    ],
                    label="Choose the parts to be graded",
                )
            with gr.Row():
                submit_btn = gr.Button("Submit", variant="primary")

            with gr.Tab("Frequencies"):
                with gr.Row():
                    frequencies_plot = gr.Plot(label="Frequencies")
                with gr.Row():
                    frequencies_feedback = gr.Textbox(label="Frequencies feedback")

            with gr.Tab("RMS"):
                with gr.Row():
                    rms_plot = gr.Plot(label="RMS plot")
                with gr.Row():
                    rms_feedback = gr.Textbox(label="RMS feedback")

            with gr.Tab("SNR"):
                with gr.Row():
                    snr_plot = gr.Plot(label="SNR plot")
                with gr.Row():
                    snr_feedback = gr.Textbox(label="SNR feedback")

            with gr.Tab("LLM Feedback"):
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

            submit_btn.click(
                fn=function_ptr,
                inputs=[audio_box, checkbox_group],
                outputs=[
                    transcription,
                    frequencies_plot,
                    frequencies_feedback,
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
                ],
            )
