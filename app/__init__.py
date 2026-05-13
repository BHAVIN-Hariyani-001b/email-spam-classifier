from flask import Flask

def create_app():
    app = Flask(__name__)

    import app.routes.predict as predict
    app.register_blueprint(predict.predict_bp)
    
    return app