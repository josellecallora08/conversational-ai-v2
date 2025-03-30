from pydub import AudioSegment
from pydub.playback import play
import os

class AudioPlayer:
    def __init__(self):
        """Initializes the audio player."""
        pass

    def play_audio(self, file_path):
        """Plays the given audio file if it exists."""
        if os.path.exists(file_path):
            audio = AudioSegment.from_file(file_path)
            play(audio)
        else:
            print(f"Error: Audio file '{file_path}' not found.")

# Example Usage
if __name__ == "__main__":
    player = AudioPlayer()
    player.play_audio("responses/greeting.wav")  # Replace with an actual file path
