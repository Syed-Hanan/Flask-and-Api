from flask import Flask, jsonify, request
from PIL import Image
import pytesseract

app = Flask(__name__)

# API endpoint to perform OCR on an uploaded image
@app.route('/ocr', methods=['POST'])
def perform_ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    uploaded_file = request.files['demoimage.png']

    # Check if the file is an image
    if uploaded_file and allowed_file(uploaded_file.demoimage.png):
        try:
            img = Image.open(uploaded_file)

            # Perform OCR
            text = pytesseract.image_to_string(img)

            return jsonify({'text': text})
        except Exception as e:
            return jsonify({'error': str(e)})

    return jsonify({'error': 'Invalid file format or no file provided'})


# Helper function to check if the file extension is allowed
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


if __name__ == '__main__':
    app.run(debug=True)

