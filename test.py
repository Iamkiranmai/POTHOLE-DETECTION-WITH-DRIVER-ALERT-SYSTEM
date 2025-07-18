from ultralytics import YOLO
import cv2
import numpy as np
import pygame
import threading
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load model
model = YOLO("best.pt")
class_names = model.names
cap = cv2.VideoCapture('t.mp4')
count = 0
buzzer_file = "buzz.mp3"

# Detection parameters
CONFIDENCE_THRESHOLD = 0.5  # Only consider detections with confidence > 50%
NMS_THRESHOLD = 0.4  # Non-Maximum Suppression threshold
BUZZER_COOLDOWN = 2  # seconds between buzzer plays

# Load the sound file
try:
    buzzer_sound = pygame.mixer.Sound(buzzer_file)
    print("Successfully loaded buzzer sound file")
except Exception as e:
    print(f"Error loading sound file: {e}")

last_play_time = 0

def play_buzzer():
    try:
        print("Playing buzzer...")
        buzzer_sound.play()
    except Exception as e:
        print(f"Error playing buzzer: {e}")

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue

    img = cv2.resize(img, (1020, 500))
    results = model.predict(img, conf=CONFIDENCE_THRESHOLD, iou=NMS_THRESHOLD)
    
    pothole_detected = False

    for r in results:
        boxes = r.boxes
        for box in boxes:
            d = int(box.cls)
            c = class_names[d]
            conf = box.conf.item()
            
            if 'pothole' in c.lower() and conf > CONFIDENCE_THRESHOLD:
                pothole_detected = True
                print(f"Pothole detected with confidence: {conf:.2f}")
                
                # Draw bounding box
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(img, f"{c} {conf:.2f}", (x1, y1 - 10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    current_time = time.time()
    if pothole_detected and (current_time - last_play_time) > BUZZER_COOLDOWN:
        last_play_time = current_time
        buzzer_thread = threading.Thread(target=play_buzzer)
        buzzer_thread.start()
        print(f"Buzzer triggered at {time.ctime(current_time)}")
                 
    cv2.imshow('Pothole Detection', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()