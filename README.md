# 👗 YOLOv8 Fashion Detector Web App

## 📌 Project Description

This project aims to build a web application capable of detecting fashion objects in street-style images using the YOLOv8 deep learning model. The model was trained on the Colorful Fashion Dataset from Kaggle, which includes 10 fashion object classes: sunglasses, hat, jacket, shirt, pants, shorts, skirt, dress, bag, and shoes.

The training was conducted over 20 epochs with a fixed batch size, resulting in good performance with a mAP@0.5 score of 0.799. The web application was developed using the Flask framework for the backend, allowing users to upload images, process them through the model, and display the detection results with bounding boxes and classification labels**.

---

## 🚀 Run the Project

Pastikan Python sudah terinstal. Jalankan perintah berikut di terminal:

```bash
python app.py
