# 📈 Machine Learning Task 1 (2026)
## Sales & Demand Forecasting for Businesses

This project is part of **Machine Learning Task 1 (2026)** by **Future Interns**.  
The objective is to build a **sales or demand forecasting system** using historical business data and present the results in a **clear, business-friendly way**.

---

## 🔍 Project Overview

Sales forecasting is one of the most widely used Machine Learning applications in real businesses.  
Companies rely on forecasts to:

- Plan inventory  
- Manage cash flow  
- Prepare staffing  
- Avoid overstocking or losses  

This project focuses on applying Machine Learning to **support real business decisions**, not just model training.

---

## 🎯 Objective

- Predict future sales based on historical data  
- Identify trends and seasonality in sales  
- Visualize forecasts clearly for non-technical stakeholders  
- Demonstrate how forecasting helps business planning  

---

## 🛠 Tools & Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Statsmodels  
- Matplotlib  

---

## 📁 Dataset

**Store Sales – Time Series Forecasting (Kaggle)**  
https://www.kaggle.com/competitions/store-sales-time-series-forecasting  

> The dataset is not included in this repository due to GitHub file size limits.  
> Please download `train.csv` from Kaggle and place it in the project directory before running the code.

---

## ⚙️ Workflow

1. Load and clean historical sales data  
2. Aggregate daily sales to form a time series  
3. Handle missing dates using forward filling  
4. Train a time-series forecasting model  
5. Evaluate predictions using error metrics  
6. Visualize historical sales and future forecasts  

---

## 📊 Outputs

- **Sales Forecast Visualization**  
- **Future Sales Predictions (CSV)**  
- **Model Evaluation Metrics (MSE, MAPE)**  

These outputs are designed to be **easy to understand for business users**.

---

## ▶ How to Run the Project

```bash
python forecast.py