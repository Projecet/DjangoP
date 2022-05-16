import requests
from bs4 import BeautifulSoup
import warnings
import json
import pandas as pd
import csv

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

url = "https://www.worldometers.info/coronavirus/#main_table"
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")

# # 월드
# world_list = []
# for i in range(0, 15):
#     cases = soup.select_one('tbody:nth-child(2) > tr:nth-child(8) > td:nth-child(' + str(i + 1) + ')').text
#     world_list.append(cases)

# print(world_list)

# 국가
country_count = 120  # 불러올 상위 국가 갯수
country_list = []
for i in range(0, country_count):
    tem_list = []
    for j in (1,8,14):
        cases = soup.select_one('tbody:nth-child(2) > tr:nth-child(' + str(i+9) +
                                ') > td:nth-child(' + str(j+1) + ')').text
        tem_list.append(cases)
    country_list.append(tem_list)

# for l in country_list:
#     print(l)

data = pd.DataFrame(country_list)
data.columns = ['country_name','active_cases','population']
# data2 = data.replace('1553','50000000')
data2 = data.replace('N/A','0')

data2['active_cases'] = data2['active_cases'].apply(lambda x: x.replace(',', '')).astype(int)
data2['population'] = data2['population'].apply(lambda x: x.replace(',','')).astype(int)

data2.to_csv('worldcorona.csv',index=False)

