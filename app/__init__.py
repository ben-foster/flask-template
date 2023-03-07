from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.app_context().push()

CORS(app)

from app.routes import routes

app.register_blueprint(routes)

app.secret_key = os.environ['APP_SECRET']