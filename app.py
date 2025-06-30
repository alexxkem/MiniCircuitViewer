import streamlit as st
from PIL import Image
import numpy as np
from ultralytics import YOLO
from utils.draw import draw_boxes


st.title("MiniCircuit AI Viewer")

#Import the model 
model = YOLO("best.pt")


#Upload an image
uploaded_file = st.file_uploader("Upload a Circuit Diagram", type=["png", "jpg", "jpeg"])

#If there is an image upload it toe streamlit
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    #Convert to numpy array and run model
    image_np = np.array(image)
    with st.spinner("Running detection..."):
        results = model.predict(image_np, conf=0.3)

    #Extracts the boxes and labels
    detections = []
    for r in results:
        for box in r.boxes:
            xyxy = box.xyxy[0].tolist()
            label = int(box.cls[0].item())
            score = float(box.conf[0].item())
            name = model.names[label]
            detections.append({
                "label": name,
                "score": score,
                "bbox": [int(xyxy[0]), int(xyxy[1]), int(xyxy[2]), int(xyxy[3])]
            })

    #Draw a box with annotated Boxes around the component with confidence score
    annotated_image = draw_boxes(image.copy(), detections)
    st.image(annotated_image, caption="Detected Components", use_container_width=True)


