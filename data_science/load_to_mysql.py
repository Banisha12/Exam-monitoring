import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

print("🚀 Starting Database Load...")

# 1. Connect
raw_password = "Banisha@890" 
safe_password = quote_plus(raw_password)
# Notice we explicitly tell it to use utf8mb4 for the avatars/emojis
DB_URI = f"mysql+pymysql://root:{safe_password}@localhost:3306/exam_monitor?charset=utf8mb4"
engine = create_engine(DB_URI)

# 2. Load CSVs
print("Loading CSVs...")
candidates_df = pd.read_csv('../data/synthetic/candidates_large.csv')
sessions_df = pd.read_csv('../data/synthetic/sessions_large.csv')
events_df = pd.read_csv('../data/synthetic/events_large.csv')
scores_df = pd.read_csv('../data/synthetic/scores_large.csv')
risks_df = pd.read_csv('../data/synthetic/risk_data_large.csv')
reports_df = pd.read_csv('../data/synthetic/ai_reports_large.csv')

# 3. Rename primary key columns to 'id' to match the old schema style
candidates_df = candidates_df.rename(columns={'candidate_id': 'id'})
sessions_df = sessions_df.rename(columns={'session_id': 'id'})
events_df = events_df.rename(columns={'event_id': 'id'})
scores_df = scores_df.rename(columns={'score_id': 'id'})
risks_df = risks_df.rename(columns={'risk_id': 'id'})
reports_df = reports_df.rename(columns={'report_id': 'id'})

# 4. Push to MySQL (This will create the tables automatically)
print("Pushing Candidates...")
candidates_df.to_sql('candidates', con=engine, if_exists='replace', index=False)

print("Pushing Sessions...")
sessions_df.to_sql('sessions', con=engine, if_exists='replace', index=False)

print("Pushing Events (This might take 5-10 seconds)...")
events_df.to_sql('events', con=engine, if_exists='replace', index=False, chunksize=5000)

print("Pushing Scores...")
scores_df.to_sql('scores', con=engine, if_exists='replace', index=False)

print("Pushing Risk Data...")
risks_df.to_sql('risk_profiles', con=engine, if_exists='replace', index=False)

print("Pushing AI Reports...")
reports_df.to_sql('ai_reports', con=engine, if_exists='replace', index=False)

print("✅ ALL DATA SUCCESSFULLY LOADED INTO MYSQL!")