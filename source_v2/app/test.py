import pickle
import feature_extractor as fe

def predict_phishing_forest(features):
    # Load the model
    with open('../RandomForestClassifier.pickle.dat', 'rb') as f:
        forest_model = pickle.load(f)

    # Make predictions
    prediction = forest_model.predict([features])

    return prediction[0]

def predict_phishing_xgb(features):
    # Load the model
    with open('../XGBoostClassifier.pickle.dat', 'rb') as f:
        xgb_model = pickle.load(f)

    # Make predictions
    prediction = xgb_model.predict([features])

    return prediction[0]


def main():
    features = fe.extract_features('https://elit.tdtu.edu.vn/login?url=/courses/')
    features = features[1:-1]
    print(features)

    prediction_forest = predict_phishing_forest(features)
    prediction_xgb = predict_phishing_xgb(features)
    print("prediction_forest",prediction_forest)
    print("prediction_xgb",prediction_xgb)

    # if prediction == 0:
    #     print("Predicting made:")
    #     print("No Phishing Detected. This URL seems safe.")
    # else:
    #     print("Prediction made:")
    #     print("Phishing Alert! This URL is classified as phishing.")


if __name__ == "__main__":
    main()