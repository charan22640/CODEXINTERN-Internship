import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
import numpy as np
import os

# Load the dataset
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'sample_house_data.csv')
df = pd.read_csv(csv_path)

# Preprocessing: One-hot encode 'Location'
encoder = OneHotEncoder(drop='first')
location_encoded = encoder.fit_transform(df[['Location']]).toarray()
location_cols = encoder.get_feature_names_out(['Location'])

# Combine all features
features = pd.concat([
    df[['Rooms', 'Size', 'YearBuilt']].reset_index(drop=True),
    pd.DataFrame(location_encoded, columns=location_cols)
], axis=1)
target = df['Price']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Linear Regression Model for House Price Prediction")
print("----------------------------------------------")
print(f"Test RMSE: {rmse:.2f}")
print(f"Test R^2 Score: {r2:.2f}")
print("\nSample Predictions:")
for i, (true, pred) in enumerate(zip(y_test.values, y_pred)):
    print(f"Actual: {true:.0f}, Predicted: {pred:.0f}") 