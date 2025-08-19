# 🩺 Healthcare AI (Vision + Voice)

<p align="center">
  <img src="https://socialify.git.ci/Ayaan198/Healthcare-AI-using-Vision-and-Voice/image?font=Jost&language=1&name=1&owner=1&pattern=Solid&theme=Dark" alt="project-image">
</p>

An intelligent medical chatbot with multimodal capabilities including vision analysis, voice interaction, and comprehensive health consultations. This AI-powered assistant leverages generative AI technologies to provide personalized medical guidance through text, image, and voice inputs.

## 🚀 Demo

*[Add demo video/GIF here]*

## 🧐 Features

- 🧠 **AI-Powered Multimodal Assistant** – Processes text, images, and speech
- 🎙️ **Speech-to-Text** – Powered by OpenAI's Whisper model for accurate transcription
- 🔊 **Text-to-Speech** – Uses ElevenLabs for realistic medical assistant responses
- 🔬 **Vision Understanding** – Leverages Meta's Llama 3 Vision-90B for analyzing medical images
- 🌐 **Interactive Gradio App** – User-friendly interface for seamless communication
- 🏥 **Healthcare Applications** – Symptom checking, preliminary diagnosis guidance, patient engagement

## 🛠️ Installation Steps

### 1. Prerequisites
```bash
Python 3.8+
pipenv
```

### 2. Clone the Repository
```bash
git clone https://github.com/Ayaan198/Healthcare-AI-using-Vision-and-Voice.git
cd Healthcare-AI-using-Vision-and-Voice
```

### 3. Install dependencies with pipenv
```bash
pipenv install
```

### 4. Set up environment variables
Create `.env` file with your API keys:
```bash
ELEVENLABS_API_KEY=your_key
GROQ_API_KEY=your_key
```

### 5. Run application
```bash
python gradio_app.py
```

### 6. Access at
```
http://localhost:7860
```

## 💻 Technologies used

### AI Models:
- **Meta Llama3 Vision 90B** (multimodal understanding)
- **OpenAI Whisper** (speech-to-text)
- **ElevenLabs** (text-to-speech voice)

### Framework:
- **Gradio** (web interface)
- **Python 3.12+**
- **Pipenv** (dependency management)

### Libraries:
- **ffmpeg** (Audio format conversion for speech processing pipelines.)
- **portaudio** (Real-time microphone and speaker audio handling.)
- **pygame** (Audio playback control in CLI for generated speech responses.)


## 🤝 Contribution Guidelines

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open Pull Request

## 👨‍💻 Like my work?

⭐ **Star this repository if you found it helpful!**


**Issues:** [GitHub Issues](https://github.com/Ayaan198/Healthcare-AI-using-Vision-and-Voice/issues)

**Email:** ayanbate22@gmail.com

---
