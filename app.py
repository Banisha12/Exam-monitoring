from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database (MySQL)
db = SQLAlchemy(app)

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Ensure upload folders exist
os.makedirs(app.config['FACE_UPLOAD_FOLDER'], exist_ok=True)


# ---------- MODELS ----------
class Candidate(db.Model):
    __tablename__ = 'candidates'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roll_number = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    seat_number = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    photo_path = db.Column(db.String(300), nullable=False)
    face_encoding = db.Column(db.LargeBinary, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    exam_id = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    end_time = db.Column(db.DateTime, nullable=True)
    end_reason = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(20), default='active')


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    confidence = db.Column(db.Float, nullable=True)
    event_metadata = db.Column(db.Text, nullable=True)
    reviewed = db.Column(db.Integer, default=0)


class IntegrityReport(db.Model):
    __tablename__ = 'integrity_reports'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    session_id = db.Column(db.Integer, db.ForeignKey('sessions.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    total_events = db.Column(db.Integer, default=0)
    integrity_score = db.Column(db.Float, nullable=True)
    flag = db.Column(db.String(20), nullable=True)
    generated_at = db.Column(db.DateTime, default=db.func.current_timestamp())


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
        print("✅ MySQL tables created (or already exist)!")
    app.run(debug=True, port=5000)