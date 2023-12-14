import requests
from bs4 import BeautifulSoup
import pandas as pd

nombre = list()
apellido = list()
especialidad = list()

url = 'http://127.0.0.1:8000/'
html_doc = requests.get(url)

soup = BeautifulSoup(html_doc.text, 'html.parser')
# data=soup.find_all('td', attrs= {"class": "table-group-divider"})
# i=0
# #print(data)
# while(i+2<len(data)):
#     nombre.append(data[i].text)
#     apellido.append(data[i+1].text)
#     especialidad.append(data[i+2].text)
#     i+=3
#
#
#
# df = pd.DataFrame({'Nombre': nombre, 'Apellido': apellido, 'Especialidad': especialidad})
# df.to_csv(path_or_buf='enfermero.csv',index=False, encoding='utf-8')

tabla = soup.find('table')
filas = tabla.find_all('tr')

for fila in filas:
    celdas = fila.find_all('td')
    # print (celdas)

    if len(celdas) > 0:
        nombre.append(celdas[0].string)
        apellido.append(celdas[1].string)
        especialidad.append(celdas[2].string)

# print(ancor)
# print(soup.prettify())
print(nombre)
print(apellido)
print(especialidad)

df = pd.DataFrame({'Nombre': nombre, 'Apellido': apellido, 'Especialidad': especialidad})
df.to_csv(path_or_buf='enfermero.csv', index=False, encoding='utf-8')
