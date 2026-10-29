import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker('en_IN')
np.random.seed(42)
random.seed(42)

os.makedirs('../data/synthetic', exist_ok=True)

print("🚀 Generating large dataset (10k candidates, 15k sessions)...")

# --- 1. CANDIDATES ---
candidates = []
for i in range(1, 10001):
    roll_number = f"STU{i:05d}"
    
    # FIX: Handle the different extensions for your real photos vs generated avatars
    if i == 1:
        avatar_path = f"avatars/{roll_number}.png"   # Your real photo
    elif i == 2:
        avatar_path = f"avatars/{roll_number}.jpeg"  # Your friend's real photo
    else:
        avatar_path = f"avatars/{roll_number}.svg"   # Generated avatars
        
    candidates.append({
        'candidate_id': i,
        'roll_number': roll_number,
        'name': fake.name(),
        'seat_number': f"B-{random.randint(1, 500)}",
        'department': random.choice(['CSE', 'ECE', 'MECH', 'CIVIL', 'IT']),
        'avatar_path': avatar_path
    })
pd.DataFrame(candidates).to_csv('../data/synthetic/candidates_large.csv', index=False)

# --- 2. SESSIONS, EVENTS, SCORES, RISKS, REPORTS ---
sessions, events, scores, risks, ai_reports = [], [], [], [], []
event_id = 1
event_types = ['looking_away', 'phone_detected', 'left_seat', 'multiple_persons', 'talking', 'normal']

print("Generating sessions, events, risks, and reports...")
for i in range(1, 15001):
    candidate_id = random.randint(1, 10000)
    archetype = random.choices(['Good', 'Distracted', 'Cheater'], weights=[70, 20, 10])[0]

    start_time = datetime(2024, 3, 15, 9, 0, 0) + timedelta(days=random.randint(0, 30), minutes=random.randint(0, 480))
    duration_mins = random.randint(120, 180)
    
    # 1. SESSIONS
    sessions.append({
        'session_id': i, 'candidate_id': candidate_id, 'exam_id': random.choice(['MATH2024', 'PHY2024', 'CSE2024']),
        'start_time': start_time.strftime('%Y-%m-%d %H:%M:%S'),
        'duration_mins': duration_mins, 'status': 'completed'
    })

    # Determine events & score based on archetype
    if archetype == 'Good':
        num_events = random.randint(0, 3)
        integrity_score = random.randint(85, 100)
        risk_level = 'Low'
    elif archetype == 'Distracted':
        num_events = random.randint(5, 15)
        integrity_score = random.randint(55, 84)
        risk_level = 'Moderate'
    else:
        num_events = random.randint(20, 50)
        integrity_score = random.randint(15, 54)
        risk_level = 'High'

    # 2. EVENTS
    for _ in range(num_events):
        event_type = random.choices(event_types, weights=[20, 5, 3, 2, 5, 65])[0]
        event_time = start_time + timedelta(minutes=random.randint(1, duration_mins))
        events.append({
            'event_id': event_id, 'session_id': i, 'candidate_id': candidate_id,
            'event_type': event_type, 'timestamp': event_time.strftime('%Y-%m-%d %H:%M:%S'),
            'duration_seconds': random.randint(1, 20), 'confidence': round(random.uniform(0.6, 0.99), 2)
        })
        event_id += 1

    # 3. SCORES
    scores.append({
        'score_id': i, 'session_id': i, 'candidate_id': candidate_id,
        'behavior_score': integrity_score, 'attention_score': integrity_score,
        'integrity_score': integrity_score
    })

    # 4. RISK DATA
    risks.append({
        'risk_id': i, 'session_id': i, 'candidate_id': candidate_id,
        'integrity_score': integrity_score, 'risk_level': risk_level,
        'risk_reason': f'Calculated based on {archetype} behavior profile'
    })

    # 5. AI REPORTS
    ai_reports.append({
        'report_id': i, 'session_id': i, 'candidate_id': candidate_id,
        'report_path': f"reports/session_{i}.pdf",
        'summary': f"Candidate {candidate_id} completed {sessions[-1]['exam_id']}. Risk: {risk_level}.",
        'model_version': 'v1.0-industry'
    })

# Save all to CSVs
pd.DataFrame(sessions).to_csv('../data/synthetic/sessions_large.csv', index=False)
pd.DataFrame(events).to_csv('../data/synthetic/events_large.csv', index=False)
pd.DataFrame(scores).to_csv('../data/synthetic/scores_large.csv', index=False)
pd.DataFrame(risks).to_csv('../data/synthetic/risk_data_large.csv', index=False)
pd.DataFrame(ai_reports).to_csv('../data/synthetic/ai_reports_large.csv', index=False)

print(f"✅ Done! Generated {len(sessions)} sessions, {len(events)} events, {len(risks)} risk profiles, and {len(ai_reports)} AI reports.")