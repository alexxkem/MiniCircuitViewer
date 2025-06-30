# MiniCircuit AI Viewer

A web app that is built with Streamlit to detect and label electrical components in a circuit diagram using a custom-trained YOLOv8 model.

How it works:
1. Upload a circuit diagram (JPG/PNG)
2. The app uses a trained object detection model ("best.pt") in order to identify components
3. It draws a bounding boxes and labels and gives a confidence rating on what the component might be, directly on the image.

Why:
This project was apart of my Senior Capstone class, where I helped create the circuit diagrams in-order to train the AI-based detection system.

Demo Screenshot:

Before:

![alt text](<Screenshot 2025-06-30 162255.png>) 



After:

![alt text](<Screenshot 2025-06-30 162259.png>)