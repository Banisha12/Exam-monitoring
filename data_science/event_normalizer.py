from datetime import datetime, timedelta

print("🚀 Starting Sprint 3: Event Normalization Pipeline\n")

# 1. Simulate Raw Detections (What the AI camera sees frame-by-frame)
# Notice how 'looking_away' happens 4 times in a row (frames 2, 3, 4, 5).
# 'phone_detected' happens twice with low confidence.
raw_frames = [
    {"frame": 1, "time": "10:00:01", "detection": "normal", "confidence": 0.99},
    {"frame": 2, "time": "10:00:02", "detection": "looking_away", "confidence": 0.95},
    {"frame": 3, "time": "10:00:03", "detection": "looking_away", "confidence": 0.96},
    {"frame": 4, "time": "10:00:04", "detection": "looking_away", "confidence": 0.94},
    {"frame": 5, "time": "10:00:05", "detection": "looking_away", "confidence": 0.95},
    {"frame": 6, "time": "10:00:06", "detection": "normal", "confidence": 0.99},
    {"frame": 7, "time": "10:00:07", "detection": "phone_detected", "confidence": 0.45}, # Uncertain!
    {"frame": 8, "time": "10:00:08", "detection": "phone_detected", "confidence": 0.48}, # Uncertain!
    {"frame": 9, "time": "10:00:09", "detection": "normal", "confidence": 0.99},
]

# 2. Define Rules
CONFIDENCE_THRESHOLD = 0.60  # If confidence < 0.60, mark as "Uncertain"
normalized_events = []

# 3. The Normalization Logic
current_event = None

for frame in raw_frames:
    detection = frame["detection"]
    confidence = frame["confidence"]
    time_obj = datetime.strptime(frame["time"], "%H:%M:%S")

    # Rule: Skip 'normal' frames
    if detection == "normal":
        if current_event:
            # If we were tracking an event and it ends, save it
            normalized_events.append(current_event)
            current_event = None
        continue

    # Rule: Group consecutive identical detections
    if current_event is None:
        # Start a new event
        current_event = {
            "event_type": detection,
            "start_time": time_obj,
            "end_time": time_obj,
            "max_confidence": confidence,
            "status": "Confirmed" if confidence >= CONFIDENCE_THRESHOLD else "Uncertain"
        }
    elif current_event["event_type"] == detection:
        # Update the existing event (extend duration, update max confidence)
        current_event["end_time"] = time_obj
        if confidence > current_event["max_confidence"]:
            current_event["max_confidence"] = confidence
        if confidence >= CONFIDENCE_THRESHOLD:
            current_event["status"] = "Confirmed"
    else:
        # A different event started (e.g., looking_away -> phone_detected)
        normalized_events.append(current_event)
        current_event = {
            "event_type": detection,
            "start_time": time_obj,
            "end_time": time_obj,
            "max_confidence": confidence,
            "status": "Confirmed" if confidence >= CONFIDENCE_THRESHOLD else "Uncertain"
        }

# Catch the last event if the video ends
if current_event:
    normalized_events.append(current_event)

# 4. Print the Results
print("✅ Normalized Events Result:")
print("-" * 50)
for event in normalized_events:
    duration = (event["end_time"] - event["start_time"]).total_seconds()
    print(f"Event: {event['event_type']:<15} | Duration: {duration}s | "
          f"Confidence: {event['max_confidence']} | Status: {event['status']}")
print("-" * 50)
print("Notice how 4 frames of 'looking_away' became 1 single event.")
print("Notice how 'phone_detected' was marked as 'Uncertain' due to low confidence.")