#Gráfico 3 - Lacunas no tratamento de Depressão e Ansiedade em adultos.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'D:\\Users\\wessi\\Documents\\projetoaplicadomackenzie\\database\\5- anxiety-disorders-treatment-gap.csv'
df_treatment = pd.read_csv(file_path)

# Calculate the total treatment gap for each year
df_treatment['Total Treatment Gap'] = df_treatment['Untreated, conditional']

# Group by year and find the mean total treatment gap
treatment_gap_by_year = df_treatment.groupby('Year')['Total Treatment Gap'].mean()

# Find the year with the highest treatment gap
year_highest_gap = treatment_gap_by_year.idxmax()
highest_gap = treatment_gap_by_year.max()

print(f"The year with the highest total treatment gap for anxiety disorders is {year_highest_gap} with a gap of {highest_gap:.2f}%")


# Plot the total treatment gap over the years
plt.figure(figsize=(10, 6))
plt.plot(treatment_gap_by_year.index, treatment_gap_by_year.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Mean Total Treatment Gap (%)')
plt.title('Total Treatment Gap for Anxiety Disorders Over Time')
plt.grid(True)
plt.xticks(treatment_gap_by_year.index)
plt.show()