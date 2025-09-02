import base64

import requests  # type: ignore[import-untyped]
from openai import OpenAI

from src.model.llm.prompts import (
    background,
    description,
    highlight_words,
    innovation,
    introduction,
    language,
    organization,
    punctuation,
    topic_words,
)

OK_STATUS = 200
TIMEOUT_TIME = 200


class LLMPeer:
    def __init__(self, endpoint: str = "http://localhost:11434/api/generate",
                 model_name: str = "qwen2.5:7b-instruct") -> None:

        self.endpoint = endpoint
        self.model_name = model_name

    def query_llm(self, prompt: str) -> str:
        url = self.endpoint
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
        }

        try:
            response = requests.post(url, json=payload, timeout=TIMEOUT_TIME)
            if response.status_code == OK_STATUS:
                data = response.json()
                return data.get("response", "No response received")
            return f"Error: {response.status_code}, {response.text}"
        except requests.exceptions.Timeout:
            return "Error: Request timed out"
        except requests.exceptions.ConnectionError:
            return "Error: Connection error"
        except requests.exceptions.RequestException as e:
            return f"Request failed: {e}"

    def get_punctuated_transcription(self, transcription: str) -> str:
        return self.query_llm(punctuation.prompt.format(transcription))

    def get_background_evaluation(self, transcription: str) -> str:
        return f"## Background Feedback\n{self.query_llm(background.prompt.format(transcription))}"

    def get_description_evaluation(self, transcription: str) -> str:
        return f"## Description Feedback\n{self.query_llm(description.prompt.format(transcription))}"

    def get_innovation_evaluation(self, transcription: str) -> str:
        return f"## Innovation Feedback\n{self.query_llm(innovation.prompt.format(transcription))}"

    def get_introduction_evaluation(self, transcription: str) -> str:
        return f"## Introduction Feedback\n{self.query_llm(introduction.prompt.format(transcription))}"

    def get_language_evaluation(self, transcription: str) -> str:
        return f"## Language Feedback\n{self.query_llm(language.prompt.format(transcription))}"

    def get_organization_evaluation(self, transcription: str) -> str:
        return f"## Organization Feedback\n{self.query_llm(organization.prompt.format(transcription))}"

    def get_highlighted_words(self, transcription: str) -> str:
        return f"## Highlighted Words\n{self.query_llm(highlight_words.prompt.format(transcription))}"

    def get_topic_words(self, transcription: str) -> str:
        return f"## Topic and Related Words\n{self.query_llm(topic_words.prompt.format(transcription))}"

    @staticmethod
    def get_audio_based_feedback(audio_path: str) -> tuple[str, str]:
        try:
            client = OpenAI()
        except:
            return "You need a valid OpenAI API Key", "Fail"

        with open(audio_path, "rb") as audio_file:
            completion = client.chat.completions.create(
                model="gpt-4o-audio-preview",
                modalities=["text", "audio"],
                audio={"voice": "alloy", "format": "mp3"},
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": """
                                    You are a speech coach and language expert. Analyze the following speech and give the following insights:
                                    1. Grammar corrections and explanations.
                                    2. Feedback on pronunciation.
                                    3. Feedback on tone and emotional intensity—was it flat, overly intense, or appropriate?
                                    4. Suggestions for improving word choice, pacing, and delivery.
                                    5. Output everything in clear bullet points or markdown.""",
                            },
                            {
                                "type": "input_audio",
                                "input_audio": {
                                    "data": base64.b64encode(audio_file.read()).decode("utf-8"),
                                    "format": "mp3",
                                },
                            },
                        ],
                    },
                ],
            )
        if not completion.choices[0].message.audio:
            return "There was an error connecting to OpenAI Platform", "Fail"

        return str(completion.choices[0].message.audio.transcript), "OK"
