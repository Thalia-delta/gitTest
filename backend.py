from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import base64
import io
from PIL import Image
import json
import os

# 配置大文件支持
app = Flask(__name__, static_folder='.', static_url_path='')
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB
app.config['JSON_AS_ASCII'] = False  # 支持中文

# 保持其他代码不变

# app = Flask(__name__, static_folder='.', static_url_path='')
# 保持CORS配置以便兼容其他可能的前端访问
CORS(app, resources={r"/*": {
    "origins": ["*"],
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})

# 根路径返回主页面
@app.route('/', methods=['GET'])
def home():
    return send_from_directory('.', 'index.html')

# 静态文件服务
@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    return send_from_directory('.', path)

# 模拟多模态大模型分析函数
def analyze_with_multimodal_model(photo_data):
    # 这里是示例实现，实际需要调用真实的多模态大模型API
    # 示例数据结构
    result = {
        "travel_path": [
            {
                "location": "北京",
                "description": "中国的首都，拥有悠久的历史和丰富的文化遗产",
                "representative_photo_index": 0,
                "photos": [0, 1, 2]
            },
            {
                "location": "上海",
                "description": "中国的经济中心，现代化的国际大都市",
                "representative_photo_index": 3,
                "photos": [3, 4, 5]
            },
            {
                "location": "杭州",
                "description": "美丽的江南水乡，西湖风光闻名天下",
                "representative_photo_index": 6,
                "photos": [6, 7]
            }
        ],
        "total_locations": 3,
        "total_photos": len(photo_data)
    }
    return result

@app.route('/analyze-photos', methods=['POST'])
def analyze_photos():
    try:
        # 获取请求中的照片数据
        photo_data = request.json
        
        # 调用多模态大模型进行分析
        analysis_result = analyze_with_multimodal_model(photo_data)
        
        # 返回分析结果
        return jsonify({
            "success": True,
            "data": analysis_result
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)