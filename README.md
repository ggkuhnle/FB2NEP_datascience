# 🧪 FB2NEP Datascience – Teaching Resources

This repository contains teaching materials and data analysis notebooks for the **FB2NEP** module on *Public Health Nutrition & Epidemiology* at the University of Reading.

These resources are designed to support the practical and quantitative components of the module. All work is done in Python (via Google Colab) using a realistic synthetic dataset.

---

## 📚 Contents

- `notebooks/`: Weekly Jupyter notebooks (Colab-compatible)
- `data/`: Synthetic dataset used throughout the module
- `scripts/`: Code to generate the dataset for transparency and reproducibility

Slides are distributed via **Blackboard** and are not included here.

---

## 🔗 Getting Started in Colab

> ⚠️ You do **not need to install anything** — all notebooks run in the browser using [Google Colab](https://colab.research.google.com).

### ▶️ Week 1: Welcome & Onboarding

📓 Notebook: [`00_playground.ipynb`](notebooks/01_playground.ipynb)
<a href="https://colab.research.google.com/github/ggkuhnle/FB2NEP_datascience/blob/main/notebooks/01_playground.ipynb" target="_blank">🚀 Open in Colab</a>

📓 Notebook: [`01_welcome_colab.ipynb`](notebooks/01_welcome_colab.ipynb)  
<a href="https://colab.research.google.com/github/ggkuhnle/FB2NEP_datascience/blob/main/notebooks/01_welcome_colab.ipynb" target="_blank">🚀 Open in Colab</a>

---

## 📁 Dataset

📄 [`data/fb2nep_data.csv`](data/fb2nep_data.csv)

This dataset simulates responses from 1,000 individuals, including variables like:

- `age`, `sex`, `BMI`, `social_class`
- `smoking_status`, `physical_activity`
- `nutrient_intake`, `risk_factor_1/2`
- Simulated binary `disease` outcome

🧬 The dataset is synthetic, generated using logistic modelling with a fixed seed for reproducibility.

---

## 🛠️ Reproducibility

To regenerate the dataset:

```bash
python scripts/generate_fb2nep_data.py
```

The script uses `numpy` and `pandas`, and is fully self-contained.

---

## 💡 License

All notebooks and scripts in this repository are shared under the **MIT License**.

---

## 🙋 Questions?

Contact Prof. Gunter Kuhnle or raise an issue in this repository.
