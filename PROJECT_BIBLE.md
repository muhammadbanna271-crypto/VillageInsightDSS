# PROJECT BIBLE

> VillageInsight DSS
> Adaptive Decision Support System for Tourism Village Development

Version : 0.9.0

Status : Active Development

---

# 1. PROJECT OVERVIEW

Project Name

VillageInsight DSS

Full Name

Village Insight Decision Support System

Purpose

Develop a web-based Decision Support System (DSS) that assists the government in evaluating, analyzing, and recommending tourism village development strategies based on statistical research.

---

# 2. RESEARCH FOUNDATION

Research Methods

- K-Means Clustering
- Random Forest (feature importance)
- TOPSIS (priority ranking within cluster)
- PCA (visualization only, 2D projection of the feature matrix)

Dataset

- 24 Tourism Villages
- 1,152 Respondents

Variables

Independent Variables

- X1 - Orientasi Pasar
- X2 - Fasilitas Pariwisata
- X3 - Infrastruktur dan Aksesibilitas
- X4 - Hubungan Pemasaran
- X5 - Kualitas Layanan

Mediator Variables

- Y1 - Inovasi Ekonomi Kreatif
- Y2 - Kepuasan Pengunjung
- Y3 - Orientasi Kewirausahaan

Dependent Variables

- Y4 - Penerimaan Daerah (PAD)
- Y5 - Kunjungan Wisata
- Y6 - Keunggulan Bersaing

Research Outputs

- Cluster Labels
- Feature Importance Ranking
- TOPSIS Priority Score

---

# 3. PROJECT GOALS

Primary Goals

- Questionnaire Management
- Village Assessment
- Data Visualization
- Cluster Prediction
- Recommendation Engine
- Decision Support

Secondary Goals

- Academic Research
- Government Monitoring
- Future Expansion
- Public Information

---

# 4. TECHNOLOGY STACK

Backend

- Python
- Django

Database

- PostgreSQL

Frontend

- HTML5
- Bootstrap 5
- JavaScript

Visualization

- Chart.js
- GIS map: planned, not yet implemented

Machine Learning

- Scikit-Learn
- Joblib
- Pandas
- NumPy

Deployment

- Docker
- Gunicorn
- Nginx

---

# 5. PROJECT STRUCTURE

VillageInsightDSS/

backend/

apps/

master/

survey/

respondent/

response/

analytics/

dashboard/

recommendation/

config/

common/

static/

templates/

manage.py

(datasets/, deployment/, docs/, scripts/, tests/ -- planned, not yet created)

---

# 6. SOFTWARE ARCHITECTURE

Browser

↓

URL

↓

View

↓

Service

↓

Repository

↓

Model

↓

PostgreSQL

Business Logic must NEVER be placed inside View.

---

# 7. DESIGN PRINCIPLES

Always follow

- SOLID
- DRY
- KISS
- Clean Architecture
- Separation of Concerns
- Reusable Components

---

# 8. DJANGO APPLICATIONS

master

Village, district, variable, indicator, questionnaire, cluster master data (CRUD)

survey

Survey and survey-village management

respondent

Respondent management

response

Survey answers, bulk Excel import, scoring

analytics

Score aggregation, K-Means clustering, feature importance, ML model registry

dashboard

Executive dashboard

recommendation

TOPSIS ranking within each cluster

(accounts, assessment, reports, administration, audit are not separate apps -- their responsibilities are folded into the apps above, e.g. auth uses Django's built-in accounts, exports live inside analytics/ and recommendation/)

---

# 9. DATABASE LAYERS

System

Master

Research

Transaction

Analytics

Logging

---

# 10. MASTER TABLES

mst_village

mst_variable

mst_indicator

mst_question

mst_cluster

mst_region

---

# 11. TRANSACTION TABLES

trx_survey

trx_respondent

trx_answer

trx_variable_score

trx_prediction

trx_recommendation

---

# 12. MACHINE LEARNING

Artifacts (joblib, not pickle)

- village_scaler.joblib
- village_kmeans.joblib

Decision logic

- TOPSIS ranking is computed directly in code (recommendation/services/topsis.py), not from external JSON rule files

---

# 13. USER ROLES

Administrator

Operator

Researcher

Government

Guest

---

# 14. CODING RULES

Python

snake_case

Classes

PascalCase

Constants

UPPER_CASE

HTML

kebab-case

URLs

lowercase

---

# 15. GIT STRATEGY

main

Production

develop

Development

feature/*

New Features

fix/*

Bug Fixes

---

# 16. VERSIONING

Major.Minor.Patch

Example

0.1.0

---

# 17. DEVELOPMENT PHASES

Phase 0

Architecture

Phase 1

Foundation

Phase 2

Master Data

Phase 3

Survey

Phase 4

Dashboard

Phase 5

Analytics

Phase 6

Machine Learning

Phase 7

Recommendation

Phase 8

Reporting

Phase 9

Deployment

---

# 18. PROJECT RULES

- Never place business logic in views.
- Always use Service Layer.
- Always use Repository Layer.
- Never duplicate code.
- Keep modules independent.
- Follow enterprise architecture.
- Maintain documentation with every sprint.
- Write clean, readable, and maintainable code.

---

# 19. LONG-TERM GOALS

- Explainable AI
- GIS Integration
- REST API
- Mobile Support
- Multi-Year Analytics
- Public Dashboard
- Real-Time Assessment

---

# END OF PROJECT BIBLE