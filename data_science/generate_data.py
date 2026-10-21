import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker('en_IN')
np.random.seed(42)
random.seed(42)

# Ensure directory exists
os.makedirs('../data/synthetic', exist_ok=True)

print("🚀 Generating Synthetic Data...")

# --- 1. CANDIDATES ---
candidates = []
for i in range(1, 101):
    candidates.append({
        'candidate_id': i,
        'roll_number': f"STU{i:03d}",
        'name': fake.name(),
        'seat_number': f"B-{random.randint(1, 100)}",
        'department': random.choice(['CSE', 'ECE', 'MECH', 'CIVIL'])
    })
pd.DataFrame(candidates).to_csv('../data/synthetic/candidates.csv', index=False)

# --- 2. SESSIONS ---
sessions = []
for i in range(1, 151):
    candidate_id = random.randint(1, 100)
    start_time = datetime(2024, 3, 15, 9, 0, 0) + timedelta(days=random.randint(0, 5))
    duration_mins = random.randint(150, 180)
    
    sessions.append({
        'session_id': i,
        'candidate_id': candidate_id,
        'exam_id': random.choice(['MATH2024', 'PHY2024', 'CSE2024']),
        'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'duration_mins': duration_mins,
        'status': 'completed'
    })
pd.DataFrame(sessions).to_csv('../data/synthetic/sessions.csv', index=False)

# --- 3. EVENTS ---
event_types = ['looking_away', 'phone_detected', 'left_seat', 'multiple_persons', 'talking', 'normal']
events = []
event_id = 1

for s in sessions:
    num_events = random.randint(10, 40)
    for _ in range(num_events):
        event_type = random.choices(event_types, weights=[15, 2, 3, 2, 5, 73])[0]
        event_time = datetime.strptime(s['start_time'], '%Y-%m-%d %H:%M:%S') + timedelta(minutes=random.randint(1, s['duration_mins']))
        
        events.append({
            'event_id': event_id,
            'session_id': s['session_id'],
            'candidate_id': s['candidate_id'],
            'event_type': event_type,
            'timestamp': event_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration_seconds': random.randint(1, 15) if event_type != 'normal' else 0,
            'confidence': round(random.uniform(0.70, 0.99), 2) if event_type != 'normal' else None
        })
        event_id += 1
pd.DataFrame(events).to_csv('../data/synthetic/events.csv', index=False)

# --- 4. SCORES ---
scores = []
for s in sessions:
    behavior_score = random.randint(40, 100)
    attention_score = random.randint(40, 100)
    integrity_score = (behavior_score * 0.6) + (attention_score * 0.4)
    
    scores.append({
        'score_id': s['session_id'],
        'session_id': s['session_id'],
        'candidate_id': s['candidate_id'],
        'behavior_score': behavior_score,
        'attention_score': attention_score,
        'integrity_score': round(integrity_score, 2)
    })
pd.DataFrame(scores).to_csv('../data/synthetic/scores.csv', index=False)

# --- 5. RISK DATA ---
risks = []
for s in scores:
    if s['integrity_score'] >= 80:
        risk_level = 'Low'
    elif s['integrity_score'] >= 50:
        risk_level = 'Moderate'
    else:
        risk_level = 'High'
        
    risks.append({
        'risk_id': s['session_id'],
        'session_id': s['session_id'],
        'candidate_id': s['candidate_id'],
        'integrity_score': s['integrity_score'],
        'risk_level': risk_level,
        'risk_reason': 'Calculated based on integrity score'
    })
pd.DataFrame(risks).to_csv('../data/synthetic/risk_data.csv', index=False)

# --- 6. AI REPORTS ---
ai_reports = []
for s in sessions:
    ai_reports.append({
        'report_id': s['session_id'],
        'session_id': s['session_id'],
        'candidate_id': s['candidate_id'],
        'report_path': f"reports/session_{s['session_id']}.pdf",
        'summary': f"Candidate performed exam {s['exam_id']}.",
        'model_version': 'v1.0-fake'
    })
pd.DataFrame(ai_reports).to_csv('../data/synthetic/ai_reports.csv', index=False)

print("✅ All 6 CSV datasets successfully generated in 'data/synthetic'!")