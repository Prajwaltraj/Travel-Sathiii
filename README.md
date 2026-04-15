# <span style="font-size:36px; color:#2E86C1; font-weight:bold;">Travel Sathi — NLP Travel Companion</span>  
### <span style="font-size:20px; color:#1ABC9C;">Domain: ✈️ Travel</span>  

### <span style="font-size:20px; color:#F39C12;">Hackathon: Hack4Hour 2026</span>  

#### 🌟 <span style="color:#8E44AD; font-size:22px; font-weight:bold;">Overview</span>  
<span style="font-size:16px; color:#34495E;">Travel Sathi is a full-stack conversational AI designed to solve the complexity of trip planning. It allows users to input natural language queries about destinations and budgets, providing context-aware responses through an interactive chat interface.</span>  

---

#### 🧠 <span style="color:#27AE60; font-size:20px;">NLP Features (Min. 2 Required)</span>  
We have implemented the following NLP techniques on our Python backend:  

- **Intent Detection (Feature A):**  
  <span style="color:#2C3E50;">Classifies user input into categories such as "Recommendation," "Weather Inquiry," or "Budget Planning".</span>  
  **Tools Used:** <span style="color:#E74C3C;">Sklearn / NLTK</span>  

- **Named Entity Recognition (Feature E):**  
  <span style="color:#2C3E50;">Extracts specific entities like destinations (GPE) and dates from user sentences to personalize responses.</span>  
  **Tools Used:** <span style="color:#E74C3C;">SpaCy</span>  

---

💻 **Tech Stack**  
- Backend: <span style="color:#2980B9;">Python with Flask/FastAPI</span>  
- Frontend: <span style="color:#2980B9;">HTML/CSS/JS (or your specific framework)</span>  
- NLP Libraries: <span style="color:#2980B9;">SpaCy, Sklearn, and NLTK</span>  

📊 **Dataset Reference**  
- Name: <span style="color:#D35400;">[Insert Name of Dataset, e.g., Kaggle World Tourism Dataset]</span>  
- Usage: Used to train the Intent Classifier and provide destination-specific data for the chatbot's responses.  

---

🚀 **Getting Started**  
**Prerequisites**  
- Python 3.8+  
- `pip install -r requirements.txt`  

**Running the App**  
- Start Backend:  
  ```bash
  python app.py
