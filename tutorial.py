import locale
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
driver = webdriver.Firefox()

products = []
prices = []
ratings = []

driver.get(
    'https://www.flipkart.com/laptops/%3C/a%3E~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp'
    ';amp;amp;amp;uniq')

contenido = driver.page_source
soup = BeautifulSoup(contenido, 'html.parser')

productos = soup.find_all('div', attrs={"class": "_4rR01T"})
for producto in productos:
    products.append(producto.text)

precios = soup.find_all('div', attrs={"class": "_30jeq3 _1_WHN1"})
for precio in precios:
    precio_sin_coma = precio.text.replace(",", "")
    precio_sin_simbolo = precio_sin_coma.replace("₹", "")
    precio_en_dolares = 0.012 * float(precio_sin_simbolo)
    precio_en_dolares = "$" + "{0:.2f}".format(precio_en_dolares)
    print(precio_en_dolares)
    prices.append(precio_en_dolares)

estrellas = soup.find_all('div', attrs={"class": "_3LWZlK"})
for i, estrella in enumerate(estrellas):
    if i < 24:
        ratings.append(estrella.text)
        print(estrella.text)
    else:
        break

print(len(products))
print(len(prices))
print(len(ratings))

df = pd.DataFrame({'Producto': products, 'Precio': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
