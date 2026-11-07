# Popularidade de Filmes em Contraste à Sua Qualidade

## 🎬 Sobre o Projeto
Este projeto consiste no desenvolvimento de um **Dashboard de Análise de Dados** focado em explorar a relação entre o sucesso comercial/popularidade de produções cinematográficas e a sua real qualidade técnica e artística percebida pelo público. 

### Justificativa da Escolha
No ecossistema do cinema atual, é comum observarmos blockbusters com enorme apelo mercadológico e bilheterias estrondosas, mas que dividem opiniões quanto à sua qualidade narrativa. Em contrapartida, obras aclamadas pela crítica ou pelo público nichado passam frequentemente despercebidas pelo grande público. A equipe escolheu este tema para investigar empiricamente essa dicotomia, utilizando métricas de dados para entender se o "hype" realmente reflete o valor percebido das produções ou se vivemos em uma era dominada puramente pelo marketing de massa.

---

## 📊 Fonte de Dados e Informações Utilizadas
Os dados que alimentam este dashboard foram extraídos da **TMDB (The Movie Database API)**. 

O conjunto de dados abrange variáveis essenciais para a análise comparativa:
* **Popularidade:** Métrica interna da plataforma baseada em visualizações diárias, votos, popularidade de atores, data de lançamento, entre outros fatores.
* **Média de Votos (`vote_average`):** A nota média atribuída pelos usuários da plataforma aos filmes.
* **Quantidade de Votos (`vote_count`):** O volume total de avaliações recebidas, servindo como termômetro para engajamento e alcance.
* **Gênero (`genres`):** Categoria temática dos filmes (ex: Ação, Drama, Comédia, Sci-Fi).
* **Ano de Lançamento (`release_date`):** A temporalidade da obra, permitindo análises históricas e de longevidade.

---

## ❓ Perguntas-Chave (Business Questions)
O dashboard foi estruturado para responder a questionamentos cruciais sobre o comportamento do público e da indústria cinematográfica:

### Questão Central
* **Filmes mais populares são necessariamente mais bem avaliados pelo público?** 
  *(Investigação da correlação direta entre o índice de popularidade e a nota média).*

### Questões Secundárias
* **Filmes com muitos votos têm avaliações médias diferentes dos filmes com poucos votos?** 
  *(Análise de viés de sobrevivência, efeito manada ou amostragem).*
* **Quais gêneros apresentam maior discrepância entre popularidade e nota?** 
  *(Identificação de quais categorias cinematográficas geram mais polarização).*
* **Filmes antigos continuam recebendo atenção?** 
  *(Análise do engajamento e do fluxo de votos em obras clássicas ou de décadas anteriores em comparação aos lançamentos recentes).*

---

## 🚀 Como Executar o Projeto
*(Instruções para clonar o repositório, instalar dependências e rodar o dashboard — adapte conforme a stack utilizada, ex: Python/Streamlit, Power BI, Tableau, etc.)*

```bash
# Clone este repositório
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)

# Entre no diretório
cd nome-do-repositorio

# Instale as dependências (exemplo para Python)
pip install -r requirements.txt

# Execute o dashboard
streamlit run app.py
