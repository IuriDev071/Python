# Não mexe aqui
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo_excel_1 = 'Médias.xlsx'
arquivo_excel_2 = 'Soma.xlsx'

#  Caso for usar um terceiro ou quarto arquivo remova a Hashtag
# arquivo_excel_3 = 'Exemplo1.xlsx'

df_planilha_1 = pd.read_excel(arquivo_excel_1, sheet_name='média')
df_planilha_2 = pd.read_excel(arquivo_excel_2, sheet_name='soma')

#  Caso for usar o terceiro ou quarto arquivo remova a Hashtag
# df_planilha_3 = pd.read_excel(arquivo_excel_2, sheet_name='teste')

# Adicionar df_planilha_3 depois de uma virgula caso for usar uma terceiraplanilha
df_todas_as_planilhas = pd.concat([df_planilha_1, df_planilha_2])

planilha_todos = df_todas_as_planilhas.groupby(['Nome'])

relatorio_top = planilha_todos.loc[:, "Nome":"Média"]

print(relatorio_top)