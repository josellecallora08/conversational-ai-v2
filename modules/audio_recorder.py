import pyaudio
import wave

class AudioRecorder:
    def __init__(self, filename="temp.wav", duration=5):
        """Initializes the recorder with default settings."""
        self.filename = filename
        self.duration = duration
        self.rate = 44100
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1

    def record(self):
        """Records audio for the set duration and saves it to a file."""
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.format, channels=self.channels,
                            rate=self.rate, input=True,
                            frames_per_buffer=self.chunk)

        print("Recording... Speak now.")
        frames = []

        for _ in range(0, int(self.rate / self.chunk * self.duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        print("Recording stopped.")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        # Save the recorded audio
        with wave.open(self.filename, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(audio.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b"".join(frames))

        print(f"Audio recorded and saved to {self.filename}")

# Example Usage
if __name__ == "__main__":
    recorder = AudioRecorder(duration=5)
    recorder.record()
