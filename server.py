from flask import Flask, request, jsonify
from emotion_app.emotion_predictor import emotion_predictor

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "Text input is required"}), 400
    result = emotion_predictor(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)