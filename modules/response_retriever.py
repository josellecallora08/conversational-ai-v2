import os

class ResponseRetriever:
    def __init__(self, response_dir="responses"):
        """Initializes the class with the directory where responses are stored."""
        self.response_dir = response_dir
        self.intent_to_audio = {
            "greeting": "greetings_default_1_Voice 1_fil-PH.wav",
            "farewell": "farewell.wav",
            "order_status": "order_status.wav",
            "support": "support.wav",
            "debt_collection": "debt_collection_intro.wav",
            "debt_acknowledgment": "debt_acknowledgment.wav",
            "payment_arrangement": "payment_arrangement.wav",
            "dispute": "debt_dispute.wav",
            "financial_difficulty": "financial_difficulty.wav",
            "payment_confirmation": "payment_confirmation.wav",
            "negotiation": "negotiation.wav"
        }

    def get_audio_response(self, intent):
        """Retrieves the appropriate audio response file based on the detected intent."""
        if intent in self.intent_to_audio:
            audio_path = os.path.join(self.response_dir, self.intent_to_audio[intent])
            if os.path.exists(audio_path):
                return audio_path
            else:
                print(f"Warning: Audio file for intent '{intent}' not found.")
                return None
        else:
            print(f"Unknown intent: '{intent}'. No response available.")
            return None

# Example Usage
if __name__ == "__main__":
    retriever = ResponseRetriever()
    intent = "payment_arrangement"
    audio_file = retriever.get_audio_response(intent)
    if audio_file:
        print(f"Playing: {audio_file}")
