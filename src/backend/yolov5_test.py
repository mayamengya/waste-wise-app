import torch
import cv2
import numpy as np
from ultralytics import YOLO

def image_detection(file_name):
    """
    Perform object detection on the given image using YOLOv5 model.

    Args:
        file_name (str): The path to the image file to be processed.

    Returns:
        None: The function displays the image with bounding boxes and labels.
    """
    # Load the image from the given file path
    img = cv2.imread(file_name)

    resultFileName = 'savedImage.jpg'  # File to save the processed image (if needed)

    # Load YOLOv5 model and perform detection
    model = torch.hub.load('ultralytics/yolov5', 'yolov5n')  # Load YOLOv5 nano model
    result = model(img)  # Perform detection on the image
    print('Detection result:', result)

    # Convert detected result to a pandas DataFrame
    data_frame = result.pandas().xyxy[0]
    print('Detected objects DataFrame:')
    print(data_frame)

    # Loop through each detection result and draw bounding boxes
    for index in data_frame.index:
        # Get coordinates of the bounding box
        x1 = int(data_frame['xmin'][index])
        y1 = int(data_frame['ymin'][index])
        x2 = int(data_frame['xmax'][index])
        y2 = int(data_frame['ymax'][index])

        # Get label and confidence score
        label = data_frame['name'][index]
        confidence = data_frame['confidence'][index]
        text = f"{label} {confidence:.2f}"  # Format the text with label and confidence

        # Draw the bounding box and label on the image
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 0), 2)
        cv2.putText(img, text, (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

    # Display the processed image with bounding boxes and labels
    cv2.imshow('Detected Image', img)
    cv2.waitKey(0)  # Wait for a key press to close the image window

# Call the function with a test image
image_detection('tests/nike-basketball.jpg')