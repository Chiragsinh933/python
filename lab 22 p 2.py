import pandas as pd
import numpy as np

# Sample data with NaN (missing value) in 'UnitsSold'
data = {
    'TransactionID': [1001, 1002, 1003, 1004, 1005],
    'ProductCategory': ['Electronics', 'Books', 'Apparel', 'Books', 'Electronics'],
    'Price': [499.99, 12.50, 75.00, 22.95, 1200.00],
    'UnitsSold': [5, 20, np.nan, 8, 3],   # Introduced a missing value
    'OrderDate': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-03', '2023-10-04'],
    'IsDiscounted': [True, False, True, False, True]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame with missing value
print("--- DataFrame Head with Missing Value (Row Index 2) ---")
print(df.head())
print("\n" + "="*50 + "\n")

# Show data types
print("--- Column Data Types ---")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# Impute missing value with mean of 'UnitsSold'
mean_units_sold = df['UnitsSold'].mean()
print(f"Calculated Mean of 'UnitsSold': {mean_units_sold:.2f}")
df['UnitsSold'].fillna(mean_units_sold, inplace=True)

# Show DataFrame after imputation
print("\n--- DataFrame after Imputing NaN with Mean ---")
print(df)
