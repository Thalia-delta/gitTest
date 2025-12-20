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

# 处理favicon.ico请求
@app.route('/favicon.ico', methods=['GET'])
def favicon():
    # 返回204 No Content状态码，避免404错误
    return '', 204

# 静态文件服务
@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    return send_from_directory('.', path)

# 模拟多模态大模型分析函数
def analyze_with_multimodal_model(photo_data):
    # 这里是示例实现，实际需要调用真实的多模态大模型API
    # 修改后的数据结构，添加时间和坐标信息以支持地图显示
    result = {
        "album_name": "我的京沪杭之旅",  # 相册名称
        "album_description": "一次跨越中国三大城市的难忘旅行，记录了历史文化与现代都市的完美融合",  # 相册整体描述
        "travel_path": [
            {
                "location": "北京",
                "description": "中国的首都，拥有悠久的历史和丰富的文化遗产",
                "representative_photo_index": 0,
                "photos": [0, 1, 2],
                "timestamp": "2025-12-15T10:00:00",  # 添加时间戳
                "coordinates": {"lat": 39.9042, "lng": 116.4074},  # 添加经纬度坐标
                # 添加三种描述类型
                "descriptions": {
                    "minimal": "北京 · 故宫游览",  # 极简回忆
                    "story": "在北京的第一天，我参观了世界上最大的古代宫殿建筑群——故宫。红墙黄瓦间，仿佛穿越回了明清时代，每一处建筑都诉说着历史的沧桑与辉煌。",  # 故事叙述
                    "social": "🏯 北京故宫打卡！红砖黄瓦，尽显皇家风范原来历史课本里的故宫真的这么震撼～",  # 社交分享版
                }
            },
            {
                "location": "上海",
                "description": "中国的经济中心，现代化的国际大都市",
                "representative_photo_index": 1,
                "photos": [1, 4, 5],
                "timestamp": "2025-12-16T14:30:00",  # 添加时间戳
                "coordinates": {"lat": 31.2304, "lng": 121.4737},  # 添加经纬度坐标
                # 添加三种描述类型
                "descriptions": {
                    "minimal": "上海 · 外滩夜景",  # 极简回忆
                    "story": "来到上海，外滩的夜景让我震撼。黄浦江两岸，一边是充满历史感的万国建筑博览群，一边是现代化的陆家嘴金融中心，仿佛在时光隧道中穿梭。",  # 故事叙述
                    "social": "🌃 上海外滩夜景绝了！一边是百年建筑，一边是摩天大楼黄浦江的晚风里都是魔都的魅力～",# 社交分享版
                }
            },
            {
                "location": "杭州",
                "description": "美丽的江南水乡，西湖风光闻名天下",
                "representative_photo_index": 2,
                "photos": [2, 7],
                "timestamp": "2025-12-17T09:15:00",  # 添加时间戳
                "coordinates": {"lat": 30.2741, "lng": 120.1551},  # 添加经纬度坐标
                # 添加三种描述类型
                "descriptions": {
                    "minimal": "杭州 · 西湖漫步",  # 极简回忆
                    "story": "杭州西湖果然名不虚传。漫步苏堤，微风拂面，远处的雷峰塔若隐若现。“欲把西湖比西子，淡妆浓抹总相宜“，古人诚不我欺。",  # 故事叙述
                    "social": "🌿 杭州西湖太治愈了！苏堤春晓，柳浪闻莺原来真的有地方能让时间慢下来～",# 社交分享版
                }
            }
        ],
        "selected_photos": [0, 1, 2, 3, 4, 5, 6, 7],  # 添加筛选出的照片序号
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