from flask import Flask, request, render_template, jsonify, url_for
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import os
import io
from PIL import Image
import numpy as np
import urllib.request
import base64

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def run_model(file_path):
    model = YOLO('model/best.pt')
    results = model.predict(file_path)

    # Get numpy array of the result
    result_array = results[0].plot()

    # Convert numpy array to PIL Image
    result_image = Image.fromarray(result_array)

    # Save to a BytesIO object
    img_io = io.BytesIO()
    result_image.save(img_io, 'JPEG')
    img_io.seek(0)

    # Encode image in base64
    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

    return img_base64, results[0].tojson()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run-detection', methods=['POST'])
def run_detection():
    if 'image' in request.files:
        file = request.files['image']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        img_base64, json_results = run_model(filepath)
        return jsonify({'image': img_base64, 'json_results': json_results})
    elif 'image_url' in request.form:
        image_url = request.form['image_url']
        filename = os.path.basename(image_url)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        urllib.request.urlretrieve(request.url_root + image_url, filepath)
        img_base64, json_results = run_model(filepath)
        return jsonify({'image': img_base64, 'json_results': json_results})
    else:
        return "No image uploaded", 400


if __name__ == '__main__':
    app.run(debug=True)