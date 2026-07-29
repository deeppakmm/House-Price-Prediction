# 🏠 House Price Prediction using Machine Learning & Flask

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Regressor-green)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

# 📌 Project Overview

This project predicts house prices using Machine Learning based on various house features such as quality, living area, basement size, garage details, construction year, and location.

The project follows the complete Machine Learning workflow:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Feature Selection
- Model Training
- Model Evaluation
- Model Saving
- Flask Web Application
- Real-time House Price Prediction

Unlike a notebook-only project, this application also includes a **Flask-based web interface** where users can enter house details and receive predicted prices instantly.

---

# 🚀 Live Demo

> **Coming Soon (Render Deployment)**

---

# 📂 Dataset

Dataset used:

**House Prices – Advanced Regression Techniques (Kaggle)**

Dataset contains information such as:

- Overall Quality
- Living Area
- Basement Area
- Garage Details
- Lot Area
- Construction Year
- Neighborhood
- Kitchen Quality
- Roof Style
- Many other housing features

Dataset Size

- Training Samples: **1460**
- Original Features: **81**

---

# 🔍 Exploratory Data Analysis (EDA)

Performed:

- Dataset inspection
- Statistical summary
- Missing value analysis
- Target variable visualization
- Outlier detection
- Correlation Heatmap
- Feature relationship analysis
- Feature importance visualization

---

# 🧹 Data Preprocessing

The following preprocessing steps were applied:

- Removed unnecessary columns (>80% missing values)
- Filled numerical missing values using Median
- Filled categorical missing values using Mode / "None"
- One-Hot Encoding for categorical variables
- Feature alignment for prediction

After preprocessing:

- Original Features → **81**
- Encoded Features → **248**

---

# 🤖 Machine Learning Models

Three regression models were trained and evaluated.

| Model | R² Score |
|------|----------:|
| Linear Regression | 0.640 |
| Random Forest Regressor | 0.886 |
| ⭐ XGBoost Regressor | **0.912** |

The **XGBoost Regressor** achieved the highest prediction accuracy and was selected as the final production model.

---

# 📊 Model Evaluation

Evaluation Metrics used:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Final XGBoost Performance

| Metric | Value |
|---------|-------:|
| MAE | 16,935 |
| MSE | 677,089,856 |
| RMSE | 26,020 |
| R² Score | **0.912** |

---

# ⭐ Important Features

Top features influencing house prices:

- OverallQual
- GrLivArea
- TotalBsmtSF
- 2ndFlrSF
- BsmtFinSF1
- 1stFlrSF
- LotArea
- GarageArea
- YearBuilt
- GarageCars

These features have the strongest impact on predicting house prices.

---

# 🌐 Web Application

The project also includes a Flask web application.

Users can:

- Enter house details
- Click **Predict Price**
- Get real-time predicted house price

Current workflow:

```
User

↓

HTML Form

↓

Flask Backend

↓

XGBoost Model

↓

Predicted Price
```

---

# 💾 Saved Models

Final trained models:

```
models/
│
├── xgboost_house_price_model_v2.pkl
└── model_columns_v2.pkl
```

---

# 📁 Project Structure

```
House_Price_Prediction/

│
├── app.py
├── predict.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── sample_submission.csv
│
├── models/
│   ├── xgboost_house_price_model_v2.pkl
│   └── model_columns_v2.pkl
│
├── notebooks/
│   └── House_Price_Prediction.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- XGBoost
- Flask
- HTML
- CSS
- Joblib

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/your-username/House_Price_Prediction.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open browser

```
http://127.0.0.1:5000
```

---

# 🚀 Future Improvements

- Deploy on Render
- Improve UI using JavaScript (AJAX) to avoid page reload
- Add prediction confidence score
- Improve model accuracy through hyperparameter tuning
- Add more input validation
- Make the application fully responsive

---

# 👨‍💻 Author

**Deepak Maurya**

Aspiring Data Scientist | Machine Learning Enthusiast
