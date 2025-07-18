# POTHOLE-DETECTION-WITH-DRIVER-ALERT-SYSTEM
Pothole Detection with Driver Alert System
This project implements a real-time pothole detection system using YOLOv8 with instance segmentation and provides an alert mechanism through a buzzer when potholes are identified. It is aimed at improving road safety by helping drivers avoid potholes, thereby reducing the risk of accidents and vehicle damage.

Features
Accurate pothole detection using YOLOv8 segmentation.

Custom-trained model on a manually annotated dataset.

Real-time video analysis using OpenCV.

Audio alert system (buzzer) triggered on pothole detection.

Efficient filtering of false detections based on confidence, area, and shape.

Project Overview
Dataset Preparation

Extracted frames from a recorded road video (p.mp4).

Annotated potholes using Roboflow’s polygon tool.

Exported dataset in YOLOv8 format.

Model Training

Trained the YOLOv8 segmentation model using Google Colab with GPU acceleration.

Saved the trained model (best.pt) after 50+ epochs of training.

Real-Time Detection with Alert

Developed test.py script to:

Load video frame-by-frame.

Run model predictions.

Validate detections.

Display results and trigger buzzer alert using threading.

Technologies Used
Technology	Purpose
YOLOv8	Instance segmentation for object detection
OpenCV	Video frame processing and visualization
PyTorch	Underlying framework for YOLOv8
Roboflow	Dataset annotation and export
Python	Core development language

Files in the Repository
bash
Copy
Edit
├── best.pt                 # Trained model
├── p.mp4                  # Test video
├── buzz.mp3               # Buzzer alert sound
├── test.py                # Main detection and alert script
├── yolov8_training.ipynb  # Training notebook (Google Colab)
└── README.md              # Project documentation
How to Run
Clone the repository:
gh repo clone deekshitha68/POTHOLE-DETECTION-WITH-DRIVER-ALERT-SYSTEM 
cd pothole-detection-alert
Install dependencies:
pip install ultralytics opencv-python numpy
Ensure the following files are in the same folder:

best.pt (trained model)

p.mp4 (input video)

buzz.mp3 (alert sound)

Run the detection:

python test.py
Press q to stop the video display.

Output
The system will display the video with potholes highlighted.
<img width="1007" height="524" alt="Screenshot 2025-07-18 at 10 53 54 AM" src="https://github.com/user-attachments/assets/bd63ad59-d11b-4e01-868e-ac06ae1225bb" />

If a pothole is detected and validated, a buzzer sound will be played.

Detection is real-time with visual and audio feedback.

Possible Extensions
Integrate with live camera feed (e.g., mounted on a vehicle).

Deploy on Raspberry Pi or NVIDIA Jetson for field use.

Add GPS location logging of detected potholes.

Send alerts to road maintenance authorities or cloud dashboards.
