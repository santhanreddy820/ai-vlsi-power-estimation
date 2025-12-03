import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# 1. Load the advanced activity data
df = pd.read_csv("activity.csv")

# Check the first few rows (optional)
print(df.head())

# 2. Build a more realistic synthetic power label
#    P_dyn ~ C_eff * V^2 * f * (toggles + hw_a + hw_b)
V = 1.0      # volts
f = 100e6    # 100 MHz
C_bit = 1e-15  # base capacitance per bit

base_activity = df["toggles"] + 0.5*df["hw_a"] + 0.5*df["hw_b"]
ideal_power_w = C_bit * (V**2) * f * base_activity

# add some noise so the mapping isn't perfectly linear
noise = np.random.normal(scale=0.1 * ideal_power_w.std(), size=len(df))
df["power_mw"] = (ideal_power_w + noise) * 1e3  # W -> mW

# 3. Feature engineering
# one-hot encode 'op' (0..4 -> op_0, op_1, ...)
op_dummies = pd.get_dummies(df["op"], prefix="op")

X = pd.concat(
    [
        df[["a", "b", "y", "toggles", "hw_a", "hw_b"]],
        op_dummies,
    ],
    axis=1,
)
y = df["power_mw"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Linear Regression model
lin = LinearRegression()
lin.fit(X_train, y_train)
y_pred_lin = lin.predict(X_test)

# 5. Random Forest model (non-linear regressor)
rf = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

def report(name, y_true, y_pred):
    print(f"\n{name}")
    print("  R2  :", r2_score(y_true, y_pred))
    print("  MSE :", mean_squared_error(y_true, y_pred))

report("LinearRegression", y_test, y_pred_lin)
report("RandomForestRegressor", y_test, y_pred_rf)
