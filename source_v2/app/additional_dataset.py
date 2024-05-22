import feature_extractor as fe
import pandas as pd

def main():
    data_phishing_urls = pd.read_csv("../datasets/phishing_urls_test.csv")
    data_legit_urls = pd.read_csv("../datasets/legit_urls_test.csv")

    extend_cases = []

    for index, row in data_phishing_urls.iterrows():
        urls = row['URLs']
        label = row['label']
        case = fe.extract_features(urls, label)
        print(case)
        if case is None:
            continue
        extend_cases.append(case)

    for index, row in data_legit_urls.iterrows():
        urls = row['URLs']
        label = row['label']
        case = fe.extract_features(urls, label)
        print(case)
        if case is None:
            continue
        extend_cases.append(case)


    df = pd.DataFrame(extend_cases)
    df.to_csv('additional_dataset.csv', index=False)

    
if __name__ == "__main__":
    main()