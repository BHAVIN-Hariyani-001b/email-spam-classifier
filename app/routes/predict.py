from flask import Blueprint, request, render_template, redirect, url_for
from app.routes.cleaner_function import TextCleaner

predict_bp = Blueprint('predict', __name__)

text_cleaner = TextCleaner()

@predict_bp.route('/',methods=['GET'])
def home():
    message = request.args.get('message', '')
    data = request.args.get('data', '')
    return render_template('index.html',message=message,data=data)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.form.get('email_text','').strip()

    if not data:
        return redirect(url_for('predict.home', message="Please enter email text for prediction."))
    try:
        prediction = text_cleaner.predict_spam(data)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return redirect(url_for('predict.home', message=f"Error during prediction"))

    return redirect(url_for('predict.home',message=str(prediction),data=str(data)))