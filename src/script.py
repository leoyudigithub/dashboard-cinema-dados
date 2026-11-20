#IMPORTS
import numpy as np
import pandas as pd
import requests


#REQUSIÇÃO DA LISTA DE FILMES DA API
def obter_lista_filmes(pagina):
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
    return filmes  
  else:
        print(f"Erro ao obter dados na página {pagina}")  

#OBTER ORÇAMENTO
def obter_orcamento(detalhes):
    
    orcamento = detalhes.get("budget", 0)
    if orcamento > 0:
      return f"US$ {orcamento:,}"
    else:
      return "US$ 0"

#OBTER BILHETERIA
def obter_bilheteria(detalhes):

    bilheteria = detalhes.get("revenue", 0)
    if bilheteria > 0:
      return f"US$ {bilheteria:,}"
    else:
      return "US$ 0"

#OBTER PAÍS DE ORIGEM DO FILME
def obter_pais_origem(detalhes):

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

#LISTA PARA CARREGAR VARIAS PAGINAS
lista_para_tabela = []

#CARREGAR VARIAS PAGINAS DE FILMES
for pagina in range(1, 3):

  for filme in obter_lista_filmes(pagina):
    id_filme = filme.get("id")
    
    url = f"https://api.themoviedb.org/3/movie/{id_filme}"
      
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGZjMDNhNWY5ZmVjNTUzZTk0ZWE3NTQ1OTE1ZmFiMSIsIm5iZiI6MTc5NDA5MTczMi4zNzYsInN1YiI6IjZhZWZhYWQ0YjQ3YmY1MjA4MzBkMzU0ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KrfUs1hdrfWYV3HDO9gDFdmdy0AQ3-Z34t-fTGKlabA",
        "accept": "application/json",
    }
      
    response = requests.get(url, headers=headers, params={"language": "en-US"})
    
    if response.status_code == 200:
     detalhes = response.json()
    
     if obter_orcamento(detalhes) != "US$ 0" and obter_bilheteria(detalhes) != "US$ 0":
      lista_para_tabela.append({
            "Título": filme.get("title"),
            "Data de Lançamento": filme.get("release_date"),
            "Popularidade": filme.get("popularity"),
            "Média de Votos": filme.get("vote_average"),
            "Orçamento": obter_orcamento(detalhes),
            "Bilheteria": obter_bilheteria(detalhes),
            "País de Origem": obter_pais_origem(detalhes),
            "ID": id_filme,
        })
    else:
        print(f"Erro ao obter dados de filme com ID: {id_filme}")

  print(f"Página {pagina} carregada.")

#CONVERTER LISTA PARA DATAFRAME
df = pd.DataFrame(lista_para_tabela)

#Configurações para exibições teste
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_rows", None)

#Exibição teste de dados carregados
print("\n--- TABELA FINAL ---")
print(df)
