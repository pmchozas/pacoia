import gradio as gr
from dotenv import load_dotenv
from model.SpeechData import SpeechData
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from pydub import AudioSegment
from huggingface_hub import login
import os

def login_hf():
  load_dotenv()
  HF_TOKEN = os.getenv("HF_TOKEN")
  login(token=HF_TOKEN)

def set_pipe():
  model_id: str = None 
  device: str = None
  if torch.cuda.is_available():
    device = "cuda:0"
    torch_dtype = torch.float16
    model_id = "nyrahealth/CrisperWhisper"
  else:
    device = "cpu"
    torch_dtype = torch.float32
    model_id = "openai/whisper-small"

  model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, 
    torch_dtype=torch_dtype, 
    low_cpu_mem_usage=True, 
    use_safetensors=True,
  )

  model.to(device)
  model = torch.compile(model)
  processor = AutoProcessor.from_pretrained(model_id)

  global pipe
  pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
    return_timestamps=True,
  )

def split_audio(audio_path: str, chunk_length_ms: int = 90000) -> list:
  audio = AudioSegment.from_file(audio_path)
  chunks = [audio[i : i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
  return chunks

def transcribe(audio_path: str) -> str:
  return pipe(audio_path)

def generate_outputs(audio_path: str) -> list:
  transcription = transcribe(audio_path)
  sd = SpeechData(transcription, audio_path)
  
  output = list()
  output.append(sd.text)
  output.append(sd.get_rms_plot())
  output.append(sd.get_snr_plot())
  output.append(sd.get_rms_feedback())
  output.append(sd.get_snr_feedback())

  output.append("Here will go LLM feedback")

  return output

def create_interface() -> gr.Blocks:
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
      rms_plot = gr.Plot(label="RMS plot")
      snr_plot = gr.Plot(label="SNR plot")
    with gr.Row():
      rms_feedback = gr.Textbox(label="RMS feedback")
      snr_feedback = gr.Textbox(label="SNR feedback")
    with gr.Row():
      llm_feedback = gr.Textbox(label="LLM feedback")

    submit_btn.click(
      fn=generate_outputs,
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
  
  return iface

def main():
  login_hf()
  set_pipe()
  create_interface().launch(debug=True)

if __name__ == "__main__":
    main()