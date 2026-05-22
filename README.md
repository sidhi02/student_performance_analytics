# 🎓 AI-Powered Student Performance Analytics

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-RandomForest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)

## 📌 Project Overview
This project analyzes student performance data to identify patterns affecting academic scores and predict whether a student is at risk based on performance metrics.

The project combines:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Tableau Dashboard
- Machine Learning Prediction
- Streamlit Web Application Deployment

It is a complete end-to-end Data Analytics and Machine Learning project.

---

## 🏗️ Project Architecture

```text
                 ┌─────────────────────┐
                 │   Student Dataset   │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Data Cleaning &    │
                 │   Preprocessing     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Exploratory Data    │
                 │ Analysis (EDA)      │
                 └──────────┬──────────┘
                            │
            ┌───────────────┴───────────────┐
            ▼                               ▼
 ┌─────────────────────┐        ┌─────────────────────┐
 │ Tableau Dashboard   │        │ Machine Learning    │
 │ Visualization       │        │ Model Training      │
 └──────────┬──────────┘        └──────────┬──────────┘
            │                              │
            ▼                              ▼
 ┌─────────────────────┐        ┌─────────────────────┐
 │ Performance Insights│        │ Risk Prediction     │
 │ & KPI Analysis      │        │ System              │
 └──────────┬──────────┘        └──────────┬──────────┘
            │                              │
            └───────────────┬──────────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Streamlit Web App   │
                 │ Deployment          │
                 └─────────────────────┘
```


## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Student Performance Insights
- Interactive Tableau Dashboard
- Pass/Fail Prediction Model
- Streamlit Web Application
- Risk Level Detection
- Personalized Recommendations
- GitHub Project Deployment
- Live Streamlit Deployment

---

## 🛠️ Technologies Used

### Programming & Analysis
- Python
- Pandas
- NumPy
- Scikit-learn

### Visualization
- Matplotlib
- Seaborn
- Plotly
- Tableau

### Deployment
- Streamlit
- GitHub

---

## 📂 Project Structure

```text
student_performance_analytics/

├── cleaned_data/
├── dashboard/
├── dataset/
├── notebooks/
│   ├── student_performance_analysis.ipynb
│   └── ml_pass_fail_prediction.ipynb
├── app/
│   ├── app.py
│   ├── pass_fail_model.pkl
│   └── requirements.txt
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 📊 Dataset Information

The dataset contains student-related attributes such as:
- Gender
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

The dataset was cleaned and transformed before analysis and modeling.

---

## 📈 Exploratory Data Analysis (EDA)

The project includes:
- Score distribution analysis
- Gender-wise performance comparison
- Correlation heatmaps
- Test preparation impact analysis
- Grade category distribution
- Average score analysis

### Key Insights
- Students completing the test preparation course scored better overall.
- Reading and writing scores were highly correlated.
- Female students performed better in reading and writing.
- Math scores showed higher variability.
- Most students belonged to the Good performance category.

---

## 🤖 Machine Learning Model

### 🎯 Objective
The objective of this project is to analyze factors affecting student academic performance and build a machine learning system capable of predicting student risk levels using examination scores and preparation metrics.

### Risk Categories
- Low Risk
- Medium Risk
- High Risk

### Model Used
- Random Forest Classifier

### Model Workflow
1. Data preprocessing
2. Feature selection
3. Train-test split
4. Model training
5. Prediction generation
6. Model saving using Joblib

---

## 📈 Model Performance

- Accuracy: 89%
- Precision: 87%
- Recall: 85%
- F1-Score: 86%
 
### Confusion Matrix
<img width="503" height="447" alt="Screenshot 2026-05-14 at 9 45 20 PM" src="https://github.com/user-attachments/assets/d93082ed-bff4-4b0f-9684-a599c742094b" />

### ROC Curve
<img width="616" height="461" alt="Screenshot 2026-05-14 at 9 45 42 PM" src="https://github.com/user-attachments/assets/38765103-377c-4248-8a2e-15be727be6f3" />

### Feature Importance
<img width="2216" height="1117" alt="Screenshot 2026-05-14 at 9 41 44 PM" src="https://github.com/user-attachments/assets/636d346c-1c5a-4fac-9d79-86dee6060dae" />

---

## 🌐 Streamlit Web App

The project includes an interactive Streamlit application where users can:
- Enter student details
- Predict performance risk
- View personalized recommendations
- Analyze score insights visually

---

## 📊 Tableau Dashboard

The Tableau dashboard provides:
- KPI cards
- Gender analysis
- Performance distribution
- Average score analysis
- Interactive filters
- Student performance insights

---

## 💡 Business Impact

This project can help educational institutions:
- Identify academically at-risk students early
- Improve intervention strategies
- Support data-driven academic decisions
- Monitor student performance trends
- Enhance student success rates

---

## ▶️ How to Run Locally

### Clone Repository

```bash
git clone https://github.com/sidhi02/student_performance_analytics.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app/app.py
```

---

## 🔗 Project Links

### GitHub Repository
[View GitHub Repository](https://github.com/sidhi02/student_performance_analytics)
### Live Streamlit App
[Open Streamlit App](https://studentperformanceanalytics-cyegnpc6slgyytahiyrs4c.streamlit.app)
### Tableau Dashboard
[View Tableau Dashboard](https://public.tableau.com/app/profile/sidhi.deshmukh/viz/students_performance_analytics/Dashboard2)

---

## 📸 Project Screenshots

- Tableau Dashboard
<img width="1007" height="665" alt="students_performance_dashboard" src="https://github.com/user-attachments/assets/83fad8ab-41e3-45a2-afea-aa8123f737be" />


- Streamlit App
<img width="1470" height="865" alt="Screenshot 2026-05-14 at 9 32 38 PM" src="https://github.com/user-attachments/assets/9ae54abe-eb6f-449b-a1e7-15d8620ab609" />
<img width="1468" height="868" alt="Screenshot 2026-05-14 at 9 32 56 PM" src="https://github.com/user-attachments/assets/65e89825-caa9-4746-b61d-4ea782f4f939" />
<img width="1467" height="870" alt="Screenshot 2026-05-14 at 9 33 14 PM" src="https://github.com/user-attachments/assets/dbe6b18a-64c2-4398-abe8-5f5be17c671c" />

---

## 📚 Learning Outcomes

Through this project, I learned:
- Data cleaning and preprocessing
- Exploratory data analysis
- Dashboard creation
- Machine learning workflows
- Model deployment
- GitHub project management
- Streamlit web app development

---

## 🚀 Future Enhancements

Future improvements planned for the project:
- AI chatbot for recommendations
- SQL database integration
- Cloud deployment
- Feature importance analysis
- PDF report generation
- Real-time analytics

---

## 👩‍💻 Author

**Sidhi Deshmukh**

3rd Year Computer Science Engineering Student  
Specialization: Artificial Intelligence & Data Science.
