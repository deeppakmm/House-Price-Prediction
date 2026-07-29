from flask import Flask, render_template, request
from predict import predict_house_price


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    predicted_price = None

    if request.method == "POST":
        user_input = {

            "OverallQual": int(request.form["OverallQual"]),
            "GrLivArea": int(request.form["GrLivArea"]),
            "GarageCars": int(request.form["GarageCars"]),
            "GarageArea": int(request.form["GarageArea"]),
            "TotalBsmtSF": int(request.form["TotalBsmtSF"]),
            "1stFlrSF": int(request.form["1stFlrSF"]),
            "2ndFlrSF": int(request.form["2ndFlrSF"]),
            "YearBuilt": int(request.form["YearBuilt"]),
            "FullBath": int(request.form["FullBath"]),
            "TotRmsAbvGrd": int(request.form["TotRmsAbvGrd"]),
            "LotArea": int(request.form["LotArea"]),
            "BsmtFinSF1": int(request.form["BsmtFinSF1"]),
            "Fireplaces": int(request.form["Fireplaces"]),

            "Neighborhood": request.form["Neighborhood"],
            "KitchenQual": request.form["KitchenQual"],
            "GarageType": request.form["GarageType"],
            "GarageFinish": request.form["GarageFinish"],
            "CentralAir": request.form["CentralAir"],
            "LotShape": request.form["LotShape"],
            "RoofStyle": request.form["RoofStyle"]

        }

        predicted_price = predict_house_price(user_input)

        

    return render_template(
    "index.html",
    predicted_price=predicted_price
)


if __name__ == "__main__":
    app.run(debug=True)