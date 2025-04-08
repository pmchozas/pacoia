# PACOIA project
![StaticCheck](https://github.com/pmchozas/pacoia/actions/workflows/TypeChecking.yml/badge.svg)
![Tests](https://github.com/pmchozas/pacoia/actions/workflows/Tests.yml/badge.svg)

Plataforma Automatizada para la evaluación de Comunicación Oral en Inglés Académico

## Requirements
- [Python 3.13.1](https://www.python.org/)
- [Virtualenv installed](https://virtualenv.pypa.io/en/latest/)
  
## Installation

### Using Virtualenv
```bash
python3 -m venv <myenvpath>
source <myenvpath>/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python3 main.py --model <asr_model_name>
```
> [!NOTE]  
> Currently the only supported ASR models are `CrisperWhisper` and `Whisper`

Then the application will be deployed in `http://127.0.0.1:7860`