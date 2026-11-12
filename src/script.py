import numpy as np
import pandas as pd
import requests

lista_para_tabela = []


def obter_orcamento(id_filme):
  url = f"https://api.themoviedb.org/3/movie/{id_filme}"

  headers = {
      "Authorization": "Bearer ",
      "accept": "application/json",
  }

  response = requests.get(url, headers=headers, params={"language": "en-US"})

  if response.status_code == 200:
    detalhes = response.json()
    budget = detalhes.get("budget", 0)
    return f"US$ {budget:,}"

  return "US$ 0"



def puxar_dados_filmes(pagina):
  url = "https://api.themoviedb.org/3/discover/movie"

  headers = {
      "Authorization": "Bearer ",
      "accept": "application/json",
  }

  params = {
      "include_adult": "false",
      "include_video": "false",
      "language": "en-US",
      "page": pagina,
      "primary_release_date.gte": "2010-10-31",
      "primary_release_date.lte": "2026-10-31",
      "sort_by": "popularity.desc",
  }

  response = requests.get(url, headers=headers, params=params)

  if response.status_code == 200:
    dados = response.json()
    filmes = dados.get("results", [])

    for filme in filmes:
      id_f = filme.get("id")
      lista_para_tabela.append({
          "Título": filme.get("title"),
          "Data de Lançamento": filme.get("release_date"),
          "Popularidade": filme.get("popularity"),
          "Média de Votos": filme.get("vote_average"),
          "ID": id_f,
          "Orçamento": obter_orcamento(id_f),
      })
  else:
    print(f"Erro ao obter dados na página {pagina}")


for pagina in range(1, 3):
  puxar_dados_filmes(pagina)
  print(f"Página {pagina} carregada.")

df = pd.DataFrame(lista_para_tabela)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

print("\n--- TABELA FINAL ---")
print(df)

