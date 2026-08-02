# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog and follows Semantic Versioning.

---

# [0.1.0] - Initial Architecture

Release Date: TBD

## Added

### Project

- Initial project planning
- Enterprise project architecture
- Folder structure
- Development roadmap
- Project Bible
- Documentation structure

### Backend

- Backend directory
- Django application structure
- Core architecture
- Common components
- Machine learning directory

### Documentation

- README.md
- PROJECT_BIBLE.md
- ROADMAP.md
- CHANGELOG.md
- TODO.md

### Database

- Database architecture design
- Conceptual data model
- Master tables design
- Transaction tables design

### Research

- Path Analysis integration plan
- PCA integration plan
- Cluster Analysis integration plan

### Machine Learning

- ML architecture
- Model artifact structure
- Rule engine design

---

# [0.9.1] - Real Data Integration Fixes

Release Date: TBD

## Fixed

- `requirements.txt` was missing `reportlab` and `matplotlib`, both used
  by `analytics/exports/pdf_export.py` and `recommendation/exports/pdf_export.py`.
  A fresh `pip install -r requirements.txt` would fail with
  `ModuleNotFoundError` the moment any PDF export code path was touched
  (discovered when running `migrate` for the first time).

## Added

- `seed_master_data.py` management command: seeds village, variable,
  indicator, questionnaire, and survey master data from a JSON fixture,
  since 88 indicators cannot practically be entered one-by-one through
  the web forms before response data can be imported.
- Documented the actual operational sequence (import -> retrain model ->
  recommendation/analytics) in README -- score aggregation and clustering
  are not triggered automatically on import; both only run as a side
  effect of the "Retrain Model" action on the Analytics/ML dashboard.

---

# [0.9.0] - Core System Complete (pre-deployment)

Release Date: TBD (PKL delivery)

## Added

- Master data CRUD: village, district, variable, indicator, questionnaire, cluster
- Survey + respondent management, Excel bulk import (88-indicator format, 24 villages)
- Score aggregation pipeline: indicator -> variable -> village (single source of truth shared by ML and recommendation)
- K-Means clustering with silhouette/inertia metrics, model persistence via joblib, MLModelRegistry versioning
- Random Forest feature importance (what separates the clusters)
- TOPSIS priority ranking, computed within each cluster
- Analytics + recommendation dashboards (Chart.js), PDF/Excel export

## Known gaps

- Path Analysis (mentioned in original plan) was not implemented
- PCA is used for 2D visualization only, not as a core analysis method
- GIS map, Word export, and Dashboard Snapshot are not yet built
- No Docker/Gunicorn/Nginx setup yet (Phase 9, in progress)

---

# Upcoming

## Version 0.2.0

### Planned

- Django Project Initialization
- PostgreSQL Integration
- Authentication Module
- Base Template
- Logging System
- Environment Configuration

---

## Version 0.3.0

### Planned

- Village Module
- Variable Module
- Indicator Module
- Questionnaire Module

---

## Version 0.4.0

### Planned

- Survey Module
- Respondent Module
- Assessment Module

---

## Version 0.5.0

### Planned

- Dashboard
- Charts
- Maps
- KPI

---

## Version 0.6.0

### Planned

- Analytics
- Path Visualization
- PCA Visualization
- Cluster Visualization

---

## Version 0.7.0

### Planned

- Machine Learning Integration
- Cluster Prediction
- Recommendation Engine

---

## Version 0.8.0

### Planned

- Reporting
- PDF Export
- Excel Export
- Word Export

---

## Version 1.0.0

### Planned

- Production Deployment
- Final Documentation
- Stable Release