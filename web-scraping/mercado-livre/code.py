#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 21:55:26 2020

@author: edshow
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date

url  = 'https://eletronicos.mercadolivre.com.br/tv/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

item_name = [i.text for i in soup.find_all('span', class_='main-title')]
item_advisor = [i.text for i in soup.find_all('span', class_='item__brand-title-tos')]
item_price = [i.text for i in soup.find_all('span', class_='price__fraction')]
item_link = [i['href'] for i in soup.find_all('a', class_='item__info-link item__js-link', href=True)]

df = pd.DataFrame([item_name, item_advisor, item_price, item_link]).transpose().fillna('na').reset_index().drop('index', axis =1)
df.rename(columns={0:'item_name', 1:'item_advisor', 2:'item_price', 3:'item_link'}, inplace = True)


df = df[(df['item_advisor'] != 'na') & (df['item_price'] != 'na')]
df['item_advisor'] = df['item_advisor'].map(lambda x: x.lstrip('por ').upper())
df['item_price'] = pd.to_numeric(df['item_price'])
df['info-update-date'] = date.today().strftime("%Y-%m-%d")


for index, item in df.iterrows():
    
    item_name = item[0]
    item_advisor = item[1]
    item_price = item[2]
    item_link = item[3]
    
    item_page = BeautifulSoup(requests.get(item_link).content, 'html.parser')
    
    item_details_headers = [i.text for i in item_page.find_all('span', class_='ui-pdp-list__item__label')]
    item_details = [i.text for i in item_page.find_all('p', class_='ui-pdp-list__item__text')]
    details_dict = {item_details_headers[i] : item_details[i] for i in range(len(item_details))}
    
    
    df.loc[index,'stock'] = item_page.find('h3', class_='ui-pdp-color--BLACK ui-pdp-size--MEDIUM ui-pdp-family--REGULAR ui-pdp-stock-information__title').text
    df.loc[index, 'brand'] = item_page.find('span', class_='andes-table__column--value').text
    df.loc[index, 'screen-type'] = details_dict['Tipo de tela']
    df.loc[index, 'screen-size'] = details_dict['Tamanho da tela']
    df.loc[index, 'screen-resoluction-type'] = details_dict['Tipo de resolução']
    df.loc[index, 'rate-score'] = item_page.find('h2', class_='ui-pdp-reviews__rating__summary__average').text
    
    try:
        df.loc[index, 'smart'] = details_dict['É smart']
    
    except:
        df.loc[index, 'smart'] = float('NaN')
    
    
    
    
    
    


        
