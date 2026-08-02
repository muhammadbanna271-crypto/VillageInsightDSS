# 🏛️ VillageInsight DSS

> **Adaptive Decision Support System for Tourism Village Development using K-Means Clustering, Feature Importance Analysis, and TOPSIS**

![Version](https://img.shields.io/badge/version-v0.9.0-blue)
![Python](https://img.shields.io/badge/Python-3.12+-green)
![Django](https://img.shields.io/badge/Django-5.x-success)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![License](https://img.shields.io/badge/license-MIT-orange)

---

# 📖 About

VillageInsight DSS (Decision Support System) is a web-based information system developed to support evidence-based decision making for tourism village development.

The system integrates data engineering and machine learning by combining:

- K-Means Clustering (village segmentation)
- Random Forest Feature Importance (what drives cluster differences)
- TOPSIS (priority ranking within each cluster)
- PCA (2D visualization only, not a core analysis method)
- Interactive Dashboard
- Recommendation Engine
- Decision Support System (DSS)

This project is developed as an undergraduate thesis at Universitas Brawijaya and is intended to be scalable for future governmental implementation.

---

# 🎯 Objectives

The system aims to:

- Manage tourism village questionnaire data
- Store respondent information
- Perform assessment based on research variables
- Visualize village performance
- Predict village cluster
- Generate development recommendations
- Support government decision making

---

# 🏗️ Project Architecture

```
VillageInsightDSS/

├── backend/
│   ├── apps/          # master, survey, respondent, response,
│   │                   # analytics, dashboard, recommendation
│   ├── common/         # shared base view/model/form classes
│   ├── config/         # Django settings, urls, wsgi/asgi
│   ├── static/         # css, js
│   └── templates/      # shared templates
├── requirements.txt
└── (deployment/, docs/, scripts/, tests/ -- planned, not yet created)
```

---

# ⚙️ Technology Stack

## Backend

- Python
- Django
- PostgreSQL

## Frontend

- HTML5
- Bootstrap 5
- JavaScript
- Chart.js
- GIS map: planned, not yet implemented (see Future Development)

## Machine Learning

- Scikit-Learn
- Joblib
- NumPy
- Pandas

## Deployment

- Docker
- Gunicorn
- Nginx

---

# 📊 Research Methodology

The system is built based on a machine learning pipeline consisting of:

- K-Means Clustering (village segmentation)
- Random Forest (feature importance across clusters)
- TOPSIS (priority ranking within cluster)
- PCA (visualization only, not a core analysis method)

Research data:

- 24 Tourism Villages
- 1,152 Respondents
- 5 Predictor Variables (X1-X5): Orientasi Pasar, Fasilitas Pariwisata,
  Infrastruktur dan Aksesibilitas, Hubungan Pemasaran, Kualitas Layanan
- 3 Mediator Variables (Y1-Y3): Inovasi Ekonomi Kreatif, Kepuasan
  Pengunjung, Orientasi Kewirausahaan
- 3 Response Variables (Y4-Y6): Penerimaan Daerah (PAD), Kunjungan
  Wisata, Keunggulan Bersaing
- Independent Variables (X1–X5)
- Mediator Variables (Y1–Y3)
- Dependent Variables (Y4–Y6)

---

# 📂 Main Modules

- Authentication
- Village Management
- Variable Management
- Indicator Management
- Questionnaire
- Survey
- Respondent
- Analytics
- Dashboard
- Assessment
- Recommendation
- Reporting
- Administration
- Audit Log

---

# 📁 Project Structure

```
backend/
│
├── apps/
│   ├── master/          # village, district, variable, indicator, questionnaire, cluster
│   ├── survey/
│   ├── respondent/
│   ├── response/        # answers + bulk Excel import + scoring
│   ├── analytics/        # score aggregation, K-Means, feature importance, ML registry
│   ├── dashboard/
│   └── recommendation/   # TOPSIS ranking within cluster
├── common/
├── config/
├── static/
├── templates/
└── manage.py
```

---

# 🔄 Operational Flow (Import → Analysis)

Importing response data does **not** automatically update scores, clusters,
or recommendations. The actual sequence is:

1. **Seed master data first** (village, variable, indicator, questionnaire,
   survey) -- see `seed_master_data.py` management command. Required once
   before any response data can be imported.
2. **Import response data** via `/response/import/`. This only stores raw
   answers (`Response`) -- no scores or clusters are computed yet.
3. **Click "Retrain Model"** on the Analytics/ML dashboard
   (`/analytics/ml/retrain/`). This single action triggers, in order:
   score aggregation (indicator → variable → village) **and** K-Means
   clustering. Both are bundled into this one step.
4. **Only after step 3** will the Recommendation (TOPSIS) page and the
   Analytics dashboards have data to show. If Recommendation looks empty
   right after import, this is why -- retrain hasn't run yet, not a bug.

This coupling (aggregation only runs as a side effect of retraining, not
on its own) is a known design quirk worth keeping in mind when debugging
or extending the pipeline.

---

# 🚀 Development Roadmap

- [x] Project Planning
- [x] Software Architecture
- [ ] Django Foundation
- [ ] Authentication
- [ ] Master Data
- [ ] Questionnaire
- [ ] Survey Module
- [ ] Dashboard
- [ ] Analytics
- [ ] Machine Learning
- [ ] Recommendation Engine
- [ ] Reporting
- [ ] Deployment

---

# 📌 Current Status

Version:

```
v0.1.0
```

Current Phase:

```
Project Architecture & Software Design
```

---

# 👨‍💻 Development Team

Developer

- Undergraduate Student
- Department of Statistics
- Bachelor of Data Science
- Universitas Brawijaya

Supervisor

- (To be updated)

Institution

- Bappelitbangda Kota Batu

---

# 📄 License

This project is released under the MIT License.

---

# 🤝 Contribution

This repository follows enterprise software architecture.

Every feature is developed incrementally based on sprint planning.

---

# ⭐ Future Development

- AI Recommendation Engine
- Explainable AI (XAI)
- Interactive GIS
- Mobile Responsive Dashboard
- API Integration
- Public Portal
- Multi-Year Analysis
- Time Series Analytics