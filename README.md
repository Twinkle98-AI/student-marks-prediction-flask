# student-marks-prediction-flask
# 🎓 Student Marks Prediction Web App

An end-to-end Machine Learning project that predicts student marks based on
study hours. The model is deployed using Flask and a simple HTML frontend.

---

## 🔍 Problem Statement
Students often wonder how many hours they need to study to achieve high marks.
This project uses a Machine Learning model to predict marks based on study time
and answers the question:

> **How many hours are required to score more than 99%?**  
👉 According to the trained model: **~10.3–10.8 hours**

---

## 🚀 Features
- Linear Regression model for prediction  
- Flask backend API  
- HTML/CSS frontend  
- Real-time predictions  
- End-to-end ML pipeline  

---

## 🛠 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Flask  
- HTML/CSS  
- Pickle  

---

## 📂 Project Structure

student-marks-prediction-flask/
│
├── app.py
├── train_model.py
├── model.pkl
├── student_scores.csv
├── templates/
│ └── index.html
└── README.md


---

## ⚙️ How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/student-marks-prediction-flask.git
cd student-marks-prediction-flask
2️⃣ Install Dependencies
pip install flask pandas numpy scikit-learn
3️⃣ Train the Model
python train_model.py
4️⃣ Run Flask App
python app.py
Open browser:

http://127.0.0.1:5000/
📊 Sample Prediction
Study Hours	Predicted Marks
5	~55%
8	~80%
10	~95%
📌 Learning Outcomes
End-to-end ML pipeline

Model serialization

Flask app deployment

Frontend & backend integration

👩‍💻 Author
Haimabati Haripriya Sahu

⭐ If you like this project, give it a star!
