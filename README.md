# Web Scraping, Hadoop e Apache Spark do Site de dados abertos da Série Histórica de Preços de Combustíveis e de GLP

## Disciplina:
Big Data

## Exercício: 
Web Scraping, Hadoop e Apache Spark do Site de dados abertos da Série Histórica de Preços de Combustíveis e de GLP

## O que faz?
Script Python que acessa o portal de dados abertos da Série Histórica de Preços de Combustíveis e de GLP (https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp/) e extrai os arquivos dos dados de preços de combustíveis de 2020 a 2025 (através de web scrapping), que serão processados posteriormente pelo Haddop e pelo Apache Spark.

## Configuração
Antes de executar, você deve configurar no arquivo **main.py**, da **parte_1_web_scraping**, o diretório de download dos arquivos extraídos.

Para isso, defina uma pasta na seguinte variável
```bash
download_dir = "seu/diretorio/para/receber/o/download/dos/arquivos/extraidos"
```
