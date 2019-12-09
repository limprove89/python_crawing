from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
import re

f = open('191209_all.csv', 'w')
f.write('상품명, 가격, 판매처, 링크\n')

target_url = 'http://browse.gmarket.co.kr/list?category=200002525&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text.replace(',','')
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    goodscodes = item.select_one('a[href*=goodscode]')
    goodscode = re.findall(r'\d{5,}', goodscodes['href'])[0]
    url = 'http://item.gmarket.co.kr/Item?goodscode=' + goodscode      
    
    f.write(title + ',' + price + ',' + seller + ',' + url + '\n')

f.close()

f = open('191209_orange.csv', 'w')
f.write('상품명, 가격, 판매처, 링크\n')

target_url = 'http://browse.gmarket.co.kr/list?category=300012572&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text.replace(',','')
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    goodscodes = item.select_one('a[href*=goodscode]')
    goodscode = re.findall(r'\d{5,}', goodscodes['href'])[0]
    url = 'http://item.gmarket.co.kr/Item?goodscode=' + goodscode      
    
    f.write(title + ',' + price + ',' + seller + ',' + url + '\n')

f.close()

f = open('191209_mong.csv', 'w')
f.write('상품명, 가격, 판매처, 링크\n')

target_url = 'http://browse.gmarket.co.kr/list?category=300012481&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text.replace(',','')
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    goodscodes = item.select_one('a[href*=goodscode]')
    goodscode = re.findall(r'\d{5,}', goodscodes['href'])[0]
    url = 'http://item.gmarket.co.kr/Item?goodscode=' + goodscode      
    
    f.write(title + ',' + price + ',' + seller + ',' + url + '\n')

f.close()

f = open('191209_avo.csv', 'w')
f.write('상품명, 가격, 판매처, 링크\n')

target_url = 'http://browse.gmarket.co.kr/list?category=300018841&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text.replace(',','')
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    goodscodes = item.select_one('a[href*=goodscode]')
    goodscode = re.findall(r'\d{5,}', goodscodes['href'])[0]
    url = 'http://item.gmarket.co.kr/Item?goodscode=' + goodscode      
    
    f.write(title + ',' + price + ',' + seller + ',' + url + '\n')

f.close()

f = open('191209_lemon.csv', 'w')
f.write('상품명, 가격, 판매처, 링크\n')

target_url = 'http://browse.gmarket.co.kr/list?category=300028000&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text.replace(',','')
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    goodscodes = item.select_one('a[href*=goodscode]')
    goodscode = re.findall(r'\d{5,}', goodscodes['href'])[0]
    url = 'http://item.gmarket.co.kr/Item?goodscode=' + goodscode      
    
    f.write(title + ',' + price + ',' + seller + ',' + url + '\n')

f.close()

f = open('191209_red.csv', 'w')
f.write('상품명, 가격, 판매처, 링크\n')

target_url = 'http://browse.gmarket.co.kr/list?category=300012483&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text.replace(',','')
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    goodscodes = item.select_one('a[href*=goodscode]')
    goodscode = re.findall(r'\d{5,}', goodscodes['href'])[0]
    url = 'http://item.gmarket.co.kr/Item?goodscode=' + goodscode      
    
    f.write(title + ',' + price + ',' + seller + ',' + url + '\n')

f.close()

f = open('191209_grape.csv', 'w')
f.write('상품명, 가격, 판매처, 링크\n')

target_url = 'http://browse.gmarket.co.kr/list?category=300025761&s=8'
html = urllib.request.urlopen(target_url).read()
soup = BeautifulSoup(html, 'html.parser')

for item in soup.select('body .box__item-container .box__information'):
    title = item.select_one('.text__item').text.strip()
    price = item.select_one('strong.text__value').text.replace(',','')
    try:
        seller = item.select_one('.text__seller').text
    except:
        seller = "종합몰"
    goodscodes = item.select_one('a[href*=goodscode]')
    goodscode = re.findall(r'\d{5,}', goodscodes['href'])[0]
    url = 'http://item.gmarket.co.kr/Item?goodscode=' + goodscode      
    
    f.write(title + ',' + price + ',' + seller + ',' + url + '\n')

f.close()
