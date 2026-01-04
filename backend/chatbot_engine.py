import json, random, pickle, re
import numpy as np
import nltk
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
import google.generativeai as genai
import os

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")


lemmatizer = WordNetLemmatizer()

BASE_DIR = os.path.dirname(__file__)

intents = json.loads(open(os.path.join(BASE_DIR, "intents.json")).read())
words = pickle.load(open(os.path.join(BASE_DIR, "words.pkl"), "rb"))
classes = pickle.load(open(os.path.join(BASE_DIR, "classes.pkl"), "rb"))
model = load_model(os.path.join(BASE_DIR, "chatbot.h5"))


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini = genai.GenerativeModel("gemini-1.5-flash")
chat = gemini.start_chat(history=[])

def clean_text(text):
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    sentences = text.split(". ")
    return ". ".join(sentences[:3])

def bag_of_words(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(w.lower()) for w in sentence_words]
    bag = [1 if w in sentence_words else 0 for w in words]
    return np.array(bag)

def predict_intent(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    threshold = 0.75

    results = [
        {"intent": classes[i], "confidence": float(r)}
        for i, r in enumerate(res) if r > threshold
    ]
    return sorted(results, key=lambda x: x["confidence"], reverse=True)

def get_static_response(intent):
    for i in intents["intents"]:
        if i["tags"] == intent:
            return random.choice(i["responses"])
    return None

def gemini_reply(query):
    try:
        response = chat.send_message(query)
        return clean_text(response.text)
    except:
        return "I'm having trouble answering right now."
