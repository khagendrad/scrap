from bs4 import BeautifulSoup
import requests 

html_text  = requests.get("https://www.worldometers.info/coronavirus/").text

soup = BeautifulSoup(html_text,'lxml')
print(soup)

#extraction