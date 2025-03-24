from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import logging
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
import time

logger = logging.getLogger()

all_game = []

driver = webdriver.Edge()
    
def load_fetch_data(link):
    driver.get(link)
    for _ in range(110):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.0001)
    
    time.sleep(2)
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    return bs

def inner_link_extraction(link):
    pass

def outer_link_extraction(link):
    game_list = []
    bs = load_fetch_data(link)
    section = bs.find("div", attrs={'id': 'SaleSection_13268'}).find("div", attrs={'class': '_1cOoCFwafBlSkwllIMf3XM'})
    section_divs = section.find_all("div", attrs={'class': ['_2hhNOdcC6yLwL_rugP3YLf', '_37iggltdgh0RtNIECJCfOj']})
    for div in section_divs:
        ### Extract link
        info_div = div.find("div", attrs={'class': '_111nfdz8Xyg7lDjTWv_OmK'})
        game_link = [a['href'] for a in info_div.find_all('a', href=True)]
        
        ### Extract pictures
        pic_div = div.find("div", attrs={'class': '_2oW_y7Mm3ihf1XQ0C1VWhx'})
        game_pic = [img['src'] for img in pic_div.find_all('img')]
        
        ### Extract name
        game_name = div.find("div", attrs={'class': '_2ekpT6PjwtcFaT4jLQehUK'}).text
        
        ### Release date
        date_release = div.find("div", attrs={'class': '_1qvTFgmehUzbdYM9cw0eS7'}).text
        
        ### Sale percentage
        price = []
        if div.find("div", attrs={'class': 'cnkoFkzVCby40gJ0jGGS4'}) != None:
            sale_perc = div.find("div", attrs={'class': 'cnkoFkzVCby40gJ0jGGS4'}).text
            org_price = div.find("div", attrs={'class': '_3fFFsvII7Y2KXNLDk_krOW'}).text
            sale_price = div.find("div", attrs={'class': '_3j4dI1yA7cRfCvK8h406OB'}).text
            currency = org_price.split('$')[0]
        else:
            sale_perc = 0
            org_price = div.find("div", attrs={'class': '_3j4dI1yA7cRfCvK8h406OB'}).text
            sale_price = None
            currency = org_price.split('$')[0]
            
        # Change price to float
        org_price = float(org_price.split(' ')[1])
        if sale_price != None:
            sale_price = float(sale_price.split(' ')[1])
        
        # Change currency
        if currency == 'A':
            currency = 'AUD'
        elif currency == 'U':
            currency = 'USD'
        else:
            currency
            
        
        price.append([sale_perc, org_price, sale_price, currency])
        
        print(price)
        ### Process inner link
        # inner_link_extraction(game_link)
    
    driver.quit()
    # print(divs)
    
        

    



class Game:
    def __init__(self, title, tags, publish_date, developer, publisher, rate, 
                org_price, sale_price, is_free, user_reviews, game_modes, controller_sup, languages):
        self.title = title
        self.tags = tags
        self.publish_date = publish_date
        self.developer = developer
        self.publisher = publisher
        self.rate = rate
        self.org_price = org_price
        self.sale_price = sale_price
        self.is_free = is_free
        self.user_reviews = user_reviews
        self.languages = languages
        self.game_modes = game_modes
        self.controller_sup = controller_sup
        self.languages = languages
        
    

    

logger.info("Crawling!!!")