
# Gráfico 5 - Relação entre diferentes tipos de tratamento no transtorno de ansiedade

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'D:\\Users\\wessi\\Documents\\projetoaplicadomackenzie\\database\\5- anxiety-disorders-treatment-gap.csv'
df = pd.read_csv(file_path)

# Ensure 'Year' column is numeric
df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

# Group data by year and calculate the mean treatment gap
treatment_gap_by_year = df.groupby('Year').agg(
    {'Potentially adequate treatment, conditional': 'mean',
     'Other treatments, conditional': 'mean',
     'Untreated, conditional': 'mean'}
)


# Plotting
plt.figure(figsize=(10, 6))

plt.plot(treatment_gap_by_year.index, treatment_gap_by_year['Potentially adequate treatment, conditional'], label='Potentially Adequate Treatment', marker='o')
plt.plot(treatment_gap_by_year.index, treatment_gap_by_year['Other treatments, conditional'], label='Other Treatments', marker='s')
plt.plot(treatment_gap_by_year.index, treatment_gap_by_year['Untreated, conditional'], label='Untreated', marker='x')

plt.xlabel('Year')
plt.ylabel('Percentage of Population')
plt.title('Treatment Gap for Anxiety Disorders Over Time')
plt.legend()
plt.grid(True)
plt.xticks(treatment_gap_by_year.index)  # Ensure all years are shown on x-axis
plt.show()