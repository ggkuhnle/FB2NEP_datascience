# FB2NEP – Public Health Nutrition & Epidemiology

This repository supports the FB2NEP module at the University of Reading, focused on core skills in nutritional epidemiology and public health nutrition. The materials use synthetic but realistic data and can be run via **Google Colab** – no installation required.

---

## 📁 Structure

- `notebooks/` – Jupyter notebooks for each week
- `data/` – synthetic datasets
- `scripts/` – dataset generation and support scripts

---

## 🚀 Getting Started

You can open notebooks directly in [Google Colab](https://colab.research.google.com/).

Example:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ggkuhnle/FB2NEP_datascience/blob/main/notebooks/00_playground.ipynb)

---

## 📚 Weekly Content Overview

| Week | Notebook | Topics |
|------|----------|--------|
| 1 | `00_playground.ipynb` | What is Python? How does Colab work? Try things out safely |
| 1 | `01_welcome_colab.ipynb` | Data handling basics: loading, summarising, exploring structure |
| 2 | `02_analysis_basics.ipynb` | Distribution, transformation, correlation, Table 1, simple regression |
| 3 | `03_confounders_colliders.ipynb` | Confounding, colliders, DAGs, model comparisons |
| 4 | `04_survival_analysis.ipynb` | Kaplan–Meier, Cox regression, survival curves |

---

## 📦 Setup (for local use)

If you'd rather work locally (optional):

```bash
git clone git@github.com:ggkuhnle/FB2NEP_datascience.git
cd FB2NEP_datascience
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

---

## 🔬 Dataset

The dataset is **synthetic** but statistically realistic. It includes demographic and health-related variables relevant for public health nutrition.

You can regenerate it using the script in `scripts/generate_dataset.py` with the fixed seed `11088` (MW of Ribonuclease T1).

---

## 👤 Author

This material is developed and maintained by [Gunter Kuhnle](https://www.reading.ac.uk/), Professor of Nutrition and Food Science, University of Reading.

---

## 📝 Licence

MIT Licence. See `LICENSE.md`.
