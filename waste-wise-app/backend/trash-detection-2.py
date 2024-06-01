# remember to add this file to git
import torch
import cv2
import numpy as np
import io
import os
import supervision as sv
from ultralytics import YOLO
import json


def make_unique_json_file(directory, file_name):
    """
    Create a JSON file with a unique name in the specified directory.
    If a file with the same name already exists,
    append a number to the file name to make it unique.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_base, file_ext = os.path.splitext(file_name)
    i = 1
    while True:
        new_file_name = f"{file_base}_{i}{file_ext}"
        new_file_path = os.path.join(directory, new_file_name)
        if not os.path.exists(new_file_path):
            return new_file_path
        i += 1


def image_detection(file_name):
    """
        Analyzes image for trash, copies the image and surrounds the highlighted trash with marker and prediction confidence
        then shows the image onscreen.

        :param file_name: Name of image file that you would like to analyze for trash (use .jpg in the same directory)
        :return: A json file with the prediction's class, coordinates and confidence. e.g. ({'predictions':
         [{'x': 388, 'y': 262, 'width': 758, 'height': 475, 'confidence': 0.4060649871826172,
        'class': 'garbage', 'class_id': 0, 'detection_id': 'c58b895d-6ecc-4a4d-9570-9103a5ae8ee8',
        'image_path': 'trash_image_7.jpg', 'prediction_type': 'ObjectDetectionModel'}],
        'image': {'width': '800', 'height': '500'}}
    """
    # img = cv2.imread(file_name)

    # train model for trash detection on custom dataset
    # model =  YOLO('yolov8m.pt')

    # Train the model
    # results = model.train(data='garbage_classification/trash.yaml')

    # Load a model
    model = YOLO('model/best (8).pt')  # load a model from dataset

    result = model.predict(file_name, save=True, show=True)

    input()

    # Store Json Results
    results = json.loads(result[0].tojson())

    # Print Json (If you want to view json results)
    # print(results)

    # Write results in a file
    with open(make_unique_json_file('outputs', 'output.json'), 'w') as results_write_json:
        json.dump(results, results_write_json)

    # print('result: ', result)
    return result


print(image_detection('static/trash_image_40.jpg'))





