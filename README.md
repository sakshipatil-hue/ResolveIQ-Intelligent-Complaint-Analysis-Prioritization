# ⚡ ResolveIQ — Intelligent Complaint Analysis & Prioritization

\<p align="center">   \<strong>Turning customer complaints into actionable intelligence.\</strong>   \<br/>   An NLP-powered complaint analysis system built with Django and Machine Learning. \</p>

\<p align="center">   \<img src="[https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)" />   \<img src="[https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django\&logoColor=white)" />   \<img src="[https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikitlearn\&logoColor=white)" />   \<img src="[https://img.shields.io/badge/NLP-8A2BE2?style=for-the-badge](https://img.shields.io/badge/NLP-8A2BE2?style=for-the-badge)" />   \<img src="[https://img.shields.io/badge/Status-Active-success?style=for-the-badge](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)" /> \</p>

---

## 💡 Overview

**ResolveIQ** is an intelligent complaint analysis and prioritization platform that transforms unstructured customer complaints into meaningful insights.

Instead of manually reviewing every complaint, ResolveIQ uses Natural Language Processing (NLP) and Machine Learning to automatically:

- 🧠 Classify complaints into relevant categories.
- 📊 Estimate prediction confidence.
- 🎭 Analyze customer sentiment.
- 🚨 Identify complaint urgency using explainable rules.
- 🔍 Flag uncertain predictions for human review.
- 📈 Maintain complaint records for historical analysis.

The goal is simple: **help organizations understand customer issues faster and prioritize the complaints that need attention.**

---

## ✨ Key Features

| Feature                     | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| 🧠 Complaint Classification | Predicts one of six complaint categories using an ML model.        |
| 🎭 Sentiment Analysis       | Identifies Positive, Neutral and Negative sentiment using VADER.   |
| 🚨 Urgency Detection        | Uses transparent keyword and phrase matching to determine urgency. |
| 📊 Confidence Scoring       | Displays the model's prediction confidence.                        |
| 🔎 Human Review Flag        | Flags predictions below a confidence threshold of 0.40.            |
| 📁 Complaint History        | Stores and displays previously analyzed complaints.                |
| 📈 Dashboard                | Provides an overview of complaint activity and insights.           |
| 🛠️ Django Admin            | Enables administrative access to stored complaint records.         |

---

## ⚙️ How It Works

ResolveIQ follows a multi-stage complaint analysis pipeline.

```text
        CUSTOMER COMPLAINT
                |
                ▼
       TEXT PREPROCESSING
                |
                ▼
       TF-IDF VECTORIZATION
                |
                ▼
      LOGISTIC REGRESSION
                |
                ▼
      COMPLAINT CATEGORY
                |
        ┌───────┴────────┐
        ▼               ▼
  SENTIMENT          URGENCY
  ANALYSIS           DETECTION
        |               |
        └───────┬───────┘
                ▼
       CONFIDENCE CHECK
                |
                ▼
       HUMAN REVIEW FLAG
                |
                ▼
       DJANGO DATABASE
                |
                ▼
       DASHBOARD & HISTORY
```

### 🧠 Machine Learning Pipeline

The complaint classification model uses:

- **TF-IDF Vectorization:** Converts text into numerical features using unigram and bigram representations.
- **Logistic Regression:** Predicts the most likely complaint category.
- **Class Weight Balancing:** Helps address differences in category distribution.

### 🎭 Sentiment Analysis

VADER (Valence Aware Dictionary and sEntiment Reasoner) analyzes the emotional tone of complaint text.

It categorizes sentiment into:

- 🟢 Positive
- 🟡 Neutral
- 🔴 Negative

### 🚨 Explainable Urgency Detection

Urgency is determined through transparent keyword and phrase matching rather than a black-box ML prediction.

For example:

- **High:** Contains phrases such as "urgent", "immediately" or "emergency".
- **Medium:** Contains indicators of a time-sensitive or unresolved issue.
- **Low:** Default classification when no urgency indicators are detected.

Each urgency decision includes an explanation, making the result easier to interpret.

### 🔎 Human-in-the-Loop Review

Predictions with confidence below **0.40** are flagged for human review.

This helps identify uncertain classifications instead of treating every model prediction as equally reliable.

---

## 📊 Model Performance

The classification model was evaluated on a held-out test dataset.

| Metric            |      Score |
| ----------------- | ---------: |
| Accuracy          | **83.11%** |
| Weighted F1-score | **83.10%** |
| Macro F1-score    | **75.22%** |
| Test Samples      |      4,180 |

**Model:** TF-IDF + Logistic Regression

**Dataset:** 20,899 CFPB financial consumer complaints.

### Complaint Categories

The model classifies complaints into six categories:

1. 🏦 Bank Account Services
2. 💳 Credit Card
3. 📋 Credit Reporting
4. 💰 Debt Collection
5. 💸 Money Transfers
6. 🏠 Mortgages and Loans

---

## 🧰 Tech Stack

| Category          | Technologies                      |
| ----------------- | --------------------------------- |
| Backend           | Python, Django                    |
| Machine Learning  | Scikit-learn, Logistic Regression |
| NLP               | TF-IDF, VADER Sentiment Analysis  |
| Data Processing   | Pandas, NumPy                     |
| Model Persistence | Joblib                            |
| Database          | SQLite                            |
| Frontend          | HTML, CSS                         |
| Visualization     | Matplotlib, Seaborn               |
| Development       | Jupyter Notebook, Git, GitHub     |

---

## 🏗️ Project Structure

```text
ResolveIQ/
│
├── app/
│   └── app.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── models/
│   └── ticket_classifier.joblib
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── reports/
│   ├── evaluation_report.md
│   ├── metrics.json
│   └── figures/
│
├── src/
│   ├── data_preprocessing.py
│   ├── evaluation.py
│   ├── predict.py
│   ├── train.py
│   └── urgency.py
│
├── tickets/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── tests/
├── manage.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Getting Started

Follow these steps to run ResolveIQ locally.

### 1. Clone the repository

```bash
git clone https://github.com/sakshipatil-hue/ResolveIQ-Intelligent-Complaint-Analysis-Prioritization.git
```

### 2. Navigate to the project directory

```bash
cd ResolveIQ-Intelligent-Complaint-Analysis-Prioritization
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

### 7. Open the application

Visit:

```text
http://127.0.0.1:8000/
```

---

## 🧪 Testing

Run Django's system checks:

```bash
python manage.py check
```

Run the test suite:

```bash
python manage.py test
```

---

## 🎯 Project Objectives

ResolveIQ explores how Machine Learning and NLP can be combined with a web framework to build practical complaint intelligence systems.

Key engineering objectives:

- Build an end-to-end ML-powered web application.
- Integrate trained models into a Django backend.
- Combine statistical NLP with transparent rule-based logic.
- Make predictions interpretable through confidence and explanation.
- Introduce human review for uncertain classifications.
- Maintain structured records for further analysis.

---

## 🔮 Future Improvements

- [ ] Interactive complaint analytics and visualizations.
- [ ] Advanced complaint prioritization using multiple signals.
- [ ] Explainable ML predictions with feature-level insights.
- [ ] REST API integration.
- [ ] User authentication and role-based access.
- [ ] Docker-based deployment.
- [ ] Cloud deployment and production monitoring.

---

## ⚠️ Limitations

- Classification performance depends on the patterns represented in the training dataset.
- VADER sentiment analysis may not fully capture sarcasm or complex context.
- Urgency detection currently relies on predefined keyword and phrase rules.
- Confidence scores are model estimates and should not be interpreted as guaranteed probabilities of correctness.

ResolveIQ is a portfolio and demonstration project, not a production financial complaint decision system.

---

## 👩‍💻 Author

**Sakshi Patil**

🎓 B.Tech — Computer Science & Engineering (AI & ML)

- 🐙 GitHub: [@sakshipatil-hue](https://github.com/sakshipatil-hue)
- 💼 LinkedIn: [Sakshi Patil](https://www.linkedin.com/in/sakshi-patil-58aa86327/)

---

\<p align="center">
&#x20; \<strong>⚡ ResolveIQ\</strong>
&#x20; \<br/>
&#x20; \<em>From complaints to clarity. From data to decisions.\</em>
&#x20; \<br/>\<br/>
&#x20; ⭐ If you find this project interesting, consider giving it a star!
\</p>
