import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 AI Spam Email Detector")
st.write("Check if your email is spam using AI")

user_input = st.text_area("✉️ Enter your email:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        input_vec = vectorizer.transform([user_input])

        prediction = model.predict(input_vec)[0]
        probability = model.predict_proba(input_vec)

        spam_prob = probability[0][list(model.classes_).index("spam")] * 100

        if prediction == "spam":
            st.error(f"🚨 Spam Detected ({spam_prob:.2f}% confidence)")
        else:
            st.success(f"✅ Not Spam ({100-spam_prob:.2f}% confidence)")