import spacy
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Initialize traditional NLP tools
class NLPManager:
    def __init__(self):
        # Feature 1: Named Entity Recognition (using SpaCy)
        self.nlp = spacy.load("en_core_web_sm")
        # Feature 2: Sentiment Analysis (using NLTK VADER)
        try:
            self.sia = SentimentIntensityAnalyzer()
        except LookupError:
            nltk.download('vader_lexicon')
            self.sia = SentimentIntensityAnalyzer()

    def analyze(self, text):
        doc = self.nlp(text)
        # Extracting entities (Names, Dates, Orgs)
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
        
        # Calculate sentiment score
        sentiment_score = self.sia.polarity_scores(text)['compound']
        
        return {
            "entities": entities,
            "sentiment": "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
        }