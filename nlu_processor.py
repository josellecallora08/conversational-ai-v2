class NLUProcessor:
    def __init__(self):
        """Define a simple mapping of keywords to intents, including a structured flow for debt collection."""
        self.intent_map = {
            "greeting": ["hello", "hi", "good morning", "good evening"],
            "farewell": ["bye", "goodbye", "see you", "farewell"],
            "order_status": ["order", "tracking", "shipment", "delivered"],
            "support": ["help", "issue", "problem", "support"],
            "debt_collection": [
                "payment due", "outstanding balance", "overdue", "late payment",
                "debt", "collection", "repayment", "due amount", "settlement"
            ],
            "debt_acknowledgment": ["I understand", "I acknowledge", "Yes, I know about my debt"],
            "payment_arrangement": ["Can I set up a payment plan?", "installments", "payment schedule"],
            "dispute": ["I don’t owe this", "There is a mistake", "This is incorrect"],
            "financial_difficulty": ["I can't pay right now", "I'm struggling financially", "hardship"],
            "payment_confirmation": ["I have made the payment", "I just paid", "Payment sent"],
            "negotiation": ["Can we lower the amount?", "Can we settle for less?", "discount", "waive fees"]
        }

    def detect_intent(self, text):
        """Detects intent based on keyword matching."""
        text = text.lower()

        for intent, keywords in self.intent_map.items():
            if any(keyword in text for keyword in keywords):
                return intent

        return "unknown"

# Example Usage
if __name__ == "__main__":
    nlu = NLUProcessor()
    test_text = "Can I set up a payment plan for my overdue balance?"
    detected_intent = nlu.detect_intent(test_text)
    print(f"Detected Intent: {detected_intent}")