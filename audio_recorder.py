import pyaudio
import wave
import numpy as np

class AudioRecorder:
    def __init__(self, output_file="temp_audio.wav", threshold=500, chunk=1024, rate=44100, channels=1):
        self.output_file = output_file
        self.threshold = threshold  # Silence threshold
        self.chunk = chunk
        self.rate = rate
        self.channels = channels
        self.audio = pyaudio.PyAudio()

    def is_silent(self, snd_data):
        """Checks if the audio data is below the silence threshold."""
        return np.max(np.abs(snd_data)) < self.threshold

    def record(self):
        """Records audio and stops when silence is detected."""
        stream = self.audio.open(format=pyaudio.paInt16,
                                 channels=self.channels,
                                 rate=self.rate,
                                 input=True,
                                 frames_per_buffer=self.chunk)

        print("Recording... Speak now.")
        frames = []
        silent_chunks = 0
        max_silent_chunks = 20  # Number of silent chunks before stopping

        while True:
            data = stream.read(self.chunk)
            audio_data = np.frombuffer(data, dtype=np.int16)
            frames.append(data)

            if self.is_silent(audio_data):
                silent_chunks += 1
                if silent_chunks > max_silent_chunks:
                    break
            else:
                silent_chunks = 0

        print("Recording stopped.")
        stream.stop_stream()
        stream.close()

        self.save_audio(frames)

    def save_audio(self, frames):
        """Saves recorded audio as a WAV file."""
        wf = wave.open(self.output_file, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        print(f"Audio saved as {self.output_file}")

    def close(self):
        """Closes PyAudio instance."""
        self.audio.terminate()

# Example Usage
if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.record()
    recorder.close()
