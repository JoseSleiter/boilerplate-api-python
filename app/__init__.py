import os
from flask import Flask
from .src.route import api

# Define allowed files
ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = os.path.join('staticFiles', 'uploads')

def create_app():
    app = Flask(__name__)
    # Configure upload file path flask
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.secret_key = 'This is your secret key to utilize session in Flask'
    
    api.init_app(app)

    return app