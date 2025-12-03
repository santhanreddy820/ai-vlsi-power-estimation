import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# ========== 1. LOAD DATA ==========
df = pd.read_csv("activity.csv")

# ========== 2. CREATE REALISTIC POWER LABEL ==========
V = 1.0
f = 100e6
C_bit = 1e-15

base_activity = df["toggles"] + 0.5*df["hw_a"] + 0.5*df["hw_b"]
ideal_power_w = C_bit * (V**2) * f * base_activity

noise = np.random.normal(scale=0.1 * ideal_power_w.std(), size=len(df))
df["power_mw"] = (ideal_power_w + noise) * 1e3

# ========== 3. FEATURE ENGINEERING ==========
op_dummies = pd.get_dummies(df["op"], prefix="op")

X = pd.concat(
    [df[["a", "b", "y", "toggles", "hw_a", "hw_b"]], op_dummies],
    axis=1
)

y = df["power_mw"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ========== 4. TRAIN MODELS ==========
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred_lin = lin.predict(X_test)

rf = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# ========== 5. METRICS ==========
print("\nLinear Regression:")
print("R2  :", r2_score(y_test, y_pred_lin))
print("MSE :", mean_squared_error(y_test, y_pred_lin))

print("\nRandom Forest:")
print("R2  :", r2_score(y_test, y_pred_rf))
print("MSE :", mean_squared_error(y_test, y_pred_rf))

# ========== 6. PLOT: REAL vs PREDICTED (LINEAR) ==========
plt.figure()
plt.scatter(y_test, y_pred_lin)
plt.xlabel("Actual Power (mW)")
plt.ylabel("Predicted Power (mW)")
plt.title("Actual vs Predicted Power - Linear Regression")
plt.grid(True)
plt.savefig("linear_real_vs_pred.png", dpi=300)
plt.show()

# ========== 7. PLOT: REAL vs PREDICTED (RANDOM FOREST) ==========
plt.figure()
plt.scatter(y_test, y_pred_rf)
plt.xlabel("Actual Power (mW)")
plt.ylabel("Predicted Power (mW)")
plt.title("Actual vs Predicted Power - Random Forest")
plt.grid(True)
plt.savefig("rf_real_vs_pred.png", dpi=300)
plt.show()

# ========== 8. OPTIONAL: ERROR DISTRIBUTION ==========
errors = y_test - y_pred_rf

plt.figure()
plt.hist(errors, bins=30)
plt.xlabel("Prediction Error (mW)")
plt.ylabel("Count")
plt.title("Prediction Error Distribution (Random Forest)")
plt.grid(True)
plt.savefig("rf_error_distribution.png", dpi=300)
plt.show()
