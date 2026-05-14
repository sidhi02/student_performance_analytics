import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance App",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(
        135deg,
        #f8fbff 0%,
        #eef4ff 55%,
        #fff7ed 100%
    );
}

/* ---------------- SIDEBAR ---------------- */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #172554 0%,
        #1e3a8a 100%
    );
    border-right: 2px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p {
    color: white !important;
}

section[data-testid="stSidebar"] div[data-baseweb="select"] * {
    color: #1e293b !important;
}

section[data-testid="stSidebar"] input {
    color: #1e293b !important;
}

/* ---------------- TITLE ---------------- */

.main-title {
    font-size: 52px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 18px;
    color: #64748b;
    margin-bottom: 25px;
}

/* ---------------- METRIC CARDS ---------------- */

.metric-card {
    background: white;
    padding: 24px;
    border-radius: 22px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    border-left: 7px solid #3b82f6;
    transition: 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
}

.metric-label {
    font-size: 15px;
    color: #64748b;
    font-weight: 600;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 34px;
    font-weight: 800;
    color: #111827;
}

.pass-card {
    border-left-color: #22c55e;
}

.risk-card {
    border-left-color: #ef4444;
}

.prob-card {
    border-left-color: #f59e0b;
}

/* ---------------- INFO BOXES ---------------- */

.success-box {
    background: #dcfce7;
    color: #166534;
    padding: 18px;
    border-radius: 14px;
    font-weight: 600;
}

.warning-box {
    background: #fef3c7;
    color: #92400e;
    padding: 18px;
    border-radius: 14px;
    font-weight: 600;
}

.info-box {
    background: #dbeafe;
    color: #1e40af;
    padding: 18px;
    border-radius: 14px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
import os
model_path = os.path.join(os.path.dirname(__file__), "pass_fail_model.pkl")
model = joblib.load(model_path)

# ---------------- SIDEBAR ----------------
st.sidebar.markdown("## 🎯 Enter Student Details")

st.sidebar.markdown(
    "Adjust the values below to predict performance."
)

gender = st.sidebar.selectbox(
    "👤 Gender",
    ["female", "male"]
)

test_preparation_course = st.sidebar.selectbox(
    "📘 Test Preparation Course",
    ["none", "completed"]
)

math_score = st.sidebar.slider(
    "➗ Math Score",
    0, 100, 50
)

reading_score = st.sidebar.slider(
    "📖 Reading Score",
    0, 100, 50
)

writing_score = st.sidebar.slider(
    "✍️ Writing Score",
    0, 100, 50
)

# ---------------- MAIN TITLE ----------------
st.markdown(
    """
<div class="main-title">
🎓 Student Performance Prediction App
</div>
""",
    unsafe_allow_html=True
)

st.markdown(
    """
<div class="subtitle">
Analyze student performance, predict pass/fail,
and get smart improvement suggestions.
</div>
""",
    unsafe_allow_html=True
)

# ---------------- CALCULATIONS ----------------
average_score = (
    math_score +
    reading_score +
    writing_score
) / 3

# ---------------- ENCODING ----------------
gender_encoded = (
    0 if gender == "female"
    else 1
)

test_prep_encoded = (
    0 if test_preparation_course == "none"
    else 1
)

# ---------------- INPUT DATA ----------------
input_data = pd.DataFrame({
    "gender": [gender_encoded],
    "test_preparation_course": [test_prep_encoded],
    "math_score": [math_score],
    "reading_score": [reading_score],
    "writing_score": [writing_score]
})

# ---------------- PREDICTION ----------------
prediction_value = model.predict(input_data)[0]

prediction = (
    "PASS"
    if prediction_value == 1
    else "FAIL"
)

# ---------------- PROBABILITY ----------------
pass_probability = (
    model.predict_proba(input_data)[0][1]
) * 100

# ---------------- RISK LEVEL ----------------
if average_score >= 75:
    risk_level = "Low Risk"

elif average_score >= 50:
    risk_level = "Medium Risk"

else:
    risk_level = "High Risk"

# ---------------- SUBJECT ANALYSIS ----------------
scores = {
    "Math": math_score,
    "Reading": reading_score,
    "Writing": writing_score
}

strongest_subject = max(
    scores,
    key=scores.get
)

weakest_subject = min(
    scores,
    key=scores.get
)

# ---------------- WHAT-IF IMPROVEMENT ----------------
improved_average = (
    sum(scores.values())
    - scores[weakest_subject]
    + min(scores[weakest_subject] + 10, 100)
) / 3

# ---------------- TABS ----------------
tab1, tab2, tab3 = st.tabs([
    "📊 Results",
    "📈 Score Analysis",
    "💡 Recommendations"
])

# ---------------- TAB 1 ----------------
with tab1:

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
<div class="metric-card">
<div class="metric-label">Average Score</div>
<div class="metric-value">{average_score:.2f}</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
<div class="metric-card pass-card">
<div class="metric-label">Prediction</div>
<div class="metric-value">{prediction}</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
<div class="metric-card risk-card">
<div class="metric-label">Risk Level</div>
<div class="metric-value">{risk_level}</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
<div class="metric-card prob-card">
<div class="metric-label">Pass Probability</div>
<div class="metric-value">{pass_probability:.1f}%</div>
</div>
""",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.progress(int(pass_probability))

# ---------------- TAB 2 ----------------
with tab2:

    score_df = pd.DataFrame({
        "Subject": [
            "Math",
            "Reading",
            "Writing"
        ],

        "Score": [
            math_score,
            reading_score,
            writing_score
        ]
    })

    fig = px.bar(
        score_df,
        x="Subject",
        y="Score",
        color="Subject",
        text="Score",

        color_discrete_map={
            "Math": "#3b82f6",
            "Reading": "#f97316",
            "Writing": "#22c55e"
        }
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Poppins",
            size=14
        ),

        yaxis=dict(range=[0, 100]),

        showlegend=False
    )

    fig.update_traces(
        textposition="outside",
        marker_line_width=0,
        width=0.45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f"""
<div class="success-box">
✅ Strongest Subject: {strongest_subject}
</div>
""",
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
<div class="warning-box">
⚠️ Weakest Subject: {weakest_subject}
</div>
""",
            unsafe_allow_html=True
        )

# ---------------- TAB 3 ----------------
with tab3:

    st.subheader(
        "Personalized Recommendation"
    )

    if average_score >= 75:

        st.success(
            "Great performance! Student should continue consistent revision and practice."
        )

    elif average_score >= 50:

        st.warning(
            "Student needs regular revision and targeted subject practice."
        )

    else:

        st.error(
            "Student needs strong improvement support and daily practice."
        )

    st.write(
        f"**Weak Area:** {weakest_subject}"
    )

    if weakest_subject == "Math":

        suggestion = (
            "Practice formulas, solve numerical problems daily, and revise basic concepts."
        )

    elif weakest_subject == "Reading":

        suggestion = (
            "Improve comprehension by reading passages and summarizing them."
        )

    else:

        suggestion = (
            "Practice grammar, essays, and structured writing regularly."
        )

    st.write(
        f"**Suggestion:** {suggestion}"
    )

    if test_preparation_course == "none":

        st.markdown(
            """
<div class="info-box">
💡 Extra Tip:
Completing a test preparation course may improve performance.
</div>
""",
            unsafe_allow_html=True
        )

    st.markdown(
        "## What-if Improvement"
    )

    st.write(
        "If the weakest subject improves by 10 marks:"
    )

    st.markdown(
        f"""
<div class="metric-card">
<div class="metric-label">Improved Average Score</div>
<div class="metric-value">{improved_average:.2f}</div>
</div>
""",
        unsafe_allow_html=True
    )
