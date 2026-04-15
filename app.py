from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from datasets import load_dataset
import uvicorn
import os

# Custom modules
from nlp_processor import NLPManager
from model_handler import get_ai_response, generate_voice

# 1. Initialize App
app = FastAPI()

# 2. Add CORS Middleware (Crucial for Frontend-Backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Setup Folders & Tools
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")
nlp_tool = NLPManager()

# 4. Load Dataset BEFORE the endpoint starts
print("Loading Travel Dataset...")
dataset = load_dataset("bitext/Bitext-travel-llm-chatbot-training-dataset", split='train')
df = pd.DataFrame(dataset.select(range(1000))) 
print("Dataset ready!")

# 5. Helper Function (Defined before the chat route)
def get_travel_context(user_query):
    keywords = user_query.lower().split()
    mask = df['instruction'].str.contains('|'.join(keywords), case=False, na=False)
    results = df[mask].head(2) 
    if not results.empty:
        return "\n".join([f"Q: {row['instruction']} A: {row['response']}" for _, row in results.iterrows()])
    return "No specific travel data found."

class UserQuery(BaseModel):
    message: str

# 6. The API Route
@app.post("/chat")
async def chat(query: UserQuery):
    # Process NLP (NER and Sentiment)
    nlp_results = nlp_tool.analyze(query.message)
    
    # Get Dataset Context
    context = get_travel_context(query.message)
    
    # Get LLM Response from Ollama
    answer = get_ai_response(query.message, context)
    
    # Generate TTS Audio
    audio_file = generate_voice(answer)
    
    return {
        "reply": answer,
        "audio_url": f"http://localhost:8000/static/{audio_file}",
        "nlp_metadata": nlp_results
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)