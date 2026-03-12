import pandas as pd
import pickle
import matplotlib.pyplot as plt

data = pd.read_csv("cars.csv")

data["Car_Age"] = 2024 - data["Year"]

data.drop(["Car_Name","Year"],axis=1,inplace=True)

model = pickle.load(open("car_model.pkl","rb"))

X = data.drop("Selling_Price",axis=1)

importance = model.feature_importances_

plt.barh(X.columns,importance)
plt.title("Feature Importance for Car Price Prediction")
plt.show()