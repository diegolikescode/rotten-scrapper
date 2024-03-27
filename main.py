from bs4 import BeautifulSoup, Tag
import requests
from scrapy.spiders import Spider
from scrapy.selector import 


class Crawling(Spider):
    name = 'rotten_tomatoes'
    allowed_domains = ['https://www.rottentomatoes.com']
    start_urls = ['https://www.rottentomatoes.com/m/oppenheimer_2023']

    def parse(self, response):
        hxs = Html

def main():
    print('init main')

    req = requests.get(url='https://www.rottentomatoes.com/m/oppenheimer_2023')
    
    if req.status_code != 200:
        print('fuck!')
        return

    soup = BeautifulSoup(req.text, 'html.parser')
    scoreboard: Tag = soup.find_all('score-board-deprecated')[0]
    audience_score, tomatometerscore = \
        scoreboard.get_attribute_list('audiencescore')[0], \
        scoreboard.get_attribute_list('tomatometerscore')[0]

    print(audience_score, tomatometerscore)
    req.close()


main()
