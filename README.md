# PACOIA project
![CI](https://github.com/pmchozas/pacoia/actions/workflows/CI.yml/badge.svg)

Plataforma Automatizada para la evaluación de Comunicación Oral en Inglés Académico

## Requirements
- [Python 3.12](https://www.python.org/)
  
## Installation

### Using Virtualenv
```bash
python3 -m venv <myenvpath>
source <myenvpath>/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python3 -m src.main --model <asr_model_name>
```

Currently the only supported ASR models are `CrisperWhisper` and `Whisper`

> [!NOTE]  
> In order to use CrisperWhisper you must generate a token [here](https://huggingface.co/nyrahealth/CrisperWhisper) and assign it to the environmental variable `HF_TOKEN`, where the token will be read by the application

Then the application will be deployed in `http://127.0.0.1:7860`