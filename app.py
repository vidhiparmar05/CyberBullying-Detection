import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the trained model and vectorizer
model_path = "svm_model.pkl"  # Path to your saved model
vectorizer_path = "vectorizer.pkl"  # Path to your saved vectorizer

with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            background: linear-gradient(90deg, #ff7f50, #1e90ff);
            -webkit-background-clip: text;
            color: transparent;
            font-weight: bold;
        }
        .sub-title {
            text-align: center;
            font-size: 18px;
            background: linear-gradient(90deg, #6A5ACD, #20B2AA);
            -webkit-background-clip: text;
            color: transparent;
            font-weight: 600;
            margin-bottom: 30px;
        }
        .input-container {
            text-align: center;
            margin-top: 20px;
        }
        .predict-button {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        .result-container {
            margin-top: 30px;
            text-align: center;
            font-size: 22px;
            color: #27AE60;
        }
        .warning-container {
            text-align: center;
            font-size: 20px;
            color: #E74C3C;
        }
        .footer {
            position: relative;
            width: 100%;
            background-color: #2C3E50;
            color: #ECF0F1;
            text-align: center;
            padding: 20px;
            font-size: 16px;
            border-top: 2px solid #2980B9;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app
st.markdown('<div class="main-title">Cyberbullying Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Analyze the type of cyberbullying in text</div>', unsafe_allow_html=True)

# Input section
user_input = st.text_area(
    "Enter a tweet or text to analyze:",
    placeholder="Type the text you want to analyze here...",
    height=150,
)

# Predict button and result section
st.markdown('<div class="predict-button">', unsafe_allow_html=True)
if st.button("Predict"):
    if user_input.strip():
        # Preprocess input and predict
        user_input_vectorized = vectorizer.transform([user_input])
        prediction = model.predict(user_input_vectorized)[0]
        
        # Display result
        st.markdown(
            f'<div class="result-container">The predicted type of cyberbullying is: <strong>{prediction}</strong></div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="warning-container">⚠️ Please enter some text to analyze!</div>',
            unsafe_allow_html=True,
        )
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        Developed by <b>Vidhi Parmar</b> | Cyberbullying Detection Project | © 2024
    </div>
    """,
    unsafe_allow_html=True,
)
