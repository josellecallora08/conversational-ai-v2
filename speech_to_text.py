import requests
import os

class SpeechToText:
    def __init__(self, api_key, model="whisper-turbo", file_path="temp_audio.wav"):
        self.api_key = api_key
        self.model = model
        self.file_path = file_path
        self.api_url = "https://api.groq.com/v1/audio/transcriptions"

    def transcribe(self):
        """Transcribes the audio file using Whisper in Groq API."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Audio file '{self.file_path}' not found.")

        with open(self.file_path, "rb") as audio_file:
            response = requests.post(
                self.api_url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                files={"file": audio_file},
                data={"model": self.model}
            )

        if response.status_code == 200:
            transcription = response.json().get("text", "")
            print(f"Transcription: {transcription}")
            return transcription
        else:
            print(f"Error: {response.json()}")
            return None

# Example Usage
if __name__ == "__main__":
    API_KEY = "your_groq_api_key"  # Replace with your actual API key
    stt = SpeechToText(api_key=API_KEY)
    transcription = stt.transcribe()
