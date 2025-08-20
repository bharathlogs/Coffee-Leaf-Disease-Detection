🌱 Coffee Leaf Disease Detection using YOLO
📌 Project Overview

Coffee is a critical agricultural crop and economic driver for many developing nations. However, coffee production is frequently affected by leaf diseases such as:

Coffee Leaf Rust

Cercospora Leaf Spot

Phoma Leaf Spot

Leaf Miner Damage

These diseases drastically reduce crop yield and quality, causing financial losses for farmers and disrupting global coffee supply chains.

Traditional disease detection relies on manual eye-based inspection, which is slow, inconsistent, and hard to scale.
To overcome these challenges, this project presents an AI-powered detection system based on YOLO (You Only Look Once), a state-of-the-art deep learning object detection framework.

🚀 Key Features

Automated Detection → Identifies healthy vs. diseased coffee leaves in real-time.

YOLO Deep Learning Model → Robust performance in complex backgrounds.

Data Augmentation → Techniques like rotation, zooming, flipping, and brightness adjustments enhance model generalization.

Pesticide Recommendation Engine → Suggests suitable pesticides based on detected disease for targeted intervention.

Eco-Friendly Farming → Reduces pesticide overuse and promotes sustainable agricultural practices.

High Accuracy & Reliability → Validated with excellent accuracy, precision, and recall.

🛠️ Tech Stack

Programming Language: Python 3.8 – 3.10

Deep Learning Framework: PyTorch / YOLOv5

Computer Vision: OpenCV

Dataset Handling & Augmentation: Torchvision, Albumentations

Visualization: Matplotlib, Seaborn

Notifications (optional): Twilio (SMS), SendGrid (Email)

📂 Dataset

Coffee leaf dataset with healthy and diseased classes.

Images curated and annotated for YOLO training.

Includes augmentation to improve robustness in varied field conditions.

(Dataset link or instructions for preparation should be added here by you.)

⚙️ System Workflow

Image Acquisition → Coffee leaf images captured via camera.

Preprocessing → Resize, normalize, augment data.

Training → Train YOLO model on annotated dataset.

Inference → Real-time detection of coffee leaf diseases.

Recommendation → Suggests suitable pesticide interventions.

📊 Results

High accuracy, precision, and recall across multiple disease classes.

Robust detection in real-world conditions (lighting changes, occlusions, leaf damage).

Demonstrated effectiveness for real-time agricultural applications.
