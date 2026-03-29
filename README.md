1. ![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
2. ai_spam_detector_pro/
│
├── app/
│   └── app.py
│
├── model/
│   ├── train_model.py
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── data/
│   └── spam.csv
│
├── requirements.txt
└── README.md
3. # 📧 AI Spam Email Detector (Production-Level)

A machine learning web app that detects whether an email/message is spam using probability-based classification (Naive Bayes).

---

## 🚀 Live Demo
👉 https://aispamdetectorpro-75ye4ojq5f4p9q6bnuyzkq.streamlit.app/

---

## 🧠 How It Works

This model uses **Naive Bayes (based on Bayes' Theorem)** to calculate the probability that a message is spam.

Pipeline:
1. Text preprocessing
2. TF-IDF vectorization
3. Naive Bayes classification
4. Probability-based prediction

---

## ✨ Features

- ✅ Real-world dataset (1000+ messages)
- ✅ Probability score (Spam confidence %)
- ✅ TF-IDF text processing
- ✅ Clean UI using Streamlit
- ✅ Model persistence using Pickle

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Pandas
- Streamlit

---

## 📊 Model Performance

- Accuracy: ~85–95% (depends on dataset)

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python model/train_model.py
streamlit run app/app.py
