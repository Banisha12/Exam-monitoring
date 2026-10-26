import pandas as pd
import os

# 1. Load Data (The Pipeline)
sessions_df = pd.read_csv('../data/synthetic/sessions.csv')
events_df = pd.read_csv('../data/synthetic/events.csv')

print("📊 BASELINE STATISTICS (Sprint 2 Results)")
print("-" * 40)

# 2. Session Count
total_sessions = len(sessions_df)
print(f"1. Total Sessions: {total_sessions}")

# 3. Average Duration (Metric 1)
avg_duration = sessions_df['duration_mins'].mean()
print(f"2. Average Session Duration: {round(avg_duration, 2)} minutes")

# 4. Event Summary (Metric 2)
events_per_session = events_df.groupby('session_id').size()
avg_events = events_per_session.mean()
max_events = events_per_session.max()
min_events = events_per_session.min()
print(f"3. Average Events per Session: {round(avg_events, 2)}")
print(f"   (Max: {max_events}, Min: {min_events})")

# 5. Missing Data Rate (Metric 3)
# Let's check if any 'event_type' or 'timestamp' is missing
missing_events = events_df['event_type'].isnull().sum()
missing_rate = (missing_events / len(events_df)) * 100
print(f"4. Missing Event Data Rate: {round(missing_rate, 2)}%")

print("-" * 40)
print("✅ Pipeline execution complete.")