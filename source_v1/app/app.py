from flask import Flask, render_template, request, jsonify
import pickle
import feature_extractor as fe

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    model = data['model']

    features = fe.extract_features(url)

    if features is None:
        return jsonify({'error': 'Failed to extract features from the URL', 'model': model}), 400

    features = features[1:-1]

    prediction = None
    msg = None
    model_type = model

    if model == 'GBM':
        prediction = predict_phishing_gbm(features)
    elif model == 'XGB':
        prediction = predict_phishing_xgb(features)

    if prediction == 0:
        msg = 'The URL seem to be safe!'
    else:
        msg = 'The URL may be a phishing site!'

    return jsonify({'prediction': int(prediction), 'msg': msg, 'model': model_type, 'domain_age': features[-3], 'google_index': features[-2], 'page_rank': features[-1]})

def predict_phishing_gbm(features):
    # Load the model
    with open('../models/GBM.pickle.dat', 'rb') as f:
        gbm_model = pickle.load(f)
    # Make predictions
    prediction = gbm_model.predict([features])
    return prediction[0]

def predict_phishing_xgb(features):
    # Load the model
    with open('../models/XGB.pickle.dat', 'rb') as f:
        xgb_model = pickle.load(f)
    # Make predictions
    prediction = xgb_model.predict([features])
    return prediction[0]

if __name__ == '__main__':
    app.run(debug=True)