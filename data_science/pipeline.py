import pandas as pd
import os

# 1. Load Data (Pointing to the LARGE dataset)
print("Loading large datasets... Please wait.")
sessions_df = pd.read_csv('../data/synthetic/sessions_large.csv')
events_df = pd.read_csv('../data/synthetic/events_large.csv')

print("\n📊 BASELINE STATISTICS (Sprint 2 Results - Large Dataset)")
print("-" * 50)

# 2. Session Count
total_sessions = len(sessions_df)
print(f"1. Total Sessions: {total_sessions}")

# 3. Average Duration (Metric 1)
avg_duration = sessions_df['duration_mins'].mean()
print(f"2. Average Session Duration: {round(avg_duration, 2)} minutes")

# 4. Event Summary (Metric 2)
# Note: We use a Left Merge to handle sessions with 0 events properly
merged_data = pd.merge(sessions_df[['session_id']], events_df, on='session_id', how='left')
events_per_session = merged_data.groupby('session_id')['event_id'].count() # Count event IDs

avg_events = events_per_session.mean()
max_events = events_per_session.max()
min_events = events_per_session.min()

print(f"3. Average Events per Session: {round(avg_events, 2)}")
print(f"   (Max: {max_events}, Min: {min_events})")

# 5. Missing Data Rate (Metric 3)
# We check if any 'event_type' is missing in the raw events file
missing_events = events_df['event_type'].isnull().sum()
missing_rate = (missing_events / len(events_df)) * 100
print(f"4. Missing Event Data Rate: {round(missing_rate, 2)}%")

print("-" * 50)
print("✅ Pipeline execution complete.")