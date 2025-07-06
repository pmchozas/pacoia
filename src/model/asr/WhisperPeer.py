from openai import OpenAI


class WhisperPeer:
    def __init__(self) -> None:
        self.client = OpenAI()

    def transcribe(self, audio_path: str) -> dict:
        with open(audio_path, "rb") as audio_file:
            text = self.client.audio.transcriptions.create(
                model="gpt-4o-mini-transcribe",
                file=audio_file,
                response_format="text",
            )
            return {"text": text}
