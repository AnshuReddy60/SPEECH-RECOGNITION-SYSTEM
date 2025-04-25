import streamlit as st
import torch
import librosa
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import io

# ✅ This must be the first Streamlit command
st.set_page_config(page_title="Speech-to-Text", layout="centered")

# Load the pre-trained model and processor
@st.cache_resource
def load_model():
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    return processor, model

processor, model = load_model()

# Streamlit interface
st.title("🎙️ Speech-to-Text Transcription Tool")
st.write("### Upload your own audio file or use the default one.")

# Upload audio file
audio_file = st.file_uploader("Upload an Audio File (.wav)", type=["wav"])

# If no file is uploaded, use a default sample audio file
if audio_file is None:
    st.write("No file uploaded. Using the default sample file.")
    audio_file = open("audio.wav", "rb")  # Make sure "audio.wav" exists

# Read audio file using BytesIO
audio_bytes = audio_file.read()

# Load the audio data
audio, rate = librosa.load(io.BytesIO(audio_bytes), sr=16000)

# Transcription
input_values = processor(audio, return_tensors="pt").input_values
with torch.no_grad():
    logits = model(input_values).logits
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.decode(predicted_ids[0])

# Output
st.write("### Transcription:")
st.write(transcription)

# Download button
st.download_button(
    label="Download Transcription",
    data=transcription,
    file_name="transcription.txt",
    mime="text/plain"
)
