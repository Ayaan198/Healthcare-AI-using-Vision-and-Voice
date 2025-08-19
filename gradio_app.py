import os
import gradio as gr
from healthcare_AI_brain import image_encoded, image_analysis_using_query
from patient_voice import audio_record, transcription_using_GROQAPI
from doctor_voice import text_to_speech

system_prompt="""
You are acting as a professional healthcare consultant for educational purposes only. Analyze the provided medical image with the expertise and communication style of an experienced physician.

**Instructions:**
- Begin your response directly with "Based on what I observe, you appear to have..." or "From what I can see, this looks like..."
- Provide your assessment in a single, flowing paragraph without bullet points, numbers, or special characters
- Speak directly to the person as their doctor would, using "you" and "your"
- Keep your response concise yet informative (maximum 3 sentences)
- If you identify potential conditions, briefly mention 2-3 practical management suggestions or when to seek care
- Maintain a professional but warm, reassuring tone
- Avoid AI-like phrases such as "I'm not a real doctor" or "this is just my analysis"
- Do not use markdown formatting, asterisks, or numbered lists
- Focus on observable findings and their most likely clinical significance

**Important:** Always conclude with appropriate guidance about consulting a healthcare professional for proper diagnosis and treatment, phrased naturally within your response.
"""

def process_inputs(audio_filepath, image_filepath):
    try:
        # Speech to text conversion
        speech_to_text = transcription_using_GROQAPI(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            audio_filepath=audio_filepath,
            stt_model="whisper-large-v3"
        )
    except Exception as e:
        print(f"Error in speech-to-text: {e}")
        speech_to_text = "Error processing audio"

    # Image analysis
    if image_filepath:
        try:
            doctor_response = image_analysis_using_query(
                query=system_prompt + speech_to_text,
                image_encoded=image_encoded(image_filepath),
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
        except Exception as e:
            print(f"Error in image analysis: {e}")
            doctor_response = "Sorry, I encountered an error analyzing the image. Please try again."
    else:
        doctor_response = "Please provide an image to analyze"

    # Text to speech conversion with error handling
    doctor_voice = text_to_speech(input_text=doctor_response, output_filepath="results.mp3")
    
    # Handle case where audio generation fails
    if doctor_voice is None:
        print("Audio generation failed, returning text only")
        return speech_to_text, doctor_response, None
    
    return speech_to_text, doctor_response, doctor_voice
    
# Create an interface
iface = gr.Interface(
    
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="Record your question"),
        gr.Image(type="filepath", label="Upload medical image (JPG/PNG)")
    ],
    outputs=[
        gr.Textbox(label="Your Question (Speech to Text)"),
        gr.Textbox(label="Doctor's Analysis"),
        gr.Audio(label="Doctor's Voice Response")
    ],
    title="🩺 Healthcare AI Doctor",
    description="<p style='text-align: center;'>Upload a medical image and ask your question using voice. Get AI-powered analysis with voice response.</p>",
    theme="soft"
)

iface.launch(debug=True, quiet=True)

# http://127.0.0.1:7860