from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import download
import pickle
import os

# Download stopwords if they are not already available
try:
    stopwords.words("english")
except LookupError:
    download("stopwords")
    
# Initialize once
class TextCleaner:
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    # 1. Convert to lowercase
    def convert_lowercase(self,text: str) -> str:
        return text.lower()

    # 2. Remove punctuation and special characters
    def remove_punctuation(self,text: str) -> str:
        cleaned = ''.join(c if c.isalnum() else ' ' for c in text)
        return ' '.join(cleaned.split())


    # 3. Remove stopwords
    def remove_stopwords(self,text: str) -> str:
        words = []
        for word in text.split():
            if word.lower() not in self.stop_words:
                words.append(word)
        return ' '.join(words)


    # 4. Stem words
    def stem_words(self,text: str) -> str:
        words = []
        for word in text.split():
            words.append(self.stemmer.stem(word))
        return ' '.join(words)


    # 5. Complete preprocessing pipeline
    def transform_text(self,text: str) -> str:
        text = self.convert_lowercase(text)
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        text = self.stem_words(text)
        return text


    def predict_spam(self,text: str) -> str:
        # Get absolute path to model directory based on this file's location
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(current_dir, '../../'))
        
        model_path = os.path.join(project_root, 'model', 'model.pkl')
        vectorizer_path = os.path.join(project_root, 'model', 'vectorizer.pkl')
        
        model = pickle.load(open(model_path, 'rb'))
        vectorizer = pickle.load(open(vectorizer_path, 'rb'))

        cleaned = self.transform_text(text)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]
        return "Email is Spam" if prediction == 1 else "Email is not Spam"
