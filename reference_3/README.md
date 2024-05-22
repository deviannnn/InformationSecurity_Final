
# Phishing Website Classifier

The code was also uploaded to kaggle:

[/aster-fung/phishing_website_detection_random_forest_96%+](https://www.kaggle.com/code/asterfung/phishing-website-detection-random-forest-96)

## Background:

From small retail commerce to stock trades -  most of our lives are connected to the internet, which is reflected in the traction gained in the usage of e-commerce platforms including digital wallets, Paypal and credit cards. The substantial growth of e-commerce attracts fraudsters and identify theives. Among various hacking techniques, phishing remains the more common and effective way to hack into virtually any person’s/organization’s asset account. As phishing tactics are evolving, phishing detection methods must be co-evoluting as well to avoid asset loss. Machine learning is widely recognized for phishing webpage detection. 

In previous study by Hannousse & Yahiouche, the research team has built a dataset containing both legitimate and phishing URLs, from which they have selected 87 features that have potential for phishing. The aim was to build dataset that when machine learning models are built upon, the models are generalised to detecting emerging phishing web pages. 

## The Dataset 
[Web page Phishing Detection Dataset ](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset)

The provided dataset includes 11430 URLs with 87 extracted features. The dataset is designed to be used as benchmarks for machine learning-based phishing detection systems. Features are from three different classes: 56 extracted from the structure and syntax of URLs, 24 extracted from the content of their correspondent pages, and 7 are extracted by querying external services. The dataset is balanced, it contains exactly 50% phishing and 50% legitimate URLs.

## The Model
- A machine learning model based on random forest classifier ensemble was built based on 23 selected features using scikit-learn was trained with a testing accuracy of 96.5%
- Correlation matrix of features was calculated for feature selection. The correlation matrix was visualised using seaborn heatmap. 

## Acknowledgements and References

 - [Towards Benchmark Datasets For Machine Learning Based Website Phishing Detection: An Experimental Study,](https://arxiv.org/abs/2010.12847)
 - [Web page Phishing Detection Dataset ](https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset)

## License

[MIT](https://choosealicense.com/licenses/mit/)

