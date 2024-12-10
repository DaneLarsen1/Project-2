import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV data
file_path = "your_file.csv"
data = pd.read_csv(file_path)

# Quick overview
print(data.info())
print(data.head())

# Summary statistics
print(data.describe())

# Graph of fare amounts
plt.figure(figsize=(8, 6))
sns.histplot(data['fare_amount'], bins=30, kde=True)
plt.title('Distribution of Fare Amounts')
plt.xlabel('Fare Amount')
plt.ylabel('Frequency')
plt.show()
