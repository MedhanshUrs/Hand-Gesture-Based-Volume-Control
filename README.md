# Hand-Gesture-Based Volume Control

This project implements a real-time hand gesture–based volume control system using computer vision and Python. The system detects hand movements through a webcam and adjusts the computer’s audio volume based on the distance between the thumb and index finger.

The project uses:

* OpenCV for video processing
* MediaPipe for hand tracking
* NumPy and Math for calculations
* AppleScript (`osascript`) for controlling system volume on macOS

## Features

* Real-time hand detection
* Dynamic system volume adjustment
* Gesture-based interaction
* Visual volume bar feedback
* Webcam-based control without external hardware

## Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

## How It Works

* The webcam captures live video.
* MediaPipe detects hand landmarks.
* The distance between the thumb and index finger is calculated.
* The distance is mapped to a volume range (0–100).
* System volume is updated dynamically.

## Installation

```bash id="hg1"
pip install opencv-python mediapipe numpy
```

## Run the Project

```bash id="hg2"
python main.py
```

## Controls

* Move thumb and index finger closer → Lower volume
* Move thumb and index finger farther apart → Increase volume
* Press `q` to quit

## Note

This implementation uses `osascript` and is designed for macOS systems.

## Report

The detailed project report is included in this repository.
