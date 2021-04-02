from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from utils import data


url = "https://covid19.saglik.gov.tr/"
uClient = urlopen(url)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser")
result = []
containers = page_soup.find('table', {'class': 'table table-striped'})

tds = containers.find_all("td")
i = 0
cities = []
points = []

while i < len(tds) - 1:
    cities.append(tds[i].text.strip())
    points.append(float(tds[i+1].text.replace(',', '.').strip()))
    i+=2

locations = {}
for city in data:
    if city['name'] == "Afyonkarahisar":
        locations['Afyon'] = [city['latitude'], city['longitude']]
    if city['name'] == "Elâzığ":
        locations['Elazığ'] = [city['latitude'], city['longitude']]
    if city['name'] == "Hakkâri":
        locations['Hakkari'] = [city['latitude'], city['longitude']]
    else:
        locations[city['name']] = [city['latitude'], city['longitude']]

latitudes = []
longitudes = []
for city in cities:
    latitudes.append(float(locations[city][0]))
    longitudes.append(float(locations[city][1]))

cities_df = pd.DataFrame()
cities_df['cities'] = cities
cities_df['risks'] = points
cities_df['latitudes'] = latitudes
cities_df['longitudes'] = longitudes

cities_df.to_csv("city_risks.csv", index=False)

print("done")