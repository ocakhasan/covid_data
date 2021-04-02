from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = "https://covid19.saglik.gov.tr/"
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")
result = []
containers = page_soup.find_all('g')

print(container)
