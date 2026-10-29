import os
import python_avatars as pa

avatar_dir = '../data/synthetic/avatars'
os.makedirs(avatar_dir, exist_ok=True)

print("🎨 Generating avatars locally...")

for i in range(1, 10001):
    # SKIP the first two students so we don't overwrite real photos!
    if i in [1, 2]:
        continue 

    roll_number = f"STU{i:05d}"
    filepath = os.path.join(avatar_dir, f"{roll_number}.svg")
    
    random_avatar = pa.Avatar.random()
    random_avatar.render(filepath)

print("✅ Avatars generated successfully (Skipped STU00001 and STU00002)!")