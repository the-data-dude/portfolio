import canaltech_crawler as crawler
from datetime import datetime
import pandas as pd
import json
import time

while True:

    #Carrega as noticias já existentes
    existing_news = pd.read_csv('canaltech_news.csv', sep = ';', header = 0)

    #Pega as novas noticias, com base na data mais recente das noticias já existentes no csv
    recent_news = crawler.crawl_canaltech(from_dt = datetime.strptime(existing_news['article_date'].max(), '%Y-%m-%d %H:%M:%S'))
    recent_news_df = pd.DataFrame(recent_news)

    #Incrementa as novas informações no csv
    if not recent_news_df.empty:
        new_rows = recent_news_df.shape[0]
        recent_news_df.to_csv('canaltech_news.csv', mode = 'a', sep = ';', index = False, header = False)
        print('{} - Adicionados {} novo(s) registro(s) no csv'.format(datetime.now(), new_rows))
        
    #Espera 5 minutos antes de repetir o processo
    time.sleep(60 * 5)
