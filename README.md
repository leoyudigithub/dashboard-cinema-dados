# Economia e Recepção da Indústria Cinematográfica: Lucro, Avaliações e o Cinema Brasileiro no Cenário Global

## 🎬 Sobre o Projeto
Este projeto consiste no desenvolvimento de uma pesquisa e **Dashboard de Análise de Dados** focado na dimensão econômica e na recepção da indústria cinematográfica global ao longo do tempo.

### Justificativa da Escolha
A indústria do cinema movimenta bilhões de dólares anualmente, operando em uma dinâmica complexa onde grandes orçamentos nem sempre garantem rentabilidade ou aclamação do público. Além disso, há uma forte assimetria no mercado global: enquanto Hollywood domina as bilheterias mundiais, indústrias regionais e emergentes, como o cinema brasileiro, enfrentam diversos desafios de distribuição e econômicos. A equipe escolheu este tema para investigar empiricamente como o investimento financeiro se traduz em retorno econômico e aprovação do público ao longo das décadas, além de traçar um raio-X comparativo do posicionamento do Brasil frente aos grandes polos cinematográficos internacionais.

---

## 📊 Fonte de Dados e Informações Utilizadas
Os dados que alimentam este projeto foram extraídos da **TMDB (The Movie Database API)**.

O conjunto de dados abrange variáveis financeiras, temporais, geográficas e de recepção:
* **Orçamento (`budget`):** Valor total investido na produção do filme (em USD).
* **Bilheteria (`revenue`):** Arrecadação global bruta obtida nas exibições (em USD).
* **Média de Votos (`vote_average`):** Nota média de avaliação atribuída pelos usuários da plataforma.
* **Quantidade de Votos (`vote_count`):** Volume total de avaliações recebidas, medindo o engajamento do público.
* **País de Origem (`production_countries`):** País ou países responsáveis pela produção da obra.
* **Ano de Lançamento (`release_date`):** Data de estreia, permitindo análises temporais por décadas.
* **Gênero (`genres`):** Categorização temática dos filmes.

---

## ❓ Perguntas-Chave (Business Questions)

### Questão Central
* **Como os valores de orçamento e bilheteria se convertem em lucro real ao longo do tempo, e de que forma o investimento financeiro se relaciona com a recepção do público nas diferentes regiões do mundo?**

### Questões Secundárias
* **Evolução do Lucro e ROI:** Como a rentabilidade dos filmes (lucro absoluto e retorno sobre o investimento - ROI) evoluiu ao longo das décadas?
* **Orçamento vs. Qualidade Percebida:** Filmes com orçamentos astronômicos garantem notas mais altas do público, ou existe um ponto de retorno decrescente?
* **Panorama Brasil vs. Mundo:** Como o mercado cinematográfico brasileiro se posiciona em termos de orçamento médio, bilheteria e avaliação do público em comparação com grandes indústrias (ex: Hollywood, cinema europeu)?
* **Desempenho Comercial vs. Crítica Popular:** A relação entre bilheteria e nota de usuários varia significativamente entre filmes nacionais e produções internacionais?

---

## 🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes ferramentas, linguagens e bibliotecas:

### 🔌 API
* **[TMDB API (The Movie Database)](https://www.themoviedb.org/documentation/api):** Fonte oficial de dados para extração de metadados, notas, popularidade e informações dos filmes.

### 🐍 Linguagem
* **Python** (Versão 3.x) — Linguagem principal utilizada para a extração, tratamento dos dados e construção do dashboard.

### 📚 Bibliotecas Python
* **[Pandas](https://pandas.pydata.org/):** Manipulação, limpeza e tratamento dos dados extraídos da API.
* **[Requests](https://docs.python-requests.org/):** Consumo e integração com os endpoints da API do TMDB.
* **[Streamlit](https://streamlit.io/):** Construção e hospedagem da interface interativa do dashboard.
* **[Matplotlib](https://matplotlib.org/):** Criação dos gráficos analíticos para visualização do contraste entre popularidade e qualidade.
* **[Numpy](https://numpy.org/):** Realização de operações matemáticas e métricas estatísticas dos dados análisados.


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
