import cv2
import numpy as np
import os
import random

# 1. Setup folder
video_dir = '../data/synthetic/videos'
os.makedirs(video_dir, exist_ok=True)

print("🎥 Generating synthetic live exam videos for 10,000 students...")
print("This might take 10-15 minutes. Please wait...")

width, height = 320, 240 # Smaller resolution for faster generation
fps = 10
total_frames = 10 # Just 1 second video per student

for i in range(1, 10001):
    roll_number = f"STU{i:05d}"
    video_path = os.path.join(video_dir, f"{roll_number}_live.mp4")
    
    # Skip if video already exists (saves time if you run it again)
    if os.path.exists(video_path):
        continue

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_path, fourcc, fps, (width, height))
    
    # 10% of students have cheating behavior
    has_cheating = random.random() < 0.10 
    
    for frame_num in range(total_frames):
        frame = np.full((height, width, 3), 50, dtype=np.uint8)
        center_x = width // 2
        center_y = height // 2
        
        if has_cheating and frame_num > 5:
            center_x += random.randint(-50, 50)
            
        cv2.circle(frame, (center_x, center_y), 40, (200, 200, 200), -1)
        cv2.putText(frame, f"{roll_number}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        out.write(frame)
        
    out.release()
    
    # Print progress every 1000 videos
    if i % 1000 == 0:
        print(f"✅ Generated {i}/10000 videos...")

print(f"\n🎉 Successfully generated 10,000 synthetic videos!")