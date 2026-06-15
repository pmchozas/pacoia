# PACOIA project
![CI](https://github.com/pmchozas/pacoia/actions/workflows/CI.yml/badge.svg)

PACOIA: A GenAI-Driven Framework for the Automated Evaluation of Oral Presentations in EAP

PACOIA is a Generative AI (GenAI)-driven framework for the automated evaluation of academic oral presentations. The system integrates multimodal analysis by combining audio-based metrics (e.g. speech rate, audibility, and clarity) with transcription-based evaluation, including metrics such as lexical richness and rubric-aligned discourse assessment. The platform adopts a dual-model architecture, using Automatic Speech Recognition (ASR) for transcription and a Large Language Models (LLM) to generate structured, rubric-based feedback aligned with EAP pedagogical criteria.


## Requirements
- [Python 3.12](https://www.python.org/)
- [Astral uv](https://docs.astral.sh/uv/)
- [FFmpeg](https://www.ffmpeg.org/)
  
## Installation

### Using Virtualenv
```bash
uv sync --locked --all-extras --dev
```

## Usage
```bash
uv run -m src.main
```

Currently the only supported ASR models are `CrisperWhisper` and `Whisper`

To disable the local execution of the ASR model, and enable the usage of the OpenAI API you must assign your OpenAI key to the environmental variable `OPENAI_API_KEY` and put the `config/config.json` `local` option to `false`.

> [!NOTE]  
> In order to use CrisperWhisper you must generate a token [here](https://huggingface.co/nyrahealth/CrisperWhisper) and assign it to the environmental variable `HF_TOKEN`, where the token will be read by the application

Then the application will be deployed in `http://127.0.0.1:7860`

## Development

### ASR Classes
- `CrisperWhisperManager.py`: Local CrisperWhisper Model
- `WhisperManager.py`: Local Whisper Model
- `WhisperPeer.py`: Remote Whisper Model

### LLM Class
- `LLMPeer.py`: Remote LLM Model

### Audio Libraries
- `AudioAnalyzer.py`: Analyzes audio metrics
- `AudioConstant.py`: Constants used for audio feedback
- `AudioDataPlotter.py`: Plots audio metrics
- `AudioFeedback.py`: Creates audio feedback

### Text Libraries
- `LexicalRichnessConstants.py`: Lexical richness constants
- `ReadabilityConstants.py`: Readability constants
- `TextAnalyzer.py`: Analyzes text metrics (Readability and LexicalRichness)
- `TextDataPlotter.py`: Plots text metrics
- `TextFeedback.py`: Creates text feedback

## Utils
- `Utils.py`: Contains utilities

## Controller
- `Controller.py`: Middle layer between the model and the view

## View
- `Interface.py`: CrisperWhisper Gradio Interface
- `WhisperInterface.py`: Whisper Gradio Interface

> [!IMPORTANT]  
> CrisperWhisper capacity to calculate word-level timestamps enable us to calculate speech's speed in WPM

## Main
- `main.py`: Handles config and starts the service

> [!NOTE]  
> Configuration is saved in `config` folder

## To Do
- Improve UI (view)
- Unit tests
- Refactor
