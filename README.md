# Análise de Dados: Top 250 Filmes do IMDb com OMDB API

### ✨ Visão Geral do Projeto

Este projeto tem como principal objetivo **demonstrar** a manipulação, limpeza, análise e enriquecimento de dados. Utiliza um *pipeline* que cruza dados de um arquivo CSV (Top 250 Filmes do IMDb) com informações adicionais obtidas de uma **API aberta** (`OMDB API`).

A estrutura do projeto segue as melhores práticas de desenvolvimento garantindo que o código seja **modularizado** e reprodutível.

---

### 🎯 Conceito e Objetivos

O conceito central é analisar e limpar os dados brutos através de um processo de **Extração, Transformação e Carga (ETL)** simplificado.

#### Principais Objetivos:

1.  **Enriquecimento de Dados:** Realizar o *merge* de dados adicionais da `OMDB API` usando o título dos filmes. O foco analítico principal foi a extração e utilização da métrica **Box Office** (bilheteria) para gerar *insights* estatísticos sobre o desempenho comercial dos filmes.
2.  **Manipulação Profissional:** Utilizar a biblioteca **Pandas** para realizar limpeza, padronização e fusão (*merge*) de DataFrames de maneira eficiente.
3.  **Visualização de Dados:** Gerar gráficos estatísticos relevantes (usando **Matplotlib** e **Seaborn**) para identificar tendências e padrões no *dataset* de filmes.

---

### 🛠️ Tecnologias e Bibliotecas Utilizadas

| Categoria | Tecnologia/Biblioteca | Finalidade no Projeto |
| :--- | :--- | :--- |
| **Linguagem** | Python | Linguagem principal para o desenvolvimento. |
| **Manipulação de Dados** | **Pandas** | Leitura, limpeza, transformação e *merge* dos dados. |
| **Requisições Web** | **Requests** | Comunicação HTTP para extrair dados da `OMDB API`. |
| **Visualização** | **Seaborn** e **Matplotlib** | Criação do gráficos de *histograma*. |
| **Estrutura** | **Venv** | Gerenciamento isolado das dependências do projeto. |

---

### 🏗️ Preparação de Ambiente e Estrutura

Para garantir a reprodutibilidade e a integridade do projeto, duas práticas essenciais foram adotadas: o **Ambiente Virtual** e a **Modularização do Código**.

#### 📦 Ambiente Virtual (`venv`)
O projeto utiliza um **ambiente virtual (`venv`)** para isolar suas dependências. **A importância desta prática reside em:**

* **Isolamento:** Garante que todas as bibliotecas e suas versões sejam instaladas *apenas* para este projeto, evitando conflitos com outras instalações de Python na máquina do usuário.
* **Reprodutibilidade:** Permite que qualquer outro desenvolvedor ou recrutador reproduza o ambiente de trabalho exato, utilizando apenas o arquivo `requirements.txt`.
* **Profissionalismo:** Demonstra o compromisso com as boas práticas de desenvolvimento e a criação de projetos portáteis e estáveis.

#### 🧑‍💻 Modularização do Código
O código foi estruturado em módulos para separar as responsabilidades:

* `main.py`: Script principal que orquestra o *pipeline* de ETL e análise (lógica de alto nível).
* `functions.py`: Módulo que armazena todas as funções reutilizáveis, como a chamada à API e as rotinas de limpeza (lógica de baixo nível).

**Estrutura do Repositório:**

nome-do-seu-projeto/ ├── .venv/ # Ambiente virtual isolado ├── data/ │ └── imdb_top_250_movies.csv # Arquivo de dados de entrada ├── src/ │ ├── main.py # Orquestrador do ETL. │ └── functions.py # Módulo de funções. ├── requirements.txt # Dependências do projeto. └── README.md # Documentação principal.


---

### 📚 Fontes de Dados e API

| Fonte | Tipo | Link | Observações |
| :--- | :--- | :--- | :--- |
| **Dados Base** | Arquivo CSV | [IMDb Top 250 Movies Dataset (Kaggle)](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset) | Fonte inicial de títulos e dados básicos. |
| **Enriquecimento** | API Aberta | [OMDB API - The Open Movie Database](https://www.omdbapi.com/) | Utilizada para obter dados como *Metascore* e *Box Office*. A **chave de acesso é gratuita** e pode ser obtida rapidamente no site. |

---

### 📺 Detalhamento em Vídeo

> **Link do Vídeo no YouTube:** https://www.youtube.com/watch?v=9pjgGE1Rsp4

*Aviso: O vídeo é um pouco mais longo, pois o objetivo é fornecer um **detalhamento completo** do código linha por linha e de todos os conceitos envolvidos, ideal para quem busca entender a aplicação prática das bibliotecas.*

---
