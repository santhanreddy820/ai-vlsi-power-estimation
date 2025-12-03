# AI-Assisted Dynamic Power Estimation of 8-bit ALU

This project demonstrates an end-to-end VLSI + AI workflow where switching activity from a Verilog-based ALU is used to predict dynamic power using Machine Learning.

## 🔧 Tools & Technologies
- Verilog HDL
- Xilinx Vivado
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

## 🧠 Project Workflow
1. Designed and simulated an 8-bit ALU in Verilog using Vivado.
2. Extracted per-cycle switching activity (toggle count & Hamming weight).
3. Generated `activity.csv` from RTL simulation.
4. Built Machine Learning models:
   - Linear Regression
   - Random Forest Regression
5. Predicted dynamic power consumption.
6. Visualized actual vs predicted power using Matplotlib.

## 📊 Results
- High prediction accuracy achieved.
- Real vs Predicted Power plots generated.

## 📁 Files
- `power_ml.py` – Basic ML model
- `power_ml_advanced.py` – Advanced ML pipeline
- `power_ml_plot.py` – Visualization script
- `activity.csv` – Switching activity data
- `*.png` – Result plots

## ✅ Outcome
Demonstrated AI-assisted RTL-level power estimation using switching activity from hardware simulation.
