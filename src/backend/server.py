from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from PIL import Image
from PIL.ExifTags import TAGS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_location_data(file_path):
    """
    Extracts location data (latitude and longitude) from an image file using its EXIF data.

    Parameters:
    - file_path (str): The path to the image file.

    Returns:
    dict: A dictionary containing the extracted location data.
    """
    try:
        # Open the image file
        image = Image.open(file_path)

        # Extract EXIF data
        exif_data = image._getexif()

        # Extract GPS data if available
        gps_info = exif_data.get(34853, None)

        if gps_info:
            # Convert GPS coordinates to decimal format
            lat, lon = convert_gps_coordinates(gps_info)
            print(f"Extracted location data: Latitude={lat}, Longitude={lon}")
            return {'latitude': lat, 'longitude': lon}
        else:
            print("No GPS data available in the image")
            return {'message': 'No GPS data available in the image'}
    except Exception as e:
        print(f"Error extracting location data: {str(e)}")
        return {'error': str(e)}
    
def convert_gps_coordinates(gps_info):
    """
    Converts GPS coordinates from degrees, minutes, and seconds to decimal format.

    Parameters:
    - gps_info (tuple): Tuple containing GPS information in the form (degrees, minutes, seconds, direction).

    Returns:
    tuple: A tuple containing the converted latitude and longitude in decimal format.
    """
    try:
        lat_deg, lat_min, lat_sec = gps_info[2]
        lon_deg, lon_min, lon_sec = gps_info[4]

        lat = lat_deg + lat_min / 60.0 + lat_sec / 3600.0
        lon = lon_deg + lon_min / 60.0 + lon_sec / 3600.0

        # if gps_info[3] == 'S':
        #     lat = -lat
        # if gps_info[1] == 'W':
        #     lon = -lon

        lon = -lon
        
        print(f"Converted GPS coordinates: Latitude={lat}, Longitude={lon}")
        return lat, lon
    except Exception as e:
        print(f"Error converting GPS coordinates: {str(e)}")
        return None, None


@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handles the file upload process.

    This function receives an uploaded file, saves it to the specified folder, and extracts location data
    from the image using the extract_location_data function. The extracted location data is included in the
    JSON response.

    Returns:
    jsonify: A JSON response containing a success message and extracted location data if available,
             or an error message in case of an exception.
    """
    try:
        uploaded_file = request.files['file']

        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(file_path)

        location_data = extract_location_data(file_path)

        return jsonify({'message': 'File uploaded successfully', 'location_data': location_data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)