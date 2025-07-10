import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'sample_data.csv')

# Load the CSV file
df = pd.read_csv(csv_path)

# Ensure Salary and Age are numeric (in case CSV has bad data)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Drop rows with NaN values (optional: for safety)
df.dropna(subset=['Salary', 'Age'], inplace=True)

# Calculate the average salary
average_salary = df['Salary'].mean()
print(f"Average Salary: {average_salary:.2f}")

# Bar chart: Average salary by department
plt.figure(figsize=(8, 5))
department_salary = df.groupby('Department')['Salary'].mean().sort_values()
department_salary.plot(kind='bar', color='skyblue')
plt.title('Average Salary by Department')
plt.ylabel('Average Salary')
plt.xlabel('Department')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'bar_chart_avg_salary_by_department.png'))
plt.show()

# Scatter plot: Age vs Salary
plt.figure(figsize=(8, 5))
plt.scatter(df['Age'], df['Salary'], c='green')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'scatter_age_vs_salary.png'))
plt.show()

# Heatmap: Correlation matrix
plt.figure(figsize=(6, 4))
numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'correlation_heatmap.png'))
plt.show()

# Insights
print("\nInsights:")
print(f"- The average salary across all employees is ₹{average_salary:.2f}.")
print(f"- The department with the highest average salary is {department_salary.idxmax()} (₹{department_salary.max():.2f}).")
print(f"- The department with the lowest average salary is {department_salary.idxmin()} (₹{department_salary.min():.2f}).")
print("- The scatter plot shows the relationship between age and salary.")
print("- The heatmap visualizes correlations between numerical features.")
