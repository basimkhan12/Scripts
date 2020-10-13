from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas


urls = []
product = []

html = urlopen('https://foralwaysflowercompany.ca/collections/frontpage/products/16-large-roses')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('fieldset', attrs={'class':'single-option-radio'})
for image in images:
    urls.append(image.text + ',')
names = bs.find_all('p', attrs={'class':'product-caption'})
for prod in names:
    product.append(prod.text)

#urls.append(11)








print(len(urls))
print(len(product))





for i in urls:
    print(i)
for i in product:
    print(i)
df = pandas.DataFrame({'images': urls,
                      'name': product})
df.to_csv('C:/Users/bjk_m/PycharmProjects/scraperimg/bodyyyy.csv')


