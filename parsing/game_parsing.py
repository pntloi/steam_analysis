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
    
    
def pagination(load_time):
    for i in range(load_time):
        driver.find_element(by=By.CLASS_NAME, value="_2tkiJ4VfEdI9kq1agjZyNz").click()
        time.sleep(3)
        
        
def load_fetch_data(link, load_time):
    driver.get(link)
    
    for _ in range(110):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
        time.sleep(0.0001)
    
    time.sleep(2)
    pagination(load_time)
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    return bs

def outer_link_extraction(link):
    game_list = []
    
    bs = load_fetch_data(link, load_time=3)
    
    category = bs.find("div", attrs={'class': 'saHqNV-7xE9caBAreUZiX'}).text
    # button = driver.find_element(by=By.CLASS_NAME, value="_2tkiJ4VfEdI9kq1agjZyNz")
    # driver.find_element(by=By.XPATH, '//button[@class="_2tkiJ4VfEdI9kq1agjZyNz"]').click()
    
    # button = bs.find("button", attrs={'class': '_2tkiJ4VfEdI9kq1agjZyNz'})
    # button.click()
    
    time.sleep(2)
    
    section = bs.find("div", attrs={'id': 'SaleSection_13268'}).find("div", attrs={'class': '_1cOoCFwafBlSkwllIMf3XM'})
    section_divs = section.find_all("div", attrs={'class': ['_2hhNOdcC6yLwL_rugP3YLf', '_37iggltdgh0RtNIECJCfOj']})
    
    game_info = []
    
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
        
        
        ### Game description
        if div.find("div", attrs={'class': '_3AsE5JhqLAiICKUYvZLpap'}) != None:
            desc = div.find("div", attrs={'class': '_3AsE5JhqLAiICKUYvZLpap'}).text
        else:
            desc = "No description"
        
        
        ### Game Genre
        genre = [a.text for a in div.find("div", attrs={'class': '_2bkP-3b7dvr0a_qPdZEfHY'})]
        
        
        ### Game rating
        rating = div.find("div", attrs={'class': '_2nuoOi5kC2aUI12z85PneA'}).text
        
        
        ### User reviews
        u_reviews = div.find("div", attrs={'class': '_1wXL_MfRpdKQ3wZiNP5lrH'}).text
                
        
        ### Sale percentage
        price = []
        if div.find("div", attrs={'class': 'cnkoFkzVCby40gJ0jGGS4'}) != None:
            sale_perc = div.find("div", attrs={'class': 'cnkoFkzVCby40gJ0jGGS4'}).text
            org_price = div.find("div", attrs={'class': '_3fFFsvII7Y2KXNLDk_krOW'}).text
            sale_price = div.find("div", attrs={'class': '_3j4dI1yA7cRfCvK8h406OB'}).text
            currency = org_price.split('$')[0]
        else:
            sale_perc = '0%'
            org_price = div.find("div", attrs={'class': '_3j4dI1yA7cRfCvK8h406OB'}).text
            sale_price = None
            currency = org_price.split('$')[0]
            
            
        # Change price to float
        # if isinstance(org_price.split(' ')[1], float):
        #     org_price = float(org_price.split(' ')[1])
        # else:
        #     org_price

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
        

        ### Return all games info
        game_sample = {
                "link": game_link,
                "name": game_name,
                "category": category,
                "genre": genre,
                "picture": game_pic,
                "description": desc,
                "rating": rating,
                "reviews": u_reviews,
                "release_date": date_release,
                "price": price
            }

        game_info.append(game_sample)
    
    driver.quit()
    return game_info
    

logger.info("Crawling!!!")