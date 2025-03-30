from audio_recorder import AudioRecorder
from speech_to_text import SpeechToText
from nlu_processor import NLUProcessor
from response_retriever import ResponseRetriever
from audio_player import AudioPlayer
import os

class ConversationalAI:
    def __init__(self, api_key):
        """Initializes the conversational AI system."""
        self.recorder = AudioRecorder()
        self.speech_to_text = SpeechToText(api_key=api_key)
        self.nlu = NLUProcessor()
        self.retriever = ResponseRetriever()
        self.player = AudioPlayer()

    def start_conversation(self):
        """Handles the full conversation flow."""
        print("AI: Starting the call...")

        # Step 1: Record user speech
        self.recorder.record()

        # Step 2: Transcribe the recorded speech
        transcription = self.speech_to_text.transcribe()
        if not transcription:
            print("AI: Unable to understand. Please try again.")
            return

        # Step 3: Analyze intent using NLU
        intent = self.nlu.detect_intent(transcription)
        print(f"AI: Detected Intent -> {intent}")

        # Step 4: Retrieve pre-recorded audio response
        audio_response = self.retriever.get_audio_response(intent)
        if audio_response:
            print("AI: Playing response...")
            self.player.play_audio(audio_response)
        else:
            print("AI: No appropriate response found.")

# Example Usage
if __name__ == "__main__":
    API_KEY = "your_groq_api_key"  # Replace with your actual Groq API key
    ai = ConversationalAI(api_key=API_KEY)
    ai.start_conversation()
