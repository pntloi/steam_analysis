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



# class Game:
#     def __init__(self, link, title, tags, publish_date, developer, publisher, rate, 
#                 org_price, sale_price, is_free, user_reviews, game_modes, controller_sup, languages):
#         self.link = link
#         self.title = title
#         self.tags = tags
#         self.publish_date = publish_date
#         self.developer = developer
#         self.publisher = publisher
#         self.rate = rate
#         self.org_price = org_price
#         self.sale_price = sale_price
#         self.is_free = is_free
#         self.user_reviews = user_reviews
#         self.languages = languages
#         self.game_modes = game_modes
#         self.controller_sup = controller_sup
#         self.languages = languages
        
        
        
logger = logging.getLogger()

driver = webdriver.Edge()

def game_info_extraction(link):
    info_list = []
    
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    time.sleep(3)
    
    game_mode = []
    
    game_mode_section = bs.find("div", attrs={'class': 'game_area_features_list_ctn'}).find_all('a', attrs={'class': 'game_area_details_specs_ctn'})
    
    for mode in game_mode_section:
        available_mode = mode.text
        mode_link = mode['href']
        game_mode.append({
            'mode': available_mode,
            'link': mode_link
        })
        
    print(game_mode)
    
    


    
    
    
    driver.quit()


logger.info("Crawling!!!")