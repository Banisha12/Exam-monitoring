import pandas as pd
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

print("Connecting to MySQL...")
raw_password = "Banisha@890" 
safe_password = quote_plus(raw_password)
DB_URI = f"mysql+pymysql://root:{safe_password}@localhost:3306/exam_monitor?charset=utf8mb4"
engine = create_engine(DB_URI)

print("Updating ALL sessions with video paths...")

# Update all 10,000 students in one go
with engine.begin() as conn:
    # This updates the session table based on the candidate_id
    conn.execute(text("""
        UPDATE sessions 
        SET video_path = CONCAT('videos/STU', LPAD(candidate_id, 5, '0'), '_live.mp4')
    """))

print("✅ Successfully linked all 10,000 videos to the database sessions!")