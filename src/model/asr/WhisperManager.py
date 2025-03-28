from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch

class WhisperManager:

  def __init__(self, model_id, torch_dtype, device):
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
      model_id, 
      torch_dtype=torch_dtype, 
      low_cpu_mem_usage=True, 
      use_safetensors=True,
    )

    model.to(device)
    model = torch.compile(model)
    processor = AutoProcessor.from_pretrained(model_id)

    self.pipeline = pipeline(
      "automatic-speech-recognition",
      model=model,
      tokenizer=processor.tokenizer,
      feature_extractor=processor.feature_extractor,
      torch_dtype=torch_dtype,
      device=device,
      return_timestamps=True,
    )
  

  def transcribe(self, audio_path: str) -> str:
    return self.pipeline(audio_path)