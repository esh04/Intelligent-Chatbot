import pandas as pd
import requests
from bs4 import BeautifulSoup

# https://towardsdatascience.com/tracking-corona-covid-19-spread-in-india-using-python-40ef8ffa7e31
def covidStatistic(state):
    state = state.title()
    url = "https://www.oneindia.com/coronavirus-affected-cities-districts-in-india.html"
    
    # make a GET request to fetch the raw HTML content
    web_content = requests.get(url).content
    
    # parse the html content
    soup = BeautifulSoup(web_content, "html.parser")
    
    table = soup.find(id=state) 
    if table is None:
        print("No such state exists in India. Please recheck your spelling.")
        return

    rows = table.findAll('td')
    total = rows[1].text.strip().split('  ')
    deaths = rows[2].text.strip().split('  ')
    recovered = rows[3].text.strip().split('  ')
    stats = 'Covid Statistics of '+state+'\nTotal Cases: '+total[0]+'; Total New Cases: '+total[1]+'\nTotal Deaths: '+deaths[0]+'; Total New Deaths: '+deaths[1]+'\nTotal Recovered: '+recovered[0]+'; Total New Recovered: '+recovered[1]
    return stats

