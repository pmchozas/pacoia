import requests
from src.model.llm.prompts import background, description, innovation, \
    introduction, language, organization, punctuation

class LLMPeer:
    def __init__(self, endpoint: str = "http://localhost:11434/api/generate",
                 model_name: str ="qwen2.5:7b-instruct") -> None:
        
        self.endpoint = endpoint
        self.model_name = model_name
    

    def query_llm(self, prompt: str) -> str:
        url = "http://localhost:11434/api/generate"
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "No response received")
            else:
                return f"Error: {response.status_code}, {response.text}"
        except Exception as e:
            return f"An error occurred: {e}"
        

    def get_punctuated_transcription(self, transcription: str) -> str:
        return self.query_llm(punctuation.prompt.format(transcription))
    

    def get_background_evaluation(self, transcription: str) -> str:
        return self.query_llm(background.prompt.format(transcription))


    def get_description_evaluation(self, transcription: str) -> str:
        return self.query_llm(description.prompt.format(transcription))


    def get_innovation_evaluation(self, transcription: str) -> str:
        return self.query_llm(innovation.prompt.format(transcription))
    

    def get_introduction_evaluation(self, transcription: str) -> str:
        return self.query_llm(introduction.prompt.format(transcription))
    

    def get_language_evaluation(self, transcription: str) -> str:
        return self.query_llm(language.prompt.format(transcription))
    

    def get_organization_evaluation(self, transcription: str) -> str:
        return self.query_llm(organization.prompt.format(transcription))
    