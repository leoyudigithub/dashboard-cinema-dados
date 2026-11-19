#IMPORTS
import numpy as np
import pandas as pd
import requests

#LISTA PARA CARREGAR VARIAS PAGINAS
lista_para_tabela = []

#FUNÇAO QUE OBTEM ORÇAMENTO DO FILME
def obter_orcamento(id_filme):
  url = f"https://api.themoviedb.org/3/movie/{id_filme}"

  headers = {
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGZjMDNhNWY5ZmVjNTUzZTk0ZWE3NTQ1OTE1ZmFiMSIsIm5iZiI6MTc5NDA5MTczMi4zNzYsInN1YiI6IjZhZWZhYWQ0YjQ3YmY1MjA4MzBkMzU0ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KrfUs1hdrfWYV3HDO9gDFdmdy0AQ3-Z34t-fTGKlabA",
      "accept": "application/json",
  }

  response = requests.get(url, headers=headers, params={"language": "en-US"})

  if response.status_code == 200:
    detalhes = response.json()
    budget = detalhes.get("budget", 0)
    return f"US$ {budget:,}"

  return "US$ 0"

#OBTER BILHETERIA
def obter_bilheteria(id_filme):
  url = f"https://api.themoviedb.org/3/movie/{id_filme}"

  headers = {
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGZjMDNhNWY5ZmVjNTUzZTk0ZWE3NTQ1OTE1ZmFiMSIsIm5iZiI6MTc5NDA5MTczMi4zNzYsInN1YiI6IjZhZWZhYWQ0YjQ3YmY1MjA4MzBkMzU0ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KrfUs1hdrfWYV3HDO9gDFdmdy0AQ3-Z34t-fTGKlabA",
      "accept": "application/json",
  }

  response = requests.get(url, headers=headers, params={"language": "en-US"})

  if response.status_code == 200:
    detalhes = response.json()
    revenue = detalhes.get("revenue", 0)
    return f"US$ {revenue:,}"

  return "US$ 0"

#FUNCAO QUE OBTEM PAIS DE ORIGEM DO FILME
def obter_pais_origem(id_filme):
  url = f"https://api.themoviedb.org/3/movie/{id_filme}"
  
  headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGZjMDNhNWY5ZmVjNTUzZTk0ZWE3NTQ1OTE1ZmFiMSIsIm5iZiI6MTc5NDA5MTczMi4zNzYsInN1YiI6IjZhZWZhYWQ0YjQ3YmY1MjA4MzBkMzU0ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KrfUs1hdrfWYV3HDO9gDFdmdy0AQ3-Z34t-fTGKlabA",
        "accept": "application/json",
    }
  
  response = requests.get(url, headers=headers, params={"language": "en-US"})

  if response.status_code == 200:
    detalhes = response.json()
    pais_origem = detalhes.get("origin_country")

    def tratar_paises(pais):
      match pais[0]:
          case "US":
              return "Estados Unidos"
          case "IN":
              return "Índia"
          case "JP":
              return "Japão"
          case "CN":
              return "China"
          case "FR":
              return "França"
          case "GB":
              return "Reino Unido"
          case "KR":
              return "Coreia do Sul"
          case "CA":
              return "Canadá"
          case "DE":
              return "Alemanha"
          case "IT":
              return "Itália"
          case "ES":
              return "Espanha"
          case "BR":
              return "Brasil"
          case "MX":
              return "México"
          case "RU":
              return "Rússia"
          case "HK":
              return "Hong Kong"
          case "AU":
              return "Austrália"
          case "AR":
              return "Argentina"
          case "SE":
              return "Suécia"
          case "DK":
              return "Dinamarca"
          case "PL":
              return "Polônia"
          case "NL":
              return "Holanda"
          case "BE":
              return "Bélgica"
          case "NO":
              return "Noruega"
          case "IE":
              return "Irlanda"
          case "MX":
              return "México"
          case "PH":
              return "Filipinas"
          case "ID":
              return "Indonésia"
          case "TH":
              return "Tailândia"
          case "NG":
              return "Nigéria"
          case "ZA":
              return "África do Sul"
          case "EG":
              return "Egito"
          case _:
              return "País desconhecido ou não listado"
    
    return tratar_paises(pais_origem)

#FUNCAO PRINCIPAL QUE PUXA A LISTA DE FILMES DA API
def puxar_dados_filmes(pagina):
  url = "https://api.themoviedb.org/3/discover/movie"

  headers = {
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGZjMDNhNWY5ZmVjNTUzZTk0ZWE3NTQ1OTE1ZmFiMSIsIm5iZiI6MTc5NDA5MTczMi4zNzYsInN1YiI6IjZhZWZhYWQ0YjQ3YmY1MjA4MzBkMzU0ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KrfUs1hdrfWYV3HDO9gDFdmdy0AQ3-Z34t-fTGKlabA",
      "accept": "application/json",
  }

  params = {
      "include_adult": "false",
      "include_video": "false",
      "language": "en-US",
      "page": pagina,
      "sort_by": "popularity.desc",
  }

  response = requests.get(url, headers=headers, params=params)

  if response.status_code == 200:
    dados = response.json()
    filmes = dados.get("results", [])

    for filme in filmes:
            
            id_f = filme.get("id")

            if obter_orcamento(id_f) != "US$ 0" and obter_bilheteria(id_f) != "US$ 0":
              lista_para_tabela.append({
                  "Título": filme.get("title"),
                  "Data de Lançamento": filme.get("release_date"),
                  "Popularidade": filme.get("popularity"),
                  "Média de Votos": filme.get("vote_average"),
                  "Orçamento": obter_orcamento(id_f),
                  "Bilheteria": obter_bilheteria(id_f),
                  "País de Origem": obter_pais_origem(id_f),
                  "ID": id_f,
              })
  else:
    print(f"Erro ao obter dados na página {pagina}")


for pagina in range(1, 3):
  puxar_dados_filmes(pagina)
  print(f"Página {pagina} carregada.")

df = pd.DataFrame(lista_para_tabela)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_rows", None)



print("\n--- TABELA FINAL ---")
print(df)

