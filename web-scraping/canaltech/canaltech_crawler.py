import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import json
import utils

def crawl_canaltech(from_dt):

# Coleta os artigos do site canal_tech
# Cada artigo é retornado em um dicionário e todos eles são adicionados à uma lista, o retorno da função é a lista completa com os artigos

    url = 'https://canaltech.com.br'
    main_category = '/ultimas/'
    page = requests.get(url + main_category)
    page_content = BeautifulSoup(page.content, 'html.parser')
    crawled_data = []
    article_content_text = ''

    articles = page_content.find_all(class_='col-xs-12 col-sm-6 col-md-4')

    for article in articles:
        try:

            #Coloquei todo mundo dentro do try, porque se ter algum problema eu prefiro não ingerir um dado errado do que ingerir e ter várias sujeiras


                #Coleta a hora de publicação do artigo
                article_str_time = article.find('span', class_='time')['title']
                article_date = re.sub(" +", " ", article_str_time.split('às')[0].replace('de', '').strip())
                article_hour = article_str_time.split('às')[1].strip().replace('h', ':')
                article_full_dt = utils.to_datetime(article_date, article_hour)


                #Coleta os dados se a hora de publicação for maior que a data enviada no parâmetro da função
                if article_full_dt > from_dt:

                    article_url = url + article.find('a', class_='jc', href = True)['href']   
                    article_title = article.find('h3', class_='title titulo-listagem').text
                    article_category = article.find('span', class_='catag').text

                    #Pega o conteúdo do artigo e o autor
                    article_request = requests.get(article_url)
                    article_content = BeautifulSoup(article_request.content, 'html.parser')
                    article_author = json.loads(article_content.find(class_='post-container article-active')['data-layer'])['autor']

                    #Como a implementação inicial é em csv, deixei comentado a parte de pegar o conteúdo
                    #Fica ruim carregar esse tipo de conteúdo no csv.

                    #for text in article_content.find(class_ = 'content').find_all('p'):
                        #article_content_text += str(text).replace('<p>', '').replace('</p>', '')

                    #Cria o retorno da função
                    article_data = {
                        'article_url' : str(article_url),
                        'article_title' : str(article_title),
                        'article_category' : str(article_category),
                        'article_date' : str(utils.to_datetime(article_date, article_hour)),
                        'article_author' : str(article_author)
                    }

                    crawled_data.append(article_data)

        except:
            pass

    return crawled_data
