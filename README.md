# 🩺 Welcome to the Healthcare AI (Vision + Voice) Assistant!
In this project, we developed an **AI-powered medical assistant** that combines **multimodal capabilities** (text, image, and voice) to provide intelligent healthcare interactions. The system allows users to **upload medical images**, **ask questions via voice or text**, and **receive AI-generated medical insights** through both text and speech.

This solution is designed for **patients, healthcare researchers, and developers** exploring the use of **generative AI in medical assistance** for symptom analysis and preliminary health guidance.

---

## 🧠 The Team:
| Member             | Position               | Responsibilities                        |
| ------------------- | ---------------------- | --------------------------------------- |
| **Ayaan Ali Bate**  | Full Stack + AI        | AI model integration, Voice & Vision pipeline |

---

## 🚀 Key Features
### Multimodal AI Interaction
- **Text + Voice Input**: Ask health-related queries through speech or text.
- **Image Uploads**: Analyze medical images such as skin conditions for early detection.
- **AI Responses**: Provides AI-powered health guidance in text and voice format.

### Speech Processing
- **Speech-to-Text**: Uses OpenAI Whisper for accurate transcription.
- **Text-to-Speech**: Realistic voice responses powered by ElevenLabs.

### Interactive Interface
- **Gradio Web App** for seamless interaction.
- **CLI Mode** for audio-based feedback on Windows systems.

---

## 🛠️ Tech Stack
- **AI Models**: Meta LLaMA 4, Scout 17B, OpenAI Whisper, ElevenLabs
- **Framework**: Gradio
- **Language**: Python 3.12+
- **Audio Handling**: FFmpeg, PortAudio, Pygame
- **Environment Management**: Pipenv

---

## 📂 Project Structure
```plaintext
Healthcare-AI-using-Vision-and-Voice/
│
├── gradio_app.py               # Main application script
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
├── assets/                     # Audio and image assets
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started
### Prerequisites
- Python 3.8+ (Recommended: 3.12+)
- Pipenv for dependency management
- FFmpeg installed on your system

### 1. Clone the Repository
```bash
git clone https://github.com/Ayaan198/Healthcare-AI-using-Vision-and-Voice.git
cd Healthcare-AI-using-Vision-and-Voice
```

### 2. Install Dependencies
```bash
pipenv install
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory and add:
```env
ELEVENLABS_API_KEY=your_key
GROQ_API_KEY=your_key
```

### 4. Run the Application
```bash
python gradio_app.py
```

Once running, access the app at:
```
http://localhost:7860
```

---

## ✅ Future Enhancements
- Integration with **EHR (Electronic Health Records)** systems.
- **Mobile App** support for Android and iOS.
- **Real-time video consultations** with integrated AI.

---

## 👨‍💻 Contributions
We welcome contributions!
1. Fork the repository
2. Create a new branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push the branch (`git push origin feature/NewFeature`)
5. Create a pull request

⭐ **Star this repository if you found it useful!**

---

## 📧 Contact
**Email**: ayanbate22@gmail.com  
**Issues**: [GitHub Issues](https://github.com/Ayaan198/Healthcare-AI-using-Vision-and-Voice/issues)

---

> **Disclaimer**: This AI assistant is for educational and research purposes only. Always consult with qualified healthcare professionals for medical advice and diagnosis.
