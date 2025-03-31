import typing
import gradio as gr
from matplotlib import pyplot as plt

class CrisperWhisperInterface:

    def __init__(self, function_ptr: typing.Callable[[str], list[typing.Union[str, plt.Figure]]]) -> None:
        title="Speech to Text App"
        css="footer{display:none !important}"

        with gr.Blocks(title=title, css=css) as iface:
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
                pass
            with gr.Row():
                speeking_rate_feedback = gr.Textbox(label="Speeking rate feedback")
                pass

            with gr.Row():
                rms_plot = gr.Plot(label="RMS plot")
            with gr.Row():
                rms_feedback = gr.Textbox(label="RMS feedback")

            with gr.Row():
                snr_plot = gr.Plot(label="SNR plot")
            with gr.Row():
                snr_feedback = gr.Textbox(label="SNR feedback")

            with gr.Row():
                llm_feedback = gr.Textbox(label="LLM feedback")

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
                    llm_feedback
                ]
            )