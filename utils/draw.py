from PIL import ImageDraw, ImageFont

#Function that draws the box around the components
def draw_boxes(image, detections):
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    for det in detections:
        box = det["bbox"]
        label = det["label"]
        score = det["score"]
        text = f"{label} ({score:.2f})"

        draw.rectangle(box, outline="red", width=2)
        draw.text((box[0], box[1] - 10), text, fill="red", font=font)
    return image
