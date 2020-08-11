import matplotlib.pylab as plt
import pandas as pd
import requests,sqlite3
from bs4 import BeautifulSoup
url = "https://www.twse.com.tw/exchangeReport/FMTQIK?response=json&date=20200701"
r = requests.get(url)
r = r.json()
title = r['title'] #標題
fields = r['fields'] #欄位
data = r['data'] #資料
x = 0
list0 = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
while x<6:
    for i in range(len(data)):
        if x == 0:
            list0.append(data[i][x])
        elif x == 1:
            list1.append(data[i][x])
        elif x == 2:
            list2.append(data[i][x])
        elif x == 3:
            list3.append(data[i][x])
        elif x == 4:
            list4.append(data[i][x])
        elif x == 5:
            list5.append(data[i][x])
    x+=1
dict1 = {fields[0]:list0,fields[1]:list1,fields[2]:list2,fields[3]:list3,fields[4]:list4,fields[5]:list5}
df = pd.DataFrame(dict1)
df2 = df.set_index('日期')
print(df2)
df.to_csv('test.csv')