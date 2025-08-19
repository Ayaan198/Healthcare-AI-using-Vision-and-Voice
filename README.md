# 🩺 Healthcare AI (Vision + Voice)

An intelligent medical chatbot with multimodal capabilities including vision analysis, voice interaction, and comprehensive health consultations. Users can upload medical images (like skin allergies), ask questions via voice input, and receive AI-powered medical insights through both voice and text responses. This AI-powered assistant combines generative AI technologies to provide personalized medical guidance through text, image, and voice inputs.

## 🚀 Demo

*[Add a demo video here]*

## 🧐 Features

- 🧠 **AI-Powered Multimodal Assistant** – Processes text, images, and speech
- 🎙️ **Speech-to-Text** – Powered by OpenAI's Whisper model for accurate transcription
- 🔊 **Text-to-Speech** – Uses ElevenLabs for realistic medical assistant responses
- 🔬 **Vision Understanding** – Leverages Meta's Llama 4 Scout 17B for analyzing medical images
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
- **Meta Llama 4 Scout 17B** (Multimodal AI for text & medical image analysis.)
- **OpenAI Whisper** (Speech-To-Text transcription)
- **ElevenLabs** (Realistic Text-To-Speech synthesis)

### Framework:
- **Gradio** (Interactive web interface)
- **Python 3.12+** (Core programming language)
- **Pipenv** (Virtual environment & dependency management)

### Libraries:
- **ffmpeg** (Audio format conversion for speech processing.)
- **portaudio** (Real-time microphone and speaker audio handling.)
- **pygame** (Audio playback control in CLI for generated speech responses for Windows)


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
