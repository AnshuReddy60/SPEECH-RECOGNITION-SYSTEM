# SPEECH-RECOGNITION-SYSTEM

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: ANSHU VEERAMALLA

**INTERN ID**: CODF269

**DOMAIN**: AIML(ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE)

**DURATION**: 1 MONTH

**MENTOR**: NEELA SANTOSH

## DESCRIPTION

# Speech-to-Text Transcription Tool

This **Speech-to-Text Transcription Tool** is a web-based application developed using **Streamlit** and **Hugging Face's Wav2Vec2 model**, providing users with an easy way to transcribe speech from audio files into text. This tool is ideal for anyone who needs a fast and accurate transcription solution for their audio recordings, such as podcasts, meetings, lectures, and more.

### **Overview**

The core of this application leverages the **Wav2Vec2 model** from Facebook, a **pre-trained model** specifically designed for automatic speech recognition (ASR). The tool processes audio data, transcribes it into text, and provides users with a simple interface to either view or download the transcription. It uses **librosa** for audio preprocessing and **Torch** for inference.

### **Key Features**

- **Audio File Upload**: Users can upload their own audio files in the **.wav** format. If no file is uploaded, a default sample file is used for transcription.
  
- **Automatic Speech Recognition**: The tool uses **Wav2Vec2**, a powerful pre-trained model that can convert audio speech into text. Wav2Vec2 is highly accurate in transcribing speech, even from noisy audio sources.

- **Real-Time Transcription**: Once the audio is uploaded, the application processes the audio and generates a transcription almost instantly. Users can view the transcribed text directly on the interface.

- **Downloadable Transcription**: After transcription, the tool provides a download button so users can save the transcription as a **.txt** file for offline use, making it easy to store or share the results.

### **How It Works**

1. **Audio Upload**: Users can upload their own audio file in **.wav** format. If no file is uploaded, the tool automatically uses a default audio file for transcription. 
   
2. **Audio Processing**: The uploaded audio file is processed using **librosa**, which is a Python package for analyzing and manipulating audio. The audio file is loaded, resampled to 16 kHz (the model’s expected input), and converted into a format suitable for the Wav2Vec2 model.

3. **Model Inference**: The **Wav2Vec2Processor** and **Wav2Vec2ForCTC** model from Hugging Face are used to transcribe the audio. The **Wav2Vec2Processor** preprocesses the audio, while the **Wav2Vec2ForCTC** model performs the transcription. The model uses **Connectionist Temporal Classification (CTC)** loss to decode the speech into text.

4. **Transcription Output**: The resulting transcription is displayed directly in the app, giving users a clear and readable text representation of their audio.

5. **Download**: Users can download the transcription as a **.txt** file via a **download button**, which makes it easy to save the output for further use.

### **Technologies Used**

- **Streamlit**: A Python framework for building interactive web applications, making it easy to deploy the tool as a user-friendly application.

- **Wav2Vec2 (Hugging Face Transformers)**: A pre-trained model specifically designed for speech-to-text tasks. Wav2Vec2 performs exceptionally well in transcribing speech from raw audio data.

- **Librosa**: A Python package used for audio analysis. It helps in loading and preprocessing the audio file for the Wav2Vec2 model.

- **PyTorch**: A machine learning framework used for inference and model operations. It is used in this project for performing the model's computations and generating transcriptions.

### **How to Run the Application**

To run this app locally:
1. Install the required libraries:
   ```bash
   pip install streamlit torch librosa transformers
   ```
2. Download the project files, including a default **audio.wav** file if desired.
3. Run the app:
   ```bash
   streamlit run speech_to_text_app.py
   ```
4. Open the app in your browser, upload an audio file, and view the transcription in real-time.

### **Conclusion**

This **Speech-to-Text Transcription Tool** leverages advanced AI technologies to provide a simple, effective, and user-friendly solution for transcribing speech into text. Whether you need to transcribe interviews, lectures, podcasts, or meetings, this tool provides fast and accurate results. It is an excellent example of how deep learning models like Wav2Vec2 can be applied in practical applications to solve real-world problems.
