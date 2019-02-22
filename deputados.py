# Link da pesquisa: https://www2.camara.leg.br/deputados/pesquisa

# ul class="demaisInformacoes visualNoMarker"

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

address_page = 'https://www2.camara.leg.br/deputados/pesquisa/layouts_deputados_resultado_pesquisa?nome=&Partido=QQ&UF=QQ&SX=QQ&Legislatura=56&condic=T&ordem=siglaUF&forma=lista&Pesquisa=Buscar'

page = urlopen(address_page)
soup = BeautifulSoup(page, 'html.parser')
ul = soup.find('ul', attrs={'class': 'demaisInformacoes'})
data = []
for infos in ul.find_all('li'):
    for name, info in zip(infos.find_all('strong'), infos.find_all('ul')):
        data.append((name.get_text(), info.li.get_text()))

with open('deputados.csv', 'a', encoding='cp1252', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for name, infos in data:
        writer.writerow([name, infos])
    