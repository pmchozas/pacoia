from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch

class CrisperWhisperManager:

    def __init__(self, torch_dtype: torch.dtype, device: str) -> None:
        self.model_id = "nyrahealth/CrisperWhisper"
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            self.model_id, 
            torch_dtype=torch_dtype, 
            low_cpu_mem_usage=True, 
            use_safetensors=True,
        )

        model.to(device)
        model = torch.compile(model)
        processor = AutoProcessor.from_pretrained(self.model_id)

        self.pipeline = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            torch_dtype=torch_dtype,
            device=device,
            return_timestamps="word"
        )
    

    def transcribe(self, audio_path: str) -> dict:
        return self.pipeline(audio_path)