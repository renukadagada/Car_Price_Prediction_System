import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("cars.csv")

# Show columns (for debugging)
print("Dataset Columns:", data.columns)

# Feature Engineering
data["Car_Age"] = 2024 - data["Year"]

# Drop unnecessary columns
data.drop(["Car_Name", "Year"], axis=1, inplace=True)

# Encode categorical columns
label = LabelEncoder()

data["Fuel_Type"] = label.fit_transform(data["Fuel_Type"])
data["Seller_Type"] = label.fit_transform(data["Seller_Type"])
data["Transmission"] = label.fit_transform(data["Transmission"])

# Features
X = data.drop("Selling_Price", axis=1)

# Target
y = data["Selling_Price"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=500,
    max_depth=12,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print("Model Accuracy (R2 Score):", score)

# Save Model
with open("car_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully as car_model.pkl")