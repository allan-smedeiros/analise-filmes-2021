import pandas as pd
import funcoes

pd.options.display.float_format = "{:,.2f}".format

arquivo = pd.read_csv("IMDB Top 250 Movies.csv", usecols=["rank","name","year"])

dataframe_filmes = funcoes.dados_filmes(arquivo)

df_dados = funcoes.col_para_num(dataframe_filmes, "BoxOffice")

mediana = df_dados["BoxOffice"].median()

df_dados["BoxOffice"] = df_dados["BoxOffice"].fillna(mediana)

estatisticas_gerais = df_dados["BoxOffice"].describe()

print(estatisticas_gerais)

funcoes.histograma_receita(df_dados,"BoxOffice")

