from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import logging

logger = logging.getLogger()

all_cat = []

def flatten(input):
    new_list = []
    
    for i in input:
        if len(i) > 0 and i != None:
            for j in i:
                new_list.append(j)
    return new_list

def category_extract(link):
    unprocessed_list = []
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    category_list = bs.find_all("div", attrs={'class':['popup_genre_expand_header', 'popup_genre_expand_content']})

    for category in category_list:
        category_item = [a['href'] for a in category.find_all('a', href=True)]
        # print(category_item)
        # print("\n")
        unprocessed_list.append(category_item)
    all_cat = flatten(unprocessed_list)  
    return all_cat


logger.info("Crawling Category!!!")
    
    
    
    

