import matplotlib.pylab as plt
import pandas as pd
import requests,sqlite3,string
from bs4 import BeautifulSoup

def main_data(url):
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
    return df

def create_table(dir):
    try:
        conn = sqlite3.connect(dir)
        cousor = conn.cursor()
        sqlstr = """CREATE TABLE "data" (
            "日期"	TEXT NOT NULL ,
            "成交股數"	TEXT NOT NULL,
            "成交金額"	TEXT NOT NULL,
            "成交筆數"	TEXT NOT NULL,
            "發行量加權股價指數"	TEXT NOT NULL,
            "漲跌點數"	TEXT NOT NULL
        );"""
        cousor.execute(sqlstr)
        conn.close()
    except:
        pass

def write_data(url,dir1):
    data = main_data(url)
    len_=  len(data.loc[0:])
    len_1 = len(data.loc[0][0:])
    conn = sqlite3.connect(dir1)
    cousor = conn.cursor()
    x = 0
    l0,l1,l2,l3,l4,l5 = [],[],[],[],[],[]
    while x<len_1:
        for i in range(len_):
            if x == 0:
                l0.append(data.loc[i][x])
            elif x == 1:
                l1.append(data.loc[i][x])
            elif x == 2:
                l2.append(data.loc[i][x])
            elif x == 3:
                l3.append(data.loc[i][x])
            elif x == 4:
                l4.append(data.loc[i][x])
            elif x == 5:
                l5.append(data.loc[i][x])
        x+=1
    x = 0
    while x<len_:
        sqlstr = """
            INSERT into data VALUES
            (
            '{date}',
            '{data1}',
            '{data2}',
            '{data3}',
            '{data4}',
            '{data5}'
            )
            """.format(date=l0[x],data1=l1[x],data2=l2[x],data3=l3[x],data4=l4[x],data5=l5[x])
        cousor.execute(sqlstr)
        conn.commit()
        x+=1
    conn.close()

def to_sql(dir1):
    date = ['20200101','20200201','20200301','20200401','20200501','20200601','20200701','20200801']
    date = ['20200701']
    dir1 = "test.sqlite"
    for i in date:
        url = "https://www.twse.com.tw/exchangeReport/FMTQIK?response=json&date={date}".format(date=i)
        create_table(dir1)
        write_data(url,dir1)

def read_sql(dir1,data):
    conn = sqlite3.connect(dir1)
    cursor = conn.execute("SELECT 日期,{} FROM data".format(data))
    l0,l1 = [],[]
    for row in cursor:
        l0.append(row[0])
        l1.append(row[1])
    conn.close()
    return l0,l1

def data1(dir1): #成交筆數
    data = read_sql(dir1,'成交筆數')
    date = data[0]
    data_list = data[1]
    ndata_list = []
    for i in data_list:
        data = i.replace(',','')
        ndata_list.append(int(data))
    plt.title('One-month number of stock transactions')
    plt.xlabel('Days')
    plt.ylabel('Number of transactions')
    plt.plot(date,ndata_list,'o--r')
    plt.xticks(fontsize = 7)
    plt.grid(True)
    plt.show()

def data2(dir1): #發行量加權股價指數
    data = read_sql(dir1,'發行量加權股價指數')
    date = data[0]
    data_list = data[1]
    ndata_list = []
    for i in data_list:
        data = i.replace(',','')
        ndata_list.append(float(data))
    plt.title('One-month issuance weighted stock price index')
    plt.xlabel('Days')
    plt.ylabel('Issuance weighted stock index')
    plt.plot(date,ndata_list,'o--r')
    plt.xticks(fontsize = 7)
    plt.grid(True)
    plt.show()

def data3(dir1):
    data = read_sql(dir1,'漲跌點數')
    date = data[0]
    data_list = data[1]
    ndata_list = []
    for i in data_list:
        data = i.replace(',','')
        ndata_list.append(float(data))
    plt.title('Change points in a month')
    plt.xlabel('Days')
    plt.ylabel('Change points')
    plt.plot(date,ndata_list,'o--r')
    plt.xticks(fontsize = 7)
    plt.grid(True)
    plt.show()

def data4(dir1):
    data = read_sql(dir1,'成交金額')
    date = data[0]
    data_list = data[1]
    ndata_list = []
    for i in data_list:
        data = i.replace(',','')
        ndata_list.append(int(data))
    plt.title('One month transaction amount')
    plt.xlabel('Days')
    plt.ylabel('Turnover')
    plt.plot(date,ndata_list,'o--r')
    plt.xticks(fontsize=7)
    plt.grid(True)
    plt.show()    

def data5(dir1):
    data = read_sql(dir1,'成交股數')
    date = data[0]
    data_list = data[1]
    ndata_list = []
    for i in data_list:
        data = i.replace(',','')
        ndata_list.append(int(data))
    plt.title('')
    plt.xlabel('')
    plt.ylabel('')
    plt.plot(date,ndata_list,'o--r')
    plt.xticks(fontsize=7)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    dir1 = 'test.sqlite'
    #to_sql(dir1) #必須先寫入資料庫中才可讀取data
    #data1(dir1)
    #data2(dir1)
    #data3(dir1)
    #data4(dir1)
    #data5(dir1)