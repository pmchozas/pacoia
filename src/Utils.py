from os import getenv

from dotenv import load_dotenv
from huggingface_hub import login
from torch import cuda, dtype, torch


def login_hf() -> None:
    load_dotenv()
    HF_TOKEN = getenv("HF_TOKEN")
    login(token=HF_TOKEN)


def default_device() -> str:
    return "cuda:0" if cuda.is_available() else "cpu"


def default_dtype() -> dtype:
    return torch.float16
