import json
import re
import os
from typing import List, Dict
from modules.audio_player import AudioPlayer

class NLURecognizer:
    def __init__(self, play_audio_on_match: bool = False, audio_base_path: str = "responses/") -> None:
        self.intent_patterns = self._load_intent()
        self.play_audio_on_match = play_audio_on_match
        self.audio_base_path = audio_base_path
        self.player = AudioPlayer() if play_audio_on_match else None

    def split_patterns(self, pattern: str) -> List[str]:
        return pattern.split('\n')

    def match_pattern(self, text: str, pattern: str) -> bool:
        return bool(re.search(pattern, text, re.IGNORECASE))

    def recognize_intent(self, text: str) -> Dict[str, Dict[str, str]]:
        matched_intents = {}
        for intent in self.intent_patterns:
            patterns = self.split_patterns(intent['pattern'])
            for pattern in patterns:
                if self.match_pattern(text, pattern):
                    matched_intents[intent['name']] = {
                        "pattern": pattern,
                        "audio": intent.get("audio")
                    }

                    if self.play_audio_on_match and intent.get("audio"):
                        self._play_audio_file(intent["audio"])
                    break
        return matched_intents

    def _load_intent(self, path: str = "config.json") -> List[Dict[str, str]]:
        with open(path) as f:
            intent = json.load(f)
        return intent['data']['intent']

    def _play_audio_file(self, filename: str):
        file_path = os.path.join(self.audio_base_path, filename)
        if os.path.exists(file_path):
            print(f"[NLU] Playing audio file: {filename}")
            self.player.play_audio(file_path)
        else:
            print(f"[NLU] Audio file not found: {filename}")
