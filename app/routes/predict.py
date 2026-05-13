from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.routes.cleaner_function import predict_spam

predict_bp = Blueprint('predict', __name__)


@predict_bp.route('/',methods=['GET'])
def home():
    message = request.args.get('message', '')
    return render_template('index.html',message=message)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.form.get('email_text','').strip()

    if not data:
        return redirect(url_for('predict.home', message="Please enter email text for prediction."))

    prediction = predict_spam(data)

    return redirect(url_for('predict.home',message=str(prediction)))