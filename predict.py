import joblib
import pandas as pd

# Load Trained Model
model = joblib.load("models/xgboost_house_price_model_v2.pkl")

# Load Training Columns
model_columns = joblib.load("models/model_columns_v2.pkl")


def predict_house_price(user_input):

    # Convert dictionary to DataFrame
    input_df = pd.DataFrame([user_input])

    # Reindex according to training columns
    input_df = input_df.reindex(
        columns=model_columns,
        fill_value=0
    )

    # Predict
    prediction = model.predict(input_df)

    return round(prediction[0], 2)