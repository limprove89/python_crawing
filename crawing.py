from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd

target_url = 'http://browse.gmarket.co.kr/list?category=200002525&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    results =[title, price, seller]
    
table = pd.DataFrame(result,columns=('title','price','seller'))
table.to_csv(path,encoding="cp949", mode="w", index=true)
makeexel(soup.select, 191209.csv)
# articles = pd.DataFrame(results, columns=['상품명','가격','판매자'])
# articles.to_csv('191209.csv')