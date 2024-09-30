import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'D:\\Users\\wessi\\Documents\\projetoaplicadomackenzie\\database\\4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv'
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do dataset
print(df.head())

# Verificar se há dados ausentes
print(df.isnull().sum())

# Visualizar a prevalência de doenças mentais por país
plt.figure(figsize=(10, 6))
new_var = sns.barplot(x='Entity', y='Code', data=df)
plt.xticks(rotation=90)
plt.title('Prevalência de Doenças Mentais por País')
plt.show()

# Verificar correlações
numerical_df = df.select_dtypes(include=['number'])
correlation_matrix = numerical_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()
