from modules.audio_recorder import AudioRecorder
from modules.speech_to_text import SpeechToText
from modules.nlu_recognizer import NLURecognizer
from modules.response_retriever import ResponseRetriever
from modules.audio_player import AudioPlayer

class ConversationalAI:
    def __init__(self, api_key):
        self.recorder = AudioRecorder()
        self.speech_to_text = SpeechToText(api_key=api_key)
        self.nlu = NLURecognizer(
            play_audio_on_match=True,  # 🔊 Automatically plays mapped audio
            audio_base_path="responses/"  # 📁 Path to your .wav files
        )
        self.retriever = ResponseRetriever()
        self.player = AudioPlayer()

    def start_conversation(self):
        print("AI: Starting the call...")

        while True:
            # Record user voice
            self.recorder.record()

            # Transcribe it
            transcription = self.speech_to_text.transcribe()
            if not transcription:
                print("AI: Unable to understand. Please try again.")
                continue

            print(f"You said: {transcription}")

            # Run NLU matching
            matched_intents = self.nlu.recognize_intent(transcription)
            if matched_intents:
                intent, pattern_info = next(iter(matched_intents.items()))
                print(f"AI: Detected Intent -> {intent} (matched: {pattern_info['pattern']})")

                # If audio was already played by NLURecognizer, you can skip this if needed
                # Otherwise, use your custom retriever fallback here:
                if not self.nlu.play_audio_on_match:
                    audio_response = self.retriever.get_audio_response(intent)
                    if audio_response:
                        print("AI: Playing fallback response...")
                        self.player.play_audio(audio_response)
            else:
                intent = None
                print("AI: No intent detected.")
                # Optional fallback: play default audio
                fallback_response = self.retriever.get_audio_response("default")
                if fallback_response:
                    self.player.play_audio(fallback_response)

            # Optional: yield response for logging/debugging
            r = type('Response', (object,), {'utterance': lambda: transcription, 'intent': intent})
            yield r

            # Exit condition
            if intent in ["call_end", "debt_settled", "goodbye"]:
                print("AI: Thank you for your time. Goodbye!")
                break

if __name__ == "__main__":
    API_KEY = "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"  # Replace with your actual key
    ai = ConversationalAI(api_key=API_KEY)
    for _ in ai.start_conversation():
        pass
