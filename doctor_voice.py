import os
import pygame
import subprocess
import platform
import time
import uuid
from elevenlabs import generate, save, set_api_key

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech(input_text, output_filepath):
    set_api_key(ELEVENLABS_API_KEY)
    
    try:
        # Generate unique filename to avoid conflicts
        unique_filename = f"audio_{uuid.uuid4().hex[:8]}_{int(time.time())}.mp3"
        temp_filepath = unique_filename if output_filepath == "results.mp3" else output_filepath
        
        # Generate audio
        audio = generate(
            text=input_text,
            voice="TxGEqnHWrfWFTfGW9XjX",  # Josh voice
            model="eleven_turbo_v2",
        )
        
        # Remove existing file if it exists
        if os.path.exists(temp_filepath):
            try:
                os.remove(temp_filepath)
            except Exception as e:
                print(f"Warning: Could not remove existing file: {e}")
        
        # Save audio file with error handling
        try:
            save(audio, temp_filepath)
            print(f"Audio saved to: {temp_filepath}")
        except Exception as save_error:
            print(f"Error saving audio file: {save_error}")
            return None
        
        # Play audio with pygame (default for Windows)
        pygame_success = False
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(temp_filepath)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                pygame.time.wait(100)  # Check every 100ms
            pygame_success = True
            
        except Exception as e:
            print(f"Error playing audio with pygame: {e}")
        
        # Only use fallback if pygame completely failed
        if not pygame_success:
            try:
                os_name = platform.system()
                if os_name == "Darwin":  # macOS
                    subprocess.run(['afplay', temp_filepath])
                elif os_name == "Windows":  # Windows
                    subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{temp_filepath}").PlaySync();'])
                elif os_name == "Linux":  # Linux
                    subprocess.run(['mpg123', '-q', temp_filepath])  # -q for quiet mode
                else:
                    print("Unsupported operating system for audio playback")
            except Exception as fallback_error:
                print(f"Fallback audio playback also failed: {fallback_error}")
        
        return temp_filepath
        
    except Exception as main_error:
        print(f"Main text_to_speech error: {main_error}")
        return None

# Test code (remove this when using in production)
if __name__ == "__main__":
    input_text = "Hi My name is Ayaan, a Computer Engineering graduate!"
    result = text_to_speech(input_text, output_filepath="doctor_voice.mp3")
    if result:
        print(f"Success! Audio file: {result}")
    else:
        print("Failed to generate audio")