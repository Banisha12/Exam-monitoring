from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Ensure folders exist
os.makedirs(app.config['FACE_UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('database', exist_ok=True)

# ---------- ROUTES ----------
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/health')
def health():
    return {"status": "ok", "message": "Smart Exam Monitor running"}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)