import whisper

model = whisper.load_model("medium")

# load audio and pad/trim it to fit 30seconds
audio = whisper.load_audio("audio-test-2.webm")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device ad the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)