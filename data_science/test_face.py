from deepface import DeepFace

print("🔍 Starting Face Matching Validation with DeepFace...\n")

# 1. Correct File Paths
registered_photo = "../data/synthetic/avatars/STU00001.png" 
live_photo = "test.png"  # Make sure this is the exact name

try:
    # 2. Use ArcFace - it is the best model for different lighting
    result = DeepFace.verify(
        img1_path = registered_photo,
        img2_path = live_photo,
        model_name = "ArcFace", 
        enforce_detection = False 
    )

    distance = result["distance"]
    is_match = result["verified"]
    threshold = result["threshold"]
    
    # 3. A better confidence formula
    # If distance is 0, confidence is 100%. If distance is threshold, confidence is 50%.
    confidence_score = round(max(0, (1 - (distance / (threshold * 2))) * 100), 2)
    
    print(f"📊 Distance: {round(distance, 4)} (Threshold: {round(threshold, 4)})")
    print(f"✅ Match Status: {'MATCHED' if is_match else 'NO MATCH'}")
    print(f"🎯 Confidence Score: {confidence_score}%")

    # 4. Accept if confidence is above 50% (Industry standard for cameras)
    if is_match and confidence_score >= 60:
        print("🟢 VALIDATION PASSED: The photo matches the student.")
    else:
        print("🔴 VALIDATION FAILED: The photo does not match the student.")

except Exception as e:
    print(f"❌ Error during verification: {e}")
    print("Make sure 'test_live.jpg' is in the data_science folder and shows your face clearly.")