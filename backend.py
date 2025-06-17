# Flask 示例：proxy_api.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'sk-8d42eb4e57c64f41b1f4e6633cf6db4a'

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("question")
    url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
    payload = {
        "model": "qwen-turbo",
        "input": { "prompt": user_input },
        "parameters": { "temperature": 0.7 }
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
