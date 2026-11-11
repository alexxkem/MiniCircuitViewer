# MiniCircuit AI Viewer

This is a simple web app I made using Python and Streamlit as part of my senior capstone project at VCU. The app uses a trained YOLO object detection model to identify and locate electrical components in circuit diagrams.

The main goal of this app was to make it easier to see how well our trained model could detect different electrical components in a circuit diagram.

## Features

- Allows users to upload circuit diagrams in PNG or JPG format.
- Uses a trained YOLO model to detect electrical components.
- Draws bounding boxes around the detected components.
- Displays the component names along with their confidence scores.
- Shows the original image and the image with the detected components.

## Technologies Used

- Python
- Streamlit
- YOLO (Ultralytics)
- Pillow
- NumPy

## How It Works

When a user uploads a circuit diagram, the app takes the image and passes it through our trained YOLO model.

The model then tries to identify the electrical components in the diagram and returns their locations along with a confidence score for each detection.

The app uses that information to draw bounding boxes around the components and displays the results so users can see what was detected.

## How to Run

1. Clone or download the repository.
2. Make sure Python is installed.
3. Install the required libraries using `pip install -r requirements.txt`.
4. Run the app using `streamlit run app.py`.
5. Upload a circuit diagram to see the detected components.

## About the Project

This app was part of my senior capstone project, where our team worked on identifying and locating electrical components in circuit diagrams using object detection.

My main contribution to the capstone was helping create circuit diagrams in AutoCAD and preparing images that could be used to train the model.

I also made this Streamlit app to test the trained model and display the detection results in a way that was easier to see.

## Demo

You can try the app here:

https://minicircuit.streamlit.app/

## What I Learned

This project helped me get more experience working with Python and Streamlit. I also learned how to use a trained object detection model in an application and display its results on an image.

It was also good practice working on a larger project with a team and seeing how different parts of a project come together.

Demo Screenshot:

Before:

![alt text](<Screenshot 2025-06-30 162255.png>) 



After:

![alt text](<Screenshot 2025-06-30 162259.png>)
