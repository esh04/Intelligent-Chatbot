import pandas as pd
import requests
from bs4 import BeautifulSoup


def news(state):
    state = state.lower()

    url = "https://www.bing.com/news/search?q="+state+"+covid"
    
    # make a GET request to fetch the raw HTML content
    web_content = requests.get(url).content
    
    # parse the html content
    soup = BeautifulSoup(web_content, "html.parser")
    
    allNews = ''

    for headline in soup.findAll("a",class_="title"):
        allNews += headline.text.strip()+' ; '+headline['href']+'\n\n'

    return(allNews)