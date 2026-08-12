# 🏛️ TRIP

> **Smart Tourism Village Decision Support System**

---

# 📖 About

TRIP (Tourism Resource Integration Platform) is a web-based Decision Support System (DSS) developed to support data-driven decision making for tourism village development in Batu City.

The system integrates tourism village research data, statistical analysis, machine learning, and decision support features into a centralized platform.

TRIP provides functionalities for:

- Tourism village data management
- Respondent and questionnaire data management
- Statistical and machine learning analysis
- Tourism village clustering
- Village performance assessment
- Interactive analytics dashboard
- Development recommendations
- Decision support for tourism village management

The system is developed in collaboration with **Bappelitbangda Kota Batu** and is intended to support data-based evaluation and development of tourism villages.

---

# 🎯 Objectives

The system aims to:

- Manage tourism village master data
- Manage research variables, indicators, and questionnaires
- Store respondent and survey response data
- Process tourism village assessment data
- Perform statistical and machine learning analysis
- Group tourism villages based on their characteristics
- Visualize analysis results through interactive dashboards
- Provide assessment and development recommendations
- Support evidence-based decision making

---

# 🏗️ Project Architecture

```text
TRIP/
│
├── backend/
├── datasets/
├── docs/
├── deployment/
├── scripts/
└── tests/
```

The backend is developed using Django with a modular application architecture.

---

# ⚙️ Technology Stack

## Backend

- Python
- Django
- SQLite (development)
- PostgreSQL (production)

## Frontend

- HTML5
- Bootstrap 5
- JavaScript
- Chart.js
- Plotly
- Leaflet

## Data Science & Machine Learning

- Scikit-Learn
- NumPy
- Pandas
- Joblib
- PCA
- K-Means Clustering
- Feature Importance Analysis

## AI & Chatbot

- Anthropic API
- Pydantic

## Deployment

- Docker
- Gunicorn
- Nginx
- WhiteNoise

---

# 📊 Research Data

The system currently manages tourism village research data consisting of:

- **24 Tourism Villages**
- **1,152 Respondents**
- **11 Research Variables**
- **88 Indicators**

The research data is processed to support tourism village assessment, clustering, and decision-making.

---

# 🔬 Research & Analysis

TRIP integrates several analytical methods, including:

## Statistical Analysis

- Path Analysis
- Principal Component Analysis (PCA)

## Machine Learning

- K-Means Clustering
- Silhouette Score Evaluation
- Feature Importance Analysis

## Decision Support

- Tourism village assessment
- Village ranking
- Cluster-based evaluation
- Development recommendations

---

# 📂 Main Modules

- Authentication
- Dashboard
- Village Management
- District Management
- Variable Management
- Indicator Management
- Questionnaire
- Survey
- Respondent
- Response
- Analytics
- Machine Learning
- Recommendation
- Chatbot
- Administration

---

# 📁 Project Structure

```text
backend/
│
├── apps/
│   ├── analytics/
│   ├── chatbot/
│   ├── master/
│   ├── recommendation/
│   ├── respondent/
│   ├── response/
│   └── survey/
│
├── common/
├── config/
├── static/
├── templates/
├── data.json
├── initial_data.json
├── export_fixture.py
├── manage.py
└── requirements.txt
```

---

# 📈 Analytics Dashboard

The analytics dashboard provides several visualizations for exploring tourism village analysis results, including:

- Cluster distribution
- Feature importance
- PCA scatter plot
- Village performance comparison
- Radar chart for village indicators
- Village ranking and cluster information

The dashboard is designed to provide a visual overview of tourism village characteristics and analytical results.

---

# 🤖 Machine Learning

The machine learning module provides automated tourism village clustering using the K-Means algorithm.

The system stores trained model information through the `MLModelRegistry`, including:

- Number of clusters
- Cluster mapping
- Silhouette score
- Training timestamp
- Model activation status

The clustering results are associated with tourism villages and can be visualized through the analytics dashboard.

---

# 🗺️ Geographic Visualization

The system is being developed to provide geographic visualization of tourism village cluster distribution.

The planned mapping visualization will display tourism villages on an interactive map based on their geographic coordinates and corresponding cluster classification.

---

# 🚀 Development Status

Current implemented features include:

- [x] Django Project Architecture
- [x] Authentication
- [x] Master Data Management
- [x] District Management
- [x] Tourism Village Management
- [x] Variable Management
- [x] Indicator Management
- [x] Questionnaire Management
- [x] Survey Module
- [x] Respondent Management
- [x] Response Management
- [x] Analytics Dashboard
- [x] Machine Learning Module
- [x] K-Means Clustering
- [x] PCA Visualization
- [x] Feature Importance Visualization
- [x] Radar Chart
- [x] Recommendation Module
- [x] Chatbot Integration

---

# 📌 Current Status

Version:

```text
v0.1.0
```

Current Phase:

```text
System Development & Analytics Integration
```

The core system architecture, master data management, research data management, analytics, and machine learning modules have been implemented.

Further development focuses on geographic cluster visualization, reporting, and production deployment.

---

# 👨‍💻 Development Team

## Developer

- Undergraduate Student
- Bachelor of Data Science
- Universitas Brawijaya

## Supervisor

- Universitas Brawijaya

## Institution

- Bappelitbangda Kota Batu

---

# 📄 License

This project is released under the MIT License.

---

# 🤝 Contribution

The project follows a modular software development approach.

Each feature is developed incrementally based on system requirements and project development stages.

---

# ⭐ Future Development

Planned future improvements include:

- Interactive GIS and cluster mapping
- AI-assisted recommendation engine
- Explainable AI (XAI)
- Mobile-responsive dashboard
- API integration
- Public information portal
- Multi-year analysis
- Time series analytics
- Production deployment