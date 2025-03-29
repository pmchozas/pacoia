import gradio as gr

class Interface:

    def __init__(self, function_ptr):
        title="Speech to Text App"
        css="footer{display:none !important}"

        with gr.Blocks(title=title, css=css) as self.blocks:
            with gr.Row():
                gr.Markdown("# Speech to Text App")
            with gr.Row():
                audio_box = gr.Audio(type="filepath")
                transcription = gr.Textbox(label="Transcription")
            with gr.Row():
                submit_btn = gr.Button("Submit", variant="primary")
            with gr.Row():
                rms_plot = gr.Plot(label="RMS plot")
                snr_plot = gr.Plot(label="SNR plot")
            with gr.Row():
                rms_feedback = gr.Textbox(label="RMS feedback")
                snr_feedback = gr.Textbox(label="SNR feedback")
            with gr.Row():
                llm_feedback = gr.Textbox(label="LLM feedback")

            submit_btn.click(
                fn=function_ptr,
                inputs=audio_box,
                outputs=[
                    transcription,
                    rms_plot,
                    snr_plot,
                    rms_feedback,
                    snr_feedback,
                    llm_feedback
                ]
            )