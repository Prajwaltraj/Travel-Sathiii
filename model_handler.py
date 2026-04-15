import ollama
from gtts import gTTS
import os
import uuid

def get_ai_response(user_input, dataset_context):
    # System prompt to ensure the bot uses your specific dataset
    prompt = f"Context from Dataset: {dataset_context}\n\nUser Question: {user_input}"
    
    # INDENTATION FIXED: These lines must be inside the function
    response = ollama.chat(model='llama3:8b', messages=[ 
        {'role': 'system', 'content': 'You are a helpful domain-specific assistant.'},
        {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']

def generate_voice(text):
    # Create unique filename for each response
    filename = f"response_{uuid.uuid4().hex[:8]}.mp3"
    
    # Ensure the path is correct for the static folder
    filepath = os.path.join("static", filename)
    
    # Generate speech
    tts = gTTS(text=text, lang='en')
    tts.save(filepath)
    return filename