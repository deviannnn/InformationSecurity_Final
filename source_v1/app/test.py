import pickle
import feature_extractor as fe
import pandas as pd

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

def main():
    features = fe.extract_features('https://stdportal.tdtu.edu.vn/Login/Index?ReturnUrl=https%3A%2F%2Fstdportal.tdtu.edu.vn%2F')
    features = features[1:-1]

    result_XGB = predict_phishing_xgb(features)
    result_GBM = predict_phishing_gbm(features)

    print("result_XGB: ", result_XGB)
    print("result_GBM: ", result_GBM)


def add_data():
    data = [('https://thuvienpdf.com/#gsc.tab=0', 0),
            ('https://www.phishtank.com/developer_info.php', 0),
            ('https://docs.nestjs.com/controllers', 0),
            ('https://vercel.com/templates/next.js?utm_source=next-site&utm_medium=navbar&utm_campaign=next_site_nav_templates', 0),
            ('https://nextjs.org/showcase', 0),
            ('https://drawsql.app/diagrams', 0),
            ('https://demos.creative-tim.com/soft-ui-dashboard-pro/pages/pages/users/new-user.html', 0),
            ('https://www.npmjs.com/package/jsbarcode', 0),
            ('https://hackertarget.com/top-million-site-list-download/', 0),
            ('https://stdportal.tdtu.edu.vn/Login/Index?ReturnUrl=https%3A%2F%2Fstdportal.tdtu.edu.vn%2F', 0),
            ('https://elearning.tdtu.edu.vn/course/', 0)]

    extend_cases = []

    for urls, label in data:
        case = fe.extract_features(urls, label)
        print(case)
        if case is None:
            continue
        extend_cases.append(case)


    df = pd.DataFrame(extend_cases)
    df.to_csv('datasets/additional_dataset.csv', index=False)

if __name__ == "__main__":
    main()