import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Starting record...")
    recording = sounddevice.rec((seconds*44100), 44100, channels=1)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Recording finished!")

voice_recorder(10, "record.wav")