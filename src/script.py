import requests
import pandas as pd
import numpy as np

url = "https://api.themoviedb.org/3/discover/movie"

headers = {
    "Authorization": "", #API KEY
    "accept": "application/json",
}


lista_para_tabela = []

for pagina in range(1,4):
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
      lista_para_tabela.append({
          "Título": filme.get("title"),
          "Data de Lançamento": filme.get("release_date"),
          "Popularidade": filme.get("popularity"),
          "Média de Votos": filme.get("vote_average"),
          "ID": filme.get("id"),
      })


df = pd.DataFrame(lista_para_tabela)

orcamentos = []

for id_filme in df["ID"]:

    url_detalhes = f"https://api.themoviedb.org/3/movie/{id_filme}"

    response = requests.get(
        url_detalhes,
        headers=headers,
        params={"language": "en-US"}
    )

    response.raise_for_status()

    detalhes = response.json()

    dolares = {f"${detalhes.get('budget', 0)}"}

    orcamentos.append(dolares)



df["budget"] = orcamentos

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_rows", None)


print(df)
print(f"\nTotal de filmes na tabela: {len(df)}")