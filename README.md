# 👗 YOLOv8 Fashion Detector Web App

## 📌 Project Description

This project aims to build a web application capable of detecting fashion objects in street-style images using the YOLOv8 deep learning model. The model was trained on the Colorful Fashion Dataset from Kaggle (https://www.kaggle.com/datasets/nguyngiabol/colorful-fashion-dataset-for-object-detection), which includes 10 fashion object classes: sunglasses, hat, jacket, shirt, pants, shorts, skirt, dress, bag, and shoes.

The training was conducted over 20 epochs with a fixed batch size, resulting in good performance with a mAP@0.5 score of 0.799. The web application was developed using the Flask framework for the backend, allowing users to upload images, process them through the model, and display the detection results with bounding boxes and classification labels.

## Training
- Model: YOLOv8  
- Epochs: 20  
- Performance:
  - **mAP@0.5**: `0.799`
  - **mAP@0.5:0.95**: `0.554`
  - **mAP@0.75**: `0.602`

## Web Application
The web app is developed using the **Flask** framework for the backend. It allows users to:

1. Upload an image.
2. Process the image using the trained YOLOv8 model.
3. View the detection results with bounding boxes and classification labels.


## How to Run Project

1. Clone this repository.
2. Install the dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
4. Run the project:
   
   ```bash
   python app.py
   
