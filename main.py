from modules.audio_recorder import AudioRecorder
from modules.speech_to_text import SpeechToText
from modules.nlu_processor import NLUProcessor
from modules.response_retriever import ResponseRetriever
from modules.audio_player import AudioPlayer
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
        """Handles the full conversation flow in a loop until a closing intent is detected."""
        print("AI: Starting the call...")

        while True:  # Keep the conversation running
            # Step 1: Record user speech
            self.recorder.record()

            # Step 2: Transcribe the recorded speech
            transcription = self.speech_to_text.transcribe()
            if not transcription:
                print("AI: Unable to understand. Please try again.")
                continue  # Ask the user to speak again

            print(f"You said: {transcription}")

            # Step 3: Analyze intent using NLU
            intent = self.nlu.detect_intent(transcription)
            print(f"AI: Detected Intent -> {intent}")

            # Step 4: Retrieve pre-recorded audio response
            audio_response = self.retriever.get_audio_response(intent)
            if audio_response:
                print("AI: Playing response...")
                self.player.play_audio(audio_response)

            # Step 5: Check for closing intents
            if intent in ["call_end", "debt_settled", "goodbye"]:
                print("AI: Thank you for your time. Goodbye!")
                break  # Exit the loop when the conversation is finished

    # Example Usage
if __name__ == "__main__":
    API_KEY = "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"  # Replace with your actual Groq API key
    ai = ConversationalAI(api_key=API_KEY)
    ai.start_conversation()
