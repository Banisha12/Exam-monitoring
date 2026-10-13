import os
from datetime import timedelta

# Get the absolute path of the project folder
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'dev-secret-key-change-in-prod'
    
    # Use absolute path with forward slashes (fixes OneDrive issue)
    DATABASE_PATH = os.path.join(BASE_DIR, 'database', 'exam_monitor.db').replace('\\', '/')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    IDLE_TIMEOUT = timedelta(minutes=10)
    MAX_EXAM_DURATION = timedelta(hours=3)
    FACE_MATCH_TOLERANCE = 0.6
    FRAME_INTERVAL_SEC = 2
    FACE_UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'faces')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    EVENT_TYPES = [
        'looking_away', 'phone_detected', 'left_seat',
        'multiple_persons', 'talking', 'impersonation', 'new_login'
    ]