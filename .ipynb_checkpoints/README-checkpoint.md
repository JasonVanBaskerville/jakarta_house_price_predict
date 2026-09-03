# 🏠 House Price Prediction

A machine learning project to predict house prices in Jakarta, Indonesia, based on property characteristics.

## 🚀 Live Demo

### 📊 Analyst Dashboard

An interactive dashboard for exploring and analyzing data on house features and prices.

👉 **[Open Analyst Dashboard](https://analystdashboard-jakartahouseprice-ecbnspyrdpwxskuyjwz3xg.streamlit.app/)**

### 🏠 House Price Prediction

An application to predict house prices based on property characteristics.

👉 **[Open House Price Prediction App](https://jakartahousepricepredict-nzaj8lzsfxbf5zggboj9rs.streamlit.app/)**

---

## 📊 Features

### Analyst Dashboard

* Dataset overview
* House price distribution
* Price analysis by city
* Price analysis by district
* Building area vs. price
* Land area vs. price
* Bedrooms vs. price
* Bathrooms vs. price
* Carport vs. price
* Correlation analysis
* Interactive filtering

### Prediction App

You can enter:

* City
* District
* Number of bedrooms
* Number of bathrooms
* Carport
* Land area
* Building area

The application will then generate an estimated house price.

---

## 🛠️ Technologies

* Python
* Pandas
* Scikit-learn
* Plotly
* Streamlit
* Jupyter Notebook

---

## 📁 Project Structure

```text
house-price-prediction/
│
├── data/
│   └── jakarta_house.csv
│
├── notebook/
│   └── house_price.ipynb
│         └── model/
│              └── jakarta_house_price_predict.joblib
│
├── analyst_dashboard.py
├── app.py
├── requirements.txt
└── README.md
---

## ⚙️ How to Run Locally

Install dependencies:

1. Clone all files into a single folder
2. Open Jupyter Lab
3. Run all cells in `jakarta_house_price_predict.ipynb`
4. Open a terminal
5. Run: 
    streamlit run analyst_dashboard.py
    streamlit run app.py
7. Open the provided link
    Example: 
        Local URL: http://localhost:8504
        Network URL: http://192.168.0.8:8504
