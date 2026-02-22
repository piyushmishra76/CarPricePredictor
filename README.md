# CarPricePredictor
🚗 Car Price Predictor (Machine Learning Project)

This project predicts the resale price of a used car using machine learning techniques.
The model learns patterns from historical car data(small data) such as namw, year, fuel type, and kilometers driven to estimate the expected market price.

📌 Problem Statement

Buying or selling a used car often involves uncertainty in pricing.
This project aims to build a regression model that can estimate a car’s resale value based on its features.

🧠 ML Approach

The following steps were followed:

Data cleaning and preprocessing

Handling categorical variables using OneHotEncoding

Log transformation of target variable to reduce skewness

Model training using regression algorithms

Model evaluation using R² score

Pipeline creation for reproducible preprocessing + prediction

⚙️ Tech Stack

Python

Pandas & NumPy

Scikit-learn

Streamlit (for UI)

Pickle / Joblib (model saving)

📊 Features Used

Car Name

Company

Manufacturing Year

Kilometers Driven

Fuel Type

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/piyushmishra76/CarPricePredictor.git
cd CarPricePredictor
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit app
streamlit run app.py

The app will open in your browser.

🎯 Model Output

The model predicts the resale price of the car in INR.
Since the model was trained on log-transformed prices, predictions are converted back using exponential transformation.
