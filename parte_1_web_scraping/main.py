import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import zipfile

download_dir = ""

# Configurações para Firefox
options = Options()
options.set_preference("browser.download.folderList", 2)  # Pasta definida pelo usuário
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_dir)  # Diretório de destino

# MIME para CSV e ZIP
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv,application/zip")

url = "https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp"
driver = webdriver.Firefox(options=options)
driver.get(url)
driver.implicitly_wait(10) # Seconds

# Tenta encontrar o botão 'Recursos' para clicá-lo
buttonsCollapsable = driver.find_elements(By.ID, "btnCollapse")
button_text = "Recursos"

for index, btn in enumerate(buttonsCollapsable):
    if button_text in btn.text:
        index_btn_recursos = index

try:
    button_recursos = buttonsCollapsable[index_btn_recursos]
    button_recursos.click()
    print('Botão <Recursos> clicado com sucesso!')
except Exception as e:
    print(f'Erro ao tentar clicar no botão <Recursos>: {e}')

#Busca o conteúdo dos recursos
posts = driver.find_element(By.ID, "collapse-recursos")
posts_html = posts.get_attribute('innerHTML')

soup = BeautifulSoup(posts_html, 'html.parser')
posts_title = soup.find_all("h4")
button = soup.find_all(id="btnDownloadUrl")

# Filtragem dos dados com base nos posts
texto_filtro = "Combustíveis Automotivos"
anos_filtro = ["2020", "2021", "2022", "2023", "2024", "2025"]

resultados_filtrados = []
for index, post in enumerate(posts_title):
    if texto_filtro in post.text and any(ano in post.text for ano in anos_filtro): # Verifica se a substring está no texto do elemento
        resultados_filtrados.append((index, post.text))  # Adiciona índice e texto aos resultados

buttonsDownloadArr = driver.find_elements(By.ID, "btnDownloadUrl")

print(len(resultados_filtrados))

# Clica nos botões para download
for posicao, texto in resultados_filtrados:
    buttonsDownloadArr[int(posicao)].click()
    time.sleep(0.5)
    
def downloads_concluidos(diretorio):
    """Verifica se há arquivos incompletos no diretório."""
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith(".part"):  # Arquivos temporários do Firefox
            return False
    return True

# Aguardando até que todos os downloads sejam concluídos
while not downloads_concluidos(download_dir):
    print("Aguardando conclusão dos downloads...")
    time.sleep(3)  # Aguarda 3 segundos antes de verificar novamente

print("Todos os downloads foram concluídos!")
print('Success in Web Scrapping!')

driver.quit()

# Busca os arquivos zip para extrair seu conteúdo
for arquivo in os.listdir(download_dir):
    if arquivo.endswith(".zip"):  # Verifica se o arquivo é um .zip
        caminho_arquivo = os.path.join(download_dir, arquivo)
        
        # Extrair o conteúdo do arquivo .zip
        with zipfile.ZipFile(caminho_arquivo, 'r') as zip_ref:
            zip_ref.extractall(download_dir)  # Extrai para o mesmo diretório
            print(f"Arquivo extraído: {arquivo}")
        
        # Excluir o arquivo .zip após a extração
        os.remove(caminho_arquivo)
        print(f"Arquivo excluído: {arquivo}")
