import typing

import gradio as gr
from matplotlib import pyplot as plt


class Interface:
    def __init__(self, function_ptr: typing.Callable[[str], list[typing.Union[str, plt.Figure]]]) -> None:
        title = "Speech to Text App"
        css = "footer{display:none !important}"

        with gr.Blocks(title=title, css=css) as self.blocks:
            with gr.Row():
                gr.Markdown("# Speech to Text App")
            with gr.Row():
                audio_box = gr.Audio(type="filepath")
                transcription = gr.Textbox(label="Transcription")
            with gr.Row():
                submit_btn = gr.Button("Submit", variant="primary")

            with gr.Row():
                frequencies_plot = gr.Plot(label="Frequencies")
            with gr.Row():
                frequencies_feedback = gr.Textbox(label="Frequencies feedback")

            with gr.Row():
                speeking_rate_plot = gr.Plot(label="Speeking rate")
            with gr.Row():
                speeking_rate_feedback = gr.Textbox(label="Speeking rate feedback")

            with gr.Row():
                rms_plot = gr.Plot(label="RMS plot")
            with gr.Row():
                rms_feedback = gr.Textbox(label="RMS feedback")

            with gr.Row():
                snr_plot = gr.Plot(label="SNR plot")
            with gr.Row():
                snr_feedback = gr.Textbox(label="SNR feedback")

            with gr.Row():
                gr.Markdown("## Introduction Feedback")
            with gr.Row():
                introduction_feedback = gr.Markdown(label="Introduction feedback")

            with gr.Row():
                gr.Markdown("## Background Feedback")
            with gr.Row():
                background_feedback = gr.Markdown(label="Background feedback")

            with gr.Row():
                gr.Markdown("## Innovation Feedback")
            with gr.Row():
                innovation_feedback = gr.Markdown(label="Innovation feedback")

            with gr.Row():
                gr.Markdown("## Description Feedback")
            with gr.Row():
                description_feedback = gr.Markdown(label="Description feedback")

            with gr.Row():
                gr.Markdown("## Organization Feedback")
            with gr.Row():
                organization_feedback = gr.Markdown(label="Organization feedback")

            with gr.Row():
                gr.Markdown("## Language Feedback")
            with gr.Row():
                language_feedback = gr.Markdown(label="Language feedback")

            submit_btn.click(
                fn=function_ptr,
                inputs=audio_box,
                outputs=[
                    transcription,
                    frequencies_plot,
                    frequencies_feedback,
                    speeking_rate_plot,
                    speeking_rate_feedback,
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
                ]
            )
