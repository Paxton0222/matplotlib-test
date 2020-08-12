import matplotlib.pylab as plt
import pandas as pd
import requests,sqlite3,string,os
from bs4 import BeautifulSoup
class Get_data:
    def __init__(self):
        pass
    def main_data(self,url):
        self.r = requests.get(url)
        self.r = self.r.json()
        self.title = self.r['title'] #標題
        self.fields = self.r['fields'] #欄位
        self.data = self.r['data'] #資料
        self.x = 0
        self.list0 = []
        self.list1 = []
        self.list2 = []
        self.list3 = []
        self.list4 = []
        self.list5 = []
        while self.x<6:
            for self.i in range(len(self.data)):
                if self.x == 0:
                    self.list0.append(self.data[self.i][self.x])
                elif self.x == 1:
                    self.list1.append(self.data[self.i][self.x])
                elif self.x == 2:
                    self.list2.append(self.data[self.i][self.x])
                elif self.x == 3:
                    self.list3.append(self.data[self.i][self.x])
                elif self.x == 4:
                    self.list4.append(self.data[self.i][self.x])
                elif self.x == 5:
                    self.list5.append(self.data[self.i][self.x])
            self.x+=1
        self.dict1 = {self.fields[0]:self.list0,self.fields[1]:self.list1,self.fields[2]:self.list2,self.fields[3]:self.list3,self.fields[4]:self.list4,self.fields[5]:self.list5}
        self.df = pd.DataFrame(self.dict1)
        df2 = self.df.set_index('日期')
        return self.df

    def create_table(self,dir):
        try:
            self.conn = sqlite3.connect(dir)
            self.cousor = self.conn.cursor()
            self.sqlstr = """CREATE TABLE "data" (
                "日期"	TEXT NOT NULL ,
                "成交股數"	TEXT NOT NULL,
                "成交金額"	TEXT NOT NULL,
                "成交筆數"	TEXT NOT NULL,
                "發行量加權股價指數"	TEXT NOT NULL,
                "漲跌點數"	TEXT NOT NULL
            );"""
            self.cousor.execute(self.sqlstr)
            self.conn.close()
        except:
            pass

    def write_data(self,url,dir1):
        self.data = self.main_data(url)
        self.len_=  len(self.data.loc[0:])
        self.len_1 = len(self.data.loc[0][0:])
        self.conn = sqlite3.connect(dir1)
        self.cousor = self.conn.cursor()
        self.x = 0
        self.l0,self.l1,self.l2,self.l3,self.l4,self.l5 = [],[],[],[],[],[]
        while self.x<self.len_1:
            for self.i in range(self.len_):
                if self.x == 0:
                    self.l0.append(self.data.loc[self.i][self.x])
                elif self.x == 1:
                    self.l1.append(self.data.loc[self.i][self.x])
                elif self.x == 2:
                    self.l2.append(self.data.loc[self.i][self.x])
                elif self.x == 3:
                    self.l3.append(self.data.loc[self.i][self.x])
                elif self.x == 4:
                    self.l4.append(self.data.loc[self.i][self.x])
                elif self.x == 5:
                    self.l5.append(self.data.loc[self.i][self.x])
            self.x+=1
        self.x = 0
        while self.x<self.len_:
            self.sqlstr = """
                INSERT into data VALUES
                (
                '{date}',
                '{data1}',
                '{data2}',
                '{data3}',
                '{data4}',
                '{data5}'
                )
                """.format(date=self.l0[self.x],data1=self.l1[self.x],data2=self.l2[self.x],data3=self.l3[self.x],data4=self.l4[self.x],data5=self.l5[self.x])
            self.cousor.execute(self.sqlstr)
            self.conn.commit()
            self.x+=1
        self.conn.close()

    def to_sql(self,dir1,year,month):
        try:
            os.remove(dir1)
        except:
            pass
        self.date = year+month
        self.date = [self.date]
        for self.i in self.date:
            self.url = "https://www.twse.com.tw/exchangeReport/FMTQIK?response=json&date={date}01".format(date=self.i)
            self.create_table(dir1)
            self.write_data(self.url,dir1)

    def read_sql(self,dir1,data):
        self.conn = sqlite3.connect(dir1)
        self.cursor = self.conn.execute("SELECT 日期,{} FROM data".format(data))
        self.l0,self.l1 = [],[]
        for self.row in self.cursor:
            self.l0.append(self.row[0])
            self.l1.append(self.row[1])
        self.conn.close()
        return self.l0,self.l1

    def read_all_sql(self,dir1):
        self.conn = sqlite3.connect(dir1)
        self.cursor = self.conn.execute("SELECT * FROM data")
        self.l0,self.l1,self.l2,self.l3,self.l4,self.l5 = [],[],[],[],[],[]
        for self.row in self.cursor:
            self.l0.append(self.row[0])
            self.l1.append(self.row[1])
            self.l2.append(self.row[2])
            self.l3.append(self.row[3])
            self.l4.append(self.row[4])
            self.l5.append(self.row[5])
        self.conn.close()
        return self.l0,self.l1,self.l2,self.l3,self.l4,self.l5

    def data1(self,dir1): #成交筆數
        self.data = self.read_sql(dir1,'成交筆數')
        self.date = self.data[0]
        self.data_list = self.data[1]
        self.ndata_list = []
        for self.i in self.data_list:
            self.data = self.i.replace(',','')
            self.ndata_list.append(int(self.data))
        plt.title('One-month number of stock transactions')
        plt.xlabel('Days')
        plt.ylabel('Number of transactions')
        plt.plot(self.date,self.ndata_list,'o--r')
        plt.xticks(fontsize = 7)
        plt.grid(True)
        plt.show()

    def data2(self,dir1): #發行量加權股價指數
        self.data = self.read_sql(dir1,'發行量加權股價指數')
        self.date = self.data[0]
        self.data_list = self.data[1]
        self.ndata_list = []
        for self.i in self.data_list:
            self.data = self.i.replace(',','')
            self.ndata_list.append(float(self.data))
        plt.title('One-month issuance weighted stock price index')
        plt.xlabel('Days')
        plt.ylabel('Issuance weighted stock index')
        plt.plot(self.date,self.ndata_list,'o--r')
        plt.xticks(fontsize = 7)
        plt.grid(True)
        plt.show()

    def data3(self,dir1): #漲跌點數
        self.data = self.read_sql(dir1,'漲跌點數')
        self.date = self.data[0]
        self.data_list = self.data[1]
        self.ndata_list = []
        for self.i in self.data_list:
            self.data = self.i.replace(',','')
            self.ndata_list.append(float(self.data))
        plt.title('Change points in a month')
        plt.xlabel('Days')
        plt.ylabel('Change points')
        plt.plot(self.date,self.ndata_list,'o--r')
        plt.xticks(fontsize = 7)
        plt.grid(True)
        plt.show()

    def data4(self,dir1): #成交金額
        self.data = self.read_sql(dir1,'成交金額')
        self.date = self.data[0]
        self.data_list = self.data[1]
        self.ndata_list = []
        for self.i in self.data_list:
            self.data = self.i.replace(',','')
            self.ndata_list.append(int(self.data))
        plt.title('One month transaction amount')
        plt.xlabel('Days')
        plt.ylabel('Turnover')
        plt.plot(self.date,self.ndata_list,'o--r')
        plt.xticks(fontsize=7)
        plt.grid(True)
        plt.show()    

    def data5(self,dir1): #成交股數
        self.data = self.read_sql(dir1,'成交股數')
        self.date = self.data[0]
        self.data_list = self.data[1]
        self.ndata_list = []
        for self.i in self.data_list:
            self.data = self.i.replace(',','')
            self.ndata_list.append(int(self.data))
        plt.title('Number of shares traded in a month')
        plt.xlabel('Days')
        plt.ylabel('Number of shares traded')
        plt.plot(self.date,self.ndata_list,'o--r')
        plt.xticks(fontsize=7)
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    dir1 = 'test.sqlite' #資料庫路徑(不須更改)
    year = '2019' #更改日期 
    month = '1'
    get = Get_data()
    get.to_sql(dir1,year,month) #必須先寫入資料庫中才可讀取data
    print(get.read_all_sql(dir1)) #讀取sql中所有資料
    #get.data1(dir1) #成交筆數
    #get.data2(dir1) #發行量加權股價指數
    #get.data3(dir1) #漲跌點數
    #get.data4(dir1) #成交金額
    #get.data5(dir1) #成交股數
    