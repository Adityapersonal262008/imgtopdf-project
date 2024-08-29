from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('files[]')
    images = []
    for file in files:
        if file and file.filename.split('.')[-1].lower() in ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif']:
            img = Image.open(file)
            img = img.convert('RGB')
            images.append(img)
    
    if images:
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.pdf')
        images[0].save(pdf_path, save_all=True, append_images=images[1:], quality=100)
        return send_file(pdf_path, as_attachment=True)
    
    return "No valid images uploaded", 400

if __name__ == "__main__":
    app.run(debug=True)
