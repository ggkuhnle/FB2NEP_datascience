import pandas as pd
import numpy as np

np.random.seed(11088)

n = 1000
data = pd.DataFrame({
    "id": range(1, n + 1),
    "age": np.random.normal(55, 10, n).round().astype(int),
    "sex": np.random.choice(["female", "male"], n),
    "BMI": np.random.normal(27, 4, n).round(1),
    "smoking_status": np.random.choice(["never", "former", "current"], n, p=[0.5, 0.3, 0.2]),
    "physical_activity": np.random.choice(["active", "inactive"], n, p=[0.6, 0.4]),
    "nutrient_intake": np.random.lognormal(mean=np.log(20), sigma=0.5, size=n).round(1),
    "social_class": np.random.choice(["ABC1", "C2DE"], n, p=[0.6, 0.4]),
    "risk_factor_1": np.random.choice([0, 1], n, p=[0.8, 0.2]),
    "risk_factor_2": np.random.choice([0, 1], n, p=[0.7, 0.3]),
})

log_odds = (
    0.03 * data["age"] +
    0.05 * (data["sex"] == "male").astype(int) +
    0.04 * data["BMI"] +
    0.3 * (data["smoking_status"] == "current").astype(int) +
    0.2 * (data["physical_activity"] == "inactive").astype(int) +
    0.02 * data["nutrient_intake"] +
    0.25 * data["risk_factor_1"] +
    0.4 * data["risk_factor_2"] -
    10
)
prob = 1 / (1 + np.exp(-log_odds))
data["disease"] = np.random.binomial(1, prob)

data.to_csv("fb2nep_data.csv", index=False)
