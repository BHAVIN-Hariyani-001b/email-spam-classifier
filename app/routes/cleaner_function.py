from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pickle
import os

# Initialize once
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# 1. Convert to lowercase
def convert_lowercase(text: str) -> str:
    return text.lower()

# 2. Remove punctuation and special characters
def remove_punctuation(text: str) -> str:
    cleaned = ''
    for ch in text:
        if ch.isalnum() or ch.isspace():
            cleaned += ch
        else:
            cleaned += ' '
    return ' '.join(cleaned.split())


# 3. Remove stopwords
def remove_stopwords(text: str) -> str:
    words = []
    for word in text.split():
        if word.lower() not in stop_words:
            words.append(word)
    return ' '.join(words)


# 4. Stem words
def stem_words(text: str) -> str:
    words = []
    for word in text.split():
        words.append(stemmer.stem(word))
    return ' '.join(words)


# 5. Complete preprocessing pipeline
def transform_text(text: str) -> str:
    text = convert_lowercase(text)
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    text = stem_words(text)
    return text


def predict_spam(text: str) -> str:
    # Get absolute path to model directory based on this file's location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '../../'))
    
    model_path = os.path.join(project_root, 'model', 'model.pkl')
    vectorizer_path = os.path.join(project_root, 'model', 'vectorizer.pkl')
    
    model = pickle.load(open(model_path, 'rb'))
    vectorizer = pickle.load(open(vectorizer_path, 'rb'))

    cleaned = transform_text(text)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]
    return "Email is Spam" if prediction == 1 else "Email is not Spam"

