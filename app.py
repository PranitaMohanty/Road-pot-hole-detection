import cv2
import numpy as np
import torch
#import torchvision.transforms as transforms
from ultralytics import YOLO

# Load YOLO model for pothole and crack detection
model = YOLO(r'C:\Users\Pranita\Desktop\aiml\road pathholes\yolov8n.pt')
# Pre-trained YOLOv8 model (or train your own for pothole detection)

# Function to detect damaged roads (potholes, cracks)
def detect_damaged_road(frame):
    results = model(frame)
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()  # Get bounding boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, "Pothole/Crack", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    return frame

# Function to detect lanes using OpenCV
def detect_lanes(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=100, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
    return frame

# Open video capture (0 for webcam, or provide video path)
cap = cv2.VideoCapture(0)  # Change to video file path if needed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = detect_damaged_road(frame)
    frame = detect_lanes(frame)
    
    cv2.imshow("AI Car: Road and Lane Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
