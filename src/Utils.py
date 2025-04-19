from typing import Optional, Union
from dotenv import load_dotenv
from huggingface_hub import login
from os import getenv
from torch import dtype, torch, cuda

def login_hf() -> None:
    load_dotenv()
    HF_TOKEN = getenv("HF_TOKEN")
    login(token=HF_TOKEN)


def default_config() -> list[Union[str, dtype]]:
    device: Optional[str] = None
    torch_dtype: Optional[dtype] = None

    if cuda.is_available():
        device = "cuda:0"
        torch_dtype = torch.float16
    else:
        device = "cpu"
        torch_dtype = torch.float16

    return [device, torch_dtype]