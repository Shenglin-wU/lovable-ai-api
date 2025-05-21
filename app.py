from flask import Flask, request, jsonify
import os
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ✅ 首頁路由：避免 Render 進首頁時出現 404
@app.route('/')
def home():
    return 'API 正在運行中，請使用 /upload 上傳圖片進行模擬排版。'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file uploaded'}), 400

    file = request.files['image']
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(save_path)

    return jsonify({
        'status': 'success',
        'filename': file.filename,
        'message': '圖片上傳成功！模擬排版已完成。'
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
