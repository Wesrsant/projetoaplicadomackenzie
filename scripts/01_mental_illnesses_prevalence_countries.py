#Gráfico 1 - Taxa de transtornos mentais por país.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'D:\\Users\\wessi\\Documents\\projetoaplicadomackenzie\\database\\1- mental-illnesses-prevalence.csv'
df = pd.read_csv(file_path)

# Find the most recent year
most_recent_year = df['Year'].max()

# Filter data for the most recent year
df_recent = df[df['Year'] == most_recent_year]

# Define mental health disorders to include in the plot
disorders = [
    'Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized',
    'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized',
    'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized',
    'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized',
    'Eating disorders (share of population) - Sex: Both - Age: Age-standardized'
]

# Sort by the sum of disorder rates
df_sorted = df_recent.sort_values(by=disorders, ascending=False).head(10)

# Create the plot
plt.figure(figsize=(14, 8))
for disorder in disorders:
  sns.barplot(x='Entity', y=disorder, data=df_sorted, label=disorder.split(' (')[0])

plt.xlabel("Country")
plt.ylabel("Prevalence Rate (%)")
plt.title(f"Top 10 Countries with Highest Rates of Mental Health Disorders ({most_recent_year})")
plt.xticks(rotation=45, ha='right')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Move the legend outside the plot
plt.tight_layout()
plt.show()