import librosa
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from logmmse import logmmse_from_file
import librosa.display

# audio_path = 'audiofile.wav'
audio_path = 'noise_removed_audio.wav'


# Load audio file
y, sr = librosa.load(audio_path, sr=None)

# Plot the audio waveform
plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr)
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.title("Audio Waveform")
plt.show()

# Noise reduction using logmmse
out_file_name = "noise_removed_audio.wav"
out = logmmse_from_file(audio_path)  # Apply noise reduction to input audio

# Save the noise-reduced audio
write(out_file_name, sr, out)

