#Gráfico 4 - Correlação entre os Transtornos de saúde mental

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'D:\\Users\\wessi\\Documents\\projetoaplicadomackenzie\\database\\4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv'
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do dataset
print(df.head())

# Verificar se há dados ausentes
print(df.isnull().sum())

# Verificar correlações
numerical_df = df.select_dtypes(include=['number'])
correlation_matrix = numerical_df.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()
