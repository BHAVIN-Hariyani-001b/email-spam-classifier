# 📧 Email Spam Detection using Machine Learning

A Machine Learning-based web application that classifies emails as **Spam** or **Not Spam** in real time. The project uses **TF-IDF Vectorization**, **Naive Bayes**, and **NLTK** for text preprocessing, and is deployed as a web application using **Flask** and [Render](https://render.com?utm_source=chatgpt.com).

---

## 🚀 Live Demo

🌐 **Live Application:** https://email-spam-classifier-rc9e.onrender.com/

---
## 📷 Screenshots
---
[Screenshot1](image/Screenshot%202026-05-14%20104353.png)
---
[Screenshot2](image/Screenshot%202026-05-14%20104458.png)
---
---

## 📌 Project Overview

Email spam detection is a classic **Text Classification** problem in **Machine Learning**. The system analyzes the content of an email and predicts whether it is **Spam** or **Not Spam**.

This project uses **Natural Language Processing (NLP) techniques** because emails are unstructured text data. Machine learning models cannot work directly with raw text, so the text must first be cleaned and transformed into numerical features.

The application applies several NLP techniques, including:

- Converting text to lowercase
- Removing punctuation and special characters
- Removing common stopwords
- Stemming words using Porter Stemmer
- Converting text into numerical vectors using **CountVectorizer**

After preprocessing, the numerical features are passed to a **Multinomial Naive Bayes** classifier, which predicts whether the email is spam or not spam in real time through a Flask web application.

The application performs:

- Text cleaning and preprocessing
- Lowercase conversion
- Punctuation removal
- Stopword removal
- Word stemming
- Feature extraction using CountVectorizer
- Spam classification using Multinomial Naive Bayes
- Real-time prediction through a Flask web interface

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning & NLP
- [scikit-learn](https://scikit-learn.org?utm_source=chatgpt.com)
- [NLTK](https://www.nltk.org?utm_source=chatgpt.com)
- [NumPy](https://numpy.org?utm_source=chatgpt.com)
- [Pandas](https://pandas.pydata.org?utm_source=chatgpt.com)

### Web Development
- [Flask](https://flask.palletsprojects.com?utm_source=chatgpt.com)
- HTML5
- CSS3

### Deployment
- [Gunicorn](https://gunicorn.org?utm_source=chatgpt.com)
- [Render](https://render.com?utm_source=chatgpt.com)

---

## 📂 Project Structure

```text
Email-Spam-Detection/
│
├── app/
│   ├── __init__.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   └── routes/
│       ├── predict.py
│       └── cleaner_function.py
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebook/
│    ├── email-spam.ipynb
│    └── predictor.ipynb
│
├── run.py
├── requirements.txt
└── README.md
```
---

## 🧠 Machine Learning Workflow

- Load and clean the email dataset
- Convert text to lowercase
- Remove punctuation and special characters
- Remove stopwords using NLTK
- Apply Porter Stemming
- Transform text into TF-IDF vectors
- Train a Logistic Regression model
- Save the trained model and vectorizer
- Deploy with Flask and Render

---

## 📝 Text Preprocessing
- Lowercasing
- Punctuation removal
- Stopword removal
- Porter stemming
---
## Example:
```
Input:  "Congratulations! You have won a free prize."
Output: "congratul free prize"
```
---

## 💻 Installation
- 1 Clone the Repository
```
git clone https://github.com/your-username/email-spam-detection.git
cd email-spam-detection
```
- 2 Create a Virtual Environment
```
python -m venv venv
```
- 3 Activate the Environment
    - 1 Windows
    ```
    venv\Scripts\activate
    ```

    - 2 Linux / macOS
    ```
    source venv/bin/activate
    ```

- 4 Install Dependencies
 ```
 pip install -r requirements.txt
 ```

- 5 Run the Application
```
python run.py
```

- 6 Open your browser and visit:
```
http://127.0.0.1:5000
```
---
## 🧪 Example Predictions
```
Email Text	Prediction
Congratulations! You won a free iPhone.	Spam
Meeting scheduled for tomorrow at 10 AM.	Not Spam
Claim your $1000 reward now!	Spam
Please review the attached project report.	Not Spam
```
---
## 🎯 Future Improvements
Add confidence scores
Support multiple ML models
Build a REST API
Add user authentication
Store prediction history

---

## 📚 Learning Outcomes

Through this project, I learned:

Natural Language Processing fundamentals
Text preprocessing techniques
TF-IDF vectorization
Logistic Regression for classification
Model serialization with Pickle
Flask application development
Deployment to Render

---

## 👨‍💻 Author
BH EDIT

- GitHub: https://github.com/BHAVIN-Hariyani-001b
- LinkedIn: https://www.linkedin.com/in/bhavin-hariyani-598263310/

---

## 📄 License

This project is licensed under the MIT License.

---

### ⭐ Support
If you found this project helpful, please give it a ⭐ on GitHub!