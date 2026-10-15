import os
from datetime import timedelta
from urllib.parse import quote_plus

# Get the absolute path of the project folder
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'dev-secret-key-change-in-prod'
    
    # ---------------- MySQL Database ----------------
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Banisha@890'          # ⚠️ PUT YOUR ACTUAL PASSWORD HERE
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_DB = 'exam_monitor'
    
    # URL-encode the password (handles @, #, $, ! etc.)
    ENCODED_PASSWORD = quote_plus(MYSQL_PASSWORD)
    
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://{MYSQL_USER}:{ENCODED_PASSWORD}'
        f'@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 280,
        'pool_pre_ping': True
    }
    
    # ---------------- Session settings ----------------
    IDLE_TIMEOUT = timedelta(minutes=10)
    MAX_EXAM_DURATION = timedelta(hours=3)
    
    # ---------------- Face detection ----------------
    FACE_MATCH_TOLERANCE = 0.6
    FRAME_INTERVAL_SEC = 2
    
    # ---------------- Storage ----------------
    FACE_UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'faces')
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    
    # ---------------- Event types ----------------
    EVENT_TYPES = [
        'looking_away',
        'phone_detected',
        'left_seat',
        'multiple_persons',
        'talking',
        'impersonation',
        'new_login'
    ]