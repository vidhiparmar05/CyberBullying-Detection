Cyberbullying is a growing concern on social media and online platforms. 
This project aims to build a machine learning model that can automatically detect cyberbullying in text-based messages, helping to prevent online harassment.
he dataset used in this project is cyberbullying_tweets, which contains 47,693 tweets labeled into six categories:

Age
Ethnicity
Gender
Religion
Other Cyberbullying
Not Cyberbullying
Methodology
Data Preprocessing:

Removing stop words, punctuation, and special characters
Tokenization and stemming
Converting text into numerical features using TF-IDF or Word Embeddings
Feature Selection:

Analyzing word frequency
Selecting relevant features for model training
Model Training:

Training multiple classifiers:
K-Nearest Neighbors (KNN)
Naïve Bayes
Logistic Regression
Support Vector Machine (SVM)
Decision Tree
Testing individual and ensemble models
Evaluation Metrics:

Accuracy
Confusion Matrix
Precision, Recall, and F1-Score
AUC-ROC Curve
Deployment
The trained model will be deployed using Streamlit, where users can input text and get real-time predictions on whether it contains cyberbullying content.

Conclusion
This project will provide an efficient and automated solution for detecting cyberbullying, helping social media platforms and online communities maintain a safer environment.
