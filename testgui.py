try:
    from PyQt5 import QtCore, QtGui, QtWidgets
    import sys,os
    sys.path.append('./test_matplotlib4.py')
    from test_matplotlib4 import Get_data
except:
    import sys,os
    os.system('pip3 install pyqt5')
    from PyQt5 import QtCore, QtGui, QtWidgets
    sys.path.append('./test_matplotlib4.py')
    from test_matplotlib4 import Get_data

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 205)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 120, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.show)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(350, 10, 241, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 10, 251, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 120, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.exit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 51, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(210, 50, 121, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(12, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "每月市場成交資訊圖表"))
        self.pushButton.setText(_translate("MainWindow", "取得圖表"))
        self.comboBox.setItemText(0, _translate("MainWindow", "成交筆數"))
        self.comboBox.setItemText(1, _translate("MainWindow", "發行量加權股價指數"))
        self.comboBox.setItemText(2, _translate("MainWindow", "漲跌點數"))
        self.comboBox.setItemText(3, _translate("MainWindow", "成交金額"))
        self.comboBox.setItemText(4, _translate("MainWindow", "成交股數"))
        self.pushButton_2.setText(_translate("MainWindow", "退出程序"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">資料選擇</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">日期選擇</span><span style=\" font-size:10pt; font-weight:600;\">:</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1990年"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1991年"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1992年"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1993年"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1994年"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "1995年"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "1996年"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "1997年"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "1998年"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "1999年"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "2000年"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "2001年"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "2002年"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "2003年"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "2004年"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "2005年"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "2006年"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "2007年"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "2008年"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "2009年"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "2010年"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "2011年"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "2012年"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "2013年"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "2014年"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "2015年"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "2016年"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "2017年"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "2018年"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "2019年"))
        self.comboBox_2.setItemText(30, _translate("MainWindow", "2020年"))
        self.comboBox_2.setItemText(31, _translate("MainWindow", "2021年"))
        self.comboBox_2.setItemText(32, _translate("MainWindow", "2022年"))
        self.comboBox_2.setItemText(33, _translate("MainWindow", "2023年"))
        self.comboBox_2.setItemText(34, _translate("MainWindow", "2024年"))
        self.comboBox_2.setItemText(35, _translate("MainWindow", "2025年"))
        self.comboBox_2.setItemText(36, _translate("MainWindow", "2026年"))
        self.comboBox_2.setItemText(37, _translate("MainWindow", "2027年"))
        self.comboBox_2.setItemText(38, _translate("MainWindow", "2028年"))
        self.comboBox_2.setItemText(39, _translate("MainWindow", "2029年"))
        self.comboBox_2.setItemText(40, _translate("MainWindow", "2030年"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "01月"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "02月"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "03月"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "04月"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "05月"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "06月"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "07月"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "08月"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "09月"))
        self.comboBox_3.setItemText(9, _translate("MainWindow", "10月"))
        self.comboBox_3.setItemText(10, _translate("MainWindow", "11月"))
        self.comboBox_3.setItemText(11, _translate("MainWindow", "12月"))
    
    def exit(self):
        sys.exit(app.exec_())
    
    def show(self):
        self.text_year = str(self.comboBox_2.currentText())
        self.text_year1 = self.text_year.replace('年',"")
        self.text_month = str(self.comboBox_3.currentText())
        self.text_month1 = self.text_month.replace('月',"")
        self.text = str(self.comboBox.currentText())
        print(self.text_year1,self.text_month1,self.text)
        self.textBrowser.append('正在搜尋:')
        self.textBrowser.insertPlainText(self.text)
        self.textBrowser.insertPlainText(self.text_year)
        self.textBrowser.insertPlainText(self.text_month)
        self.dir = "test.sqlite"
        self.get = Get_data()
        try:
            self.get.to_sql(self.dir,self.text_year1,self.text_month1)
            self.textBrowser.append('查找成功!')
            if self.text == "成交筆數":
                self.get.data1(self.dir)
            elif self.text == "發行量加權股價指數":
                self.get.data2(self.dir)
            elif self.text == "漲跌點數":
                self.get.data3(self.dir)
            elif self.text == "成交金額":
                self.get.data4(self.dir)
            elif self.text == "成交股數":
                self.get.data5(self.dir)
        except:
            self.textBrowser.append('不存在的日期!')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())