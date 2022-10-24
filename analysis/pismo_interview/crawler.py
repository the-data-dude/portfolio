import requests
import json
import time
from dbconnect import db_session, Quote

class Crawler:

    def __init__(self, api_id):
        self.api_id = api_id
        self.results = []
    
    def __headers(self):
        headers= {"apikey": self.api_id}
        return headers

    def __payload(self):
        payload = {}
        return payload

    def crawl_data(self, start_date, end_date, quotes_filter):
        url = f"https://api.apilayer.com/currency_data/timeframe?start_date={start_date}&end_date={end_date}"
        response = requests.request("GET", url, headers=self.__headers(), data = self.__payload())
        status_code = response.status_code
        result = json.loads(response.text)

        if result['success'] == True:

            for date,quotes in result['quotes'].items():
                for quote,value in quotes.items():
                    if quote in quotes_filter:
                        self.results.append(Quote(id = str(date)+"-"+str(quote), date = date, currency = quote, value = value))

    def save(self):

        session = db_session()

        for quote in self.results:
            session.merge(quote)
    
        try:
            session.commit()
            session.close()
            return True
        except:
            session.rollback()
            return False

    def run(self, start_date, end_date, quotes_filter):
        self.crawl_data(start_date, end_date, quotes_filter)
        self.save()

if __name__ == '__main__':

    wanted = ['USDBRL', 'USDEUR', 'USDCLP']

    crawler = Crawler(api_id = 'N619oeRadapSrCG4Ighsn3w0WbZ4NlQJ')
    crawler.run(start_date = '2022-01-01', end_date = '2022-08-31', quotes_filter=wanted)
    time.sleep(5)
    crawler.run(start_date = '2021-01-01', end_date = '2021-12-31', quotes_filter=wanted)
    time.sleep(5)
    crawler.run(start_date = '2020-01-01', end_date = '2020-12-31', quotes_filter=wanted)
    time.sleep(5)
    crawler.run(start_date = '2019-01-01', end_date = '2019-12-31', quotes_filter=wanted)
