# AI-Assisted Dynamic Power Estimation of an 8-bit ALU

This project demonstrates an end-to-end **VLSI + Artificial Intelligence workflow** where real switching activity from a Verilog-based ALU is used to **train Machine Learning models for dynamic power estimation**. The complete flow includes RTL design, simulation, data extraction, ML model training, and visualization.

---

## 🔧 Tools & Technologies
- Verilog HDL  
- Xilinx Vivado  
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  

---

## 🧠 Project Workflow

1. Designed an **8-bit ALU** in Verilog HDL.
2. Verified functionality using a **self-written random testbench** in Xilinx Vivado.
3. Extracted **per-cycle switching activity** including:
   - Bit-level output toggle count  
   - Hamming weight of input operands  
4. Logged simulation data into `activity.csv`.
5. Built Machine Learning models in Python:
   - Linear Regression (baseline)
   - Random Forest Regression (non-linear model)
6. Predicted **dynamic power consumption** from RTL activity data.
7. Visualized **actual vs predicted power** using Matplotlib.

---

## 📊 Machine Learning Approach

Dynamic power is modeled using the relation:

\[
P_{dyn} \approx C \times V^2 \times f \times Activity
\]

Where activity is derived from:
- Output toggle count  
- Operand Hamming weights  

A synthetic but realistic power label is generated and used to train:
- Linear Regression
- Random Forest Regressor  

Both models are evaluated using:
- **R² Score**
- **Mean Squared Error (MSE)**

---

## ✅ Results

- Achieved **very high prediction accuracy** with Random Forest regression.
- Generated **Actual vs Predicted Power plots** for visual evaluation.
- Demonstrated that **Machine Learning can accurately estimate power at RTL level** using switching activity.

---

## 🧪 RTL & Simulation

- `alu.v` – 8-bit ALU RTL design in Verilog  
- `alu_tb.v` – Clocked random testbench with per-cycle activity logging  
- `simulation_waveform.png` – Vivado waveform screenshot for functional verification  

The ALU was simulated using **Vivado Behavioral Simulation**, and toggle-based activity was captured at every clock cycle.

---

## 📁 Project Files

| File Name | Description |
|-----------|-------------|
| `alu.v` | Verilog RTL of 8-bit ALU |
| `alu_tb.v` | Testbench with activity logging |
| `activity.csv` | Switching activity dataset from simulation |
| `power_ml.py` | Basic ML power estimation |
| `power_ml_advanced.py` | Advanced ML with feature engineering |
| `power_ml_plot.py` | Visualization script using Matplotlib |
| `linear_real_vs_pred.png` | Actual vs Predicted plot (Linear Regression) |
| `rf_real_vs_pred.png` | Actual vs Predicted plot (Random Forest) |
| `simulation_waveform.png` | Verification waveform screenshot |

---

## 🚀 Key Outcomes

- Demonstrated **AI-assisted RTL-level power estimation**
- Implemented **feature engineering from switching activity**
- Compared **linear vs non-linear regression models**
- Visualized model performance using **professional plots**
- Built a **complete industry-style VLSI + AI pipeline**

---

## 👨‍💻 Author

**Dasari Santhan Reddy**  
B.Tech | VLSI & AI Enthusiast  
GitHub: *(https://github.com/santhanreddy820)*  
LinkedIn: *(www.linkedin.com/in/dasari-santhan-reddy-032a7a259)*  

---

## 📜 License

This project is for academic and learning purposes.
