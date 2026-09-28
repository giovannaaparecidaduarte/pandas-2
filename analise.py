import pandas as pd 

#lendo a planilha excel
df=pd.read_csv('dados_alunos_escola.xlsx - Sheet1.csv')

print(df) #leitura da planilha inteira

# 1. vizualizar as primeiras linhas 
print(df.head()) #exibe as primeiras linhas do dataframe

# 2. verificar o resumo estatistico (medias, minimos, maximos)
#print(df.describe()) 

# 3. ver os tipos de dados e se há valores nulos
print(df.info())