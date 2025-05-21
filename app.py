from flask import Flask, request, jsonify
import os
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ✅ 首頁路由（Render 預設會打開 /，所以這段必加）
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

    # 模型邏輯之後會放這裡，現在先假裝完成
    return jsonify({
        'status': 'success',
        'filename': file.filename,
        'message': '圖片上傳成功！模擬排版已完成。'
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
