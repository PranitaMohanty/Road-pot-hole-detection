 🚗 Real-time pothole detection from road images and videos

🧠 Overview

This project uses **YOLOv8**, a state-of-the-art object detection model, to automatically identify potholes on roads from images or video feeds. It aims to support smart road monitoring and maintenance by enabling fast, accurate, and automated pothole detection.


 🧰 Tech Stack

* **Model:** YOLOv8 (Ultralytics)
* **Language:** Python
* **Libraries:** OpenCV, Torch, Ultralytics, NumPy, Matplotlib
* **Deployment:** Streamlit / Gradio (optional)

 ⚙️ Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/pothole-detection-yolov8.git
cd pothole-detection-yolov8
```

2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

 3️⃣ Download YOLOv8 weights

```bash
yolo detect predict model=yolov8n.pt
```



🚀 Usage

🔹 Run detection on images or videos

```bash
yolo detect predict model=best.pt source='road_images/' save=True
```

 🔹 For live webcam detection

```bash
yolo detect predict model=best.pt source=0
```



 📊 Results

| Metric    | Value |
| --------- | ----- |
| Precision | 0.90  |
| Recall    | 0.87  |
| mAP@0.5   | 0.89  |

Sample Output:
![Output](assets/pothole_output.jpg)



 📂 Folder Structure

```
pothole-detection-yolov8/
│
├── data/
│   ├── images/
│   ├── labels/
│   └── pothole.yaml
│
├── models/
│   └── best.pt
│
├── src/
│   ├── train.py
│   └── detect.py
│
├── requirements.txt
└── README.md
```



 🪪 License

This project is licensed under the **MIT License**.



