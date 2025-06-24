from flask import Flask, render_template, request
import os
from ultralytics import YOLO
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = YOLO('best.pt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            original_filename = str(uuid.uuid4()) + "_original.jpg"
            original_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
            image_file.save(original_path)

            detected_filename = str(uuid.uuid4()) + ".jpg"
            detected_path = os.path.join(app.config['UPLOAD_FOLDER'], detected_filename)

            results = model(original_path)
            results[0].save(filename=detected_path)

            return render_template('index.html',
                                   image_path=detected_path,
                                   original_image_path=original_path)

    return render_template('index.html', image_path=None, original_image_path=None)

if __name__ == '__main__':
    app.run(debug=True)
