import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt


def dados_filmes(df_filmes):
  api_key = "33657daf"
  filmes = []
  for titulo_filme in df_filmes["name"]:
    endpoint = f"http://www.omdbapi.com/?t={titulo_filme}&apikey={api_key}"
    dados_filme = requests.get(endpoint)

    if dados_filme.status_code == 200:
        filmes.append(dados_filme.json())

  df_final = pd.DataFrame(filmes)
  return df_final


def col_para_num(dataframe_filmes, coluna):
  dataframe_filmes[coluna] = pd.to_numeric(      #método para converter strings em colunas de um df em número
  (dataframe_filmes[coluna]                    
  .str.replace("$","")
  .str.replace(",","")), 
  errors="coerce")                                #argumento usado para adicionar NaN em dados inválidos
  
  return dataframe_filmes

def histograma_receita(dataframe,coluna):
   plt.figure(figsize=(10,6))
   sns.histplot(dataframe, x=coluna, bins=30)
   plt.title("Distribuição da Receita de Bilheteria")
   plt.xlabel("Receita da bilheteria (em milhões)")
   plt.ylabel("Quantidade de Filmes")
   plt.show()
