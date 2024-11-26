
# Análise de Saúde Mental

Este repositório contém dados e análises relacionadas à pesquisa sobre saúde mental, inspiradas nos achados da Dra. **Saloni Dattani**, uma renomada pesquisadora na área de saúde mental e epidemiologia. A análise visa explorar as principais tendências, desafios e soluções relacionados à saúde mental na sociedade moderna, utilizando estudos científicos e insights baseados em dados.

## Visão Geral

A saúde mental é um dos maiores desafios globais de saúde atualmente. Este projeto aborda:

- Estatísticas globais sobre saúde mental
- Principais fatores que contribuem para os transtornos mentais (como fatores socioeconômicos, ambientais e genéticos)
- Tendências de longo prazo nos resultados de saúde mental
- Abordagens para melhorar o bem-estar mental

## Principais Descobertas

A análise se inspira amplamente no trabalho da Dra. **Saloni Dattani**, que destaca:

- A prevalência de transtornos mentais em diferentes grupos demográficos
- Como os serviços de saúde mental podem ser aprimorados por meio de políticas públicas baseadas em evidências
- O impacto do estigma, da conscientização e da acessibilidade no cuidado com a saúde mental

## Fontes de Dados

Os dados utilizados neste projeto foram obtidos de conjuntos de dados públicos sobre saúde global, incluindo:

- **Organização Mundial da Saúde (OMS)**
- **Our World in Data**
- **Instituto Nacional de Saúde Mental (NIMH)**

O repositório inclui os conjuntos de dados já limpos, scripts de análise e visualizações.

Este projeto contém scripts Python desenvolvidos para a análise de dados relacionados à saúde mental, utilizando as bases de dados localizadas na pasta `/database`.

## Estrutura de dados e scripts Projeto

- **Base de Dados**: Todos os arquivos CSV e demais fontes de dados estão armazenados na pasta `/database`.
- **Scripts**: Os scripts Python para análise estão na pasta `/scripts`.

## Como Executar os Scripts

Os scripts estão padronizados para ler os arquivos CSV da pasta `/database`, utilizando o caminho:

```python
file_path = 'projetoaplicadomackenzie\\database\\nome_do_arquivo.csv'
```

# Bibliotecas Utilizadas
Os scripts dependem das seguintes bibliotecas para executar a análise:

* Pandas: Utilizado para manipulação e análise dos dados em formato de DataFrames.
* Seaborn: Utilizado para visualizações estatísticas.
* Matplotlib: Utilizado para criar gráficos e visualizações adicionais.


# Instalação de Dependências
Para instalar todas as bibliotecas necessárias, execute o seguinte comando após ativar o seu ambiente virtual:

```pip install -r requirements.txt```

Esse comando instalará todas as dependências listadas no arquivo requirements.txt, que contém as bibliotecas auxiliares utilizadas no projeto.

# Rodando os Scripts
Com as dependências instaladas e o ambiente virtual ativado, execute os scripts diretamente no terminal:

```python scripts/nome_do_script.py```

Certifique-se de que o caminho dos arquivos CSV está correto no script que você deseja executar, e que o arquivo de dados correspondente está na pasta /database.


## Contribuições
Membros do grupo:

* Wesley Rodrigo dos Santos
* Flávio Estavam Nogueira Andrade
* Miguel Shiraishi de Almeida

[Link da apresentação no YouTube](https://youtu.be/KeitcekOTbQ)

[Material de Apoio PPT](https://docs.google.com/presentation/d/1TIS5EkjWHcKXGIUx0FVbXkBAq82dfXTSyH-RPSYvVjY/edit#slide=id.p)

## Referências

- Dattani, S., & **Our World in Data** - _Análise de Saúde Mental_
- [Estudo Original](https://ourworldindata.org/mental-health)

