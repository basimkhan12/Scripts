from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pandas


urls = []
product = []

html = urlopen('https://cacticus.ca/product-category/shop/')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', attrs={'class':'attachment-shop_catalog size-shop_catalog wp-post-image'})
for image in images:
    urls.append(image['src']+'\n')
names = bs.find_all('h2', attrs={'class':'woocommerce-loop-product__title'})
for prod in names:
    product.append(prod.text)


#print(len(urls))
#print(len(product))





#print(urls)
#print(product)
df = pandas.DataFrame({'images': urls,
                      'name': product})
df.to_csv('C:/Users/bjk_m/PycharmProjects/scraperimg/body.csv')


