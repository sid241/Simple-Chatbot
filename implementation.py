import io
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer

warnings.filterwarnings('ignore')
nltk.download('popular', quiet=True)

# Load and preprocess chatbot data
with open('chatbot.txt', 'r', encoding='utf8', errors='ignore') as file:
    corpus = file.read().lower()

sent_tokens = nltk.sent_tokenize(corpus)
word_tokens = nltk.word_tokenize(corpus)

lemmatizer = WordNetLemmatizer()

def preprocess(text):
    return [lemmatizer.lemmatize(token) for token in nltk.word_tokenize(text.lower().translate(str.maketrans('', '', string.punctuation)))]

# Greeting responses
greetings = {"hello", "hi", "hey", "greetings", "sup", "what's up"}
greeting_responses = ["Hey there!", "Hello!", "Hi, how can I assist you?", "Greetings!", "Hey! What's up?"]

def get_greeting(user_input):
    for word in user_input.split():
        if word.lower() in greetings:
            return random.choice(greeting_responses)
    return None

# Generate response
def generate_response(user_input):
    bot_response = ""
    sent_tokens.append(user_input)
    vectorizer = TfidfVectorizer(tokenizer=preprocess, stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sent_tokens)
    similarity_values = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    best_match_idx = similarity_values.argsort()[0][-2]
    
    flat_values = similarity_values.flatten()
    flat_values.sort()
    best_match_score = flat_values[-2]
    
    if best_match_score == 0:
        bot_response = "I'm not sure I understand. Could you rephrase that?"
    else:
        bot_response = sent_tokens[best_match_idx]
    
    sent_tokens.pop()
    return bot_response

print("BOT: Hello! I'm ChatBot. Type 'exit' to end our conversation.")

while True:
    user_input = input().strip().lower()
    if user_input in {"bye", "exit", "quit"}:
        print("BOT: Goodbye! Have a great day!")
        break
    elif user_input in {"thanks", "thank you"}:
        print("BOT: You're welcome!")
        break
    else:
        greeting = get_greeting(user_input)
        if greeting:
            print(f"BOT: {greeting}")
        else:
            print(f"BOT: {generate_response(user_input)}")
