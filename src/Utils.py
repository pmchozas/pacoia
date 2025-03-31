from typing import Optional, Union
from dotenv import load_dotenv
from huggingface_hub import login
import os
import torch

class Utils:

    @staticmethod
    def login_hf() -> None:
        load_dotenv()
        HF_TOKEN = os.getenv("HF_TOKEN")
        login(token=HF_TOKEN)


    @staticmethod
    def default_config() -> list[Union[str, torch.dtype]]:
        model_id: Optional[str] = None
        device: Optional[str] = None
        torch_dtype: Optional[torch.dtype] = None

        if torch.cuda.is_available():
            device = "cuda:0"
            torch_dtype = torch.float16
            model_id = "nyrahealth/CrisperWhisper"
        else:
            device = "cpu"
            torch_dtype = torch.float32
            model_id = "openai/whisper-small"

        return [model_id, device, torch_dtype]