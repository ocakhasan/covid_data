import pandas as pd
import numpy as np
import re
import urllib.request
import json

URL = "https://covid19.saglik.gov.tr/"

contents = urllib.request.urlopen(URL).read().decode('utf-8')
x = re.search("var sondurumjson = \[(.*?)];//", contents).group(1)
# parse x:
response = json.loads(x)


def change_date(date):
    d = date.split('.')
    return d[2] + "-" + d[1] + "-" + d[0]

def change_num(data):
    data = data.replace('.', '')
    return int(data)

daily_confirmed = change_num(response['gunluk_vaka'])
daily_recovered = change_num(response['gunluk_iyilesen'])
daily_death = change_num(response['gunluk_vefat'])
confirmed = change_num(response['toplam_hasta'])
recovered = change_num(response['toplam_iyilesen'])
death = change_num(response['toplam_vefat'])
date = change_date(response['tarih'])
test = change_num(response['gunluk_test'])

to_add = [date, confirmed, recovered, death, test, daily_confirmed, daily_death, daily_recovered]


df = pd.read_csv("turkey_covid.csv")
if date != df['Date'].iloc[-1]:
    
    df.loc[df.shape[0]] = to_add
    df.to_csv("turkey_covid.csv", index=False)
    print("updated")
else:
    print("up to date")