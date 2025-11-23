import pandas as pd

# Create sample data
data = {
    'TransactionID': [1001, 1002, 1003, 1004, 1005],
    'ProductCategory': ['Electronics', 'Books', 'Apparel', 'Books', 'Electronics'],
    'Price': [499.99, 12.50, 75.00, 22.95, 1200.00],
    'UnitsSold': [5, 20, 15, 8, 3],
    'OrderDate': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-03', '2023-10-04'],
    'IsDiscounted': [True, False, True, False, True]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print first 5 rows
print("--- Original DataFrame Head (First 5 Rows) ---")
print(df.head())

print("\n" + "="*50 + "\n")

# Print data types of columns
print("--- Column Data Types (from .dtypes) ---")
print(df.dtypes)

print("\n" + "="*50 + "\n")

# Print dataframe info summary
print("--- DataFrame Summary (.info() method) ---")
df.info()
