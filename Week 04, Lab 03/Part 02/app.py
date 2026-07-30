from flask import Flask, request, jsonify
import joblib
import json
import numpy as np

app = Flask(__name__)

model = joblib.load('model_v3.joblib')

with open('model_metadata.json', 'r') as f:
    metadata = json.load(f)

@app.route('/models', methods=['GET'])
def get_models():
    return jsonify(metadata)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        probability = model.predict_proba(features)
        
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': probability.tolist()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
