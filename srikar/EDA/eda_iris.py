import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD DATA
# Update the path to match where your Iris.csv file is saved on your computer
df = pd.read_csv(r"C:\Users\YERRA SRIKAR\Downloads\archive\Iris.csv")

# 2. DATA CLEANING & STRUCTURE CHECKS
print("--- DATA SUMMARY ---")
print(f"Shape: {df.shape}")
print(f"Missing Values:\n{df.isnull().sum()}\n")
print(f"Duplicates: {df.duplicated().sum()}\n")

# 3. STATISTICAL OVERVIEW
print("--- NUMERICAL STATS ---")
print(df.describe().T[['mean', 'std', 'min', '50%', 'max']])

print("\n--- CLASS DISTRIBUTION ---")
print(df['Species'].value_counts())

# 4. VISUALIZATIONS
# Plot 1: Target Class Bar Chart
plt.figure(figsize=(6, 4))
df['Species'].value_counts().plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title('Species Count')
plt.xlabel('Species')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Plot 2: Sepal Length vs Petal Length Scatter
plt.figure(figsize=(6, 4))
colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'blue', 'Iris-virginica': 'green'}

for species, group in df.groupby('Species'):
    plt.scatter(group['SepalLengthCm'], group['PetalLengthCm'], label=species, color=colors[species], alpha=0.8)

plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

# Plot 3: Petal Length Distribution Histogram
plt.figure(figsize=(6, 4))
plt.hist(df['PetalLengthCm'], bins=15, color='purple', edgecolor='black', alpha=0.7)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()