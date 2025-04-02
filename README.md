# Web Scraping, Hadoop e Apache Spark do Site de dados abertos da Série Histórica de Preços de Combustíveis e de GLP

## Disciplina:
Big Data

## Exercício: 
Web Scraping, Hadoop e Apache Spark do Site de dados abertos da Série Histórica de Preços de Combustíveis e de GLP

## O que faz?
Script Python que acessa o portal de dados abertos da Série Histórica de Preços de Combustíveis e de GLP (https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp/) e extrai os arquivos dos dados de preços de combustíveis de 2020 a 2025 (através de web scrapping), que serão processados posteriormente pelo Haddop e pelo Apache Spark.

## Configuração
Antes de executar, você deve configurar no arquivo **main.py**, da pasta **parte_1_web_scraping**, e no arquivo **dataframe_api.ipynb**, da pasta **parte_3_spark**, o diretório de download dos arquivos extraídos.

Para isso, defina o caminho da pasta nas seguintes variáveis

**main.py**
```bash
download_dir = "seu/diretorio/para/receber/o/download/dos/arquivos/extraidos"
```
**dataframe_api.ipynb**
```bash
data_path = "seu/diretorio/para/receber/o/download/dos/arquivos/extraidos"
```
