import sys
from tkinter.tix import Form

# import MyGUI as MyGUI
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog

# indicators
t200 = {"name": "The 200!", "gWeight": 2, "bWeight": -2, "spc": "Is the 200 crossing up or down?", "gsp": 1,
        "bsp": -1.5, "notes": ""}
t9 = {"name": "The 9!", "gWeight": 1.5, "bWeight": -1.5,
      "spc": "Is it One candle close above or below thw nine the 9? (Means get in or watch or get out if below)",
      "gsp": 1.5, "bsp": -1.5, "notes": "Prob close when under 9"}
MACD = {"name": "MACD", "gWeight": 1.5, "bWeight": -1.5, "spc": "Is the MACD reversing up or down, is it crossing?",
        "gsp": 1.5, "bsp": -1.5, "notes": ""}
RSI = {"name": "RSI", "gWeight": 1, "bWeight": -1, "spc": "Is the RSI  Oversold(good)(y) or Overbought(bad)(n)?", "gsp": 1.5,
       "bsp": -1, "notes": "over bought for selling only"}
VWAP = {"name": "VWAP", "gWeight": 1.5, "bWeight": -1.5, "spc": "None/WIP", "gsp": 0, "bsp": 0,
        "notes": ""}
HA = {"name": "Heiken Ashi", "gWeight": 1.2, "bWeight": -1, "spc": "None/WIP", "gsp": 0, "bsp": 0,
      "notes": ""}
SHAC = {"name": "Smoothed Ha Candles", "gWeight": 1.2, "bWeight": -1, "spc": "None/WIP", "gsp": 0, "bsp": 0,
        "notes": ""}
RIB = {"name": "Ribbons", "gWeight": 1.5, "bWeight": -1.5, "spc": "None/WIP", "gsp": 0, "bsp": 0,
       "notes": ""}
VPVR = {"name": "VPVR", "gWeight": 1.2, "bWeight": -1, "spc": "Is it Jump Up/Jump Down?", "gsp": 2, "bsp": -2,
        "notes": "Good for crypto."}
# t9 = {"name" : "The 9!", "gWeight" : 1.5, "bWeight" : -1.5, "spc" : "Is it One candle close above or below thw nine the 9? (Means get in or watch or get out if below)", "gsp" : 1.5, "bsp" : -1.5, "notes" : "Prob close when under 9"}
others = ["Support", "Resistance", "Moveing Averages", "VBottoms (for entry) and etc...", "Wedges and etc...",
          "Divergence (really bad)", "Earnings Call (bad)"]
# LUX = "Is it neer a cloud?"
LUX = {"name": "LUX", "gWeight": 1, "bWeight": -1, "spc": "Is it neer a cloud? Buy Cloud(y) Sell Cloud(n)", "gsp": 1.5, "bsp": -1.5,
       "notes": "Prob close when under 9"}

# Form, Window = uic.loadUiType("Stock-Watchlist-Logger.ui")

class homeScreen(QDialog):

    def __init__(self):
        super(homeScreen, self).__init__()
        uic.loadUi("homeScreenDialog.ui", self)
        # self.show()
        self.stockCheck_button.clicked.connect(self.showStockCheck)

    def showStockCheck(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)


class stockCheck(QDialog):
    def __init__(self):
        super(stockCheck, self).__init__()
        uic.loadUi("stockCheckDialog.ui", self)
        # Hideing the SPC's
        self.LUX_SPC.hide()
        self.MACD_SPC.hide()
        self.RSI_SPC.hide()
        self.VPVR_SPC.hide()
        self.nine_SPC.hide()
        self.twohundred_SPC.hide()

        #TODO
        # make compact ver with just one checkbox instead of two radio buttons

        # self.halal_Box.setChecked(True) # Example

        # Scoring

        #Vars
        self.twoHundred = False
        self.nine = False
        self.MACD = False
        self.RSI = False
        self.VWAP = False
        self.HA = False
        self.SHAC = False
        self.RIB = False
        self.VPVR = False
        self.LUX = False

        self.submit_Button.clicked.connect(self.score)

        #TODO
        # there are SPC's in all of the places even though not all of them use them, maby add SPC's later?

        #t200
        self.twohundred_Is_True.clicked.connect(self.twohundred_is_True)
        self.twohundred_Is_False.clicked.connect(self.twohundred_is_False)
        self.twohundred_Check_True.clicked.connect(self.twohundred_check_True)
        self.twohundred_Check_False.clicked.connect(self.twohundred_check_False)
        self.twohundred_SPC_True.clicked.connect(self.twohundred_spc_True)
        self.twohundred_SPC_False.clicked.connect(self.twohundred_spc_False)
        #t9
        self.nine_Is_True.clicked.connect(self.nine_is_True)
        self.nine_Is_False.clicked.connect(self.nine_is_False)
        self.nine_Check_True.clicked.connect(self.nine_check_True)
        self.nine_Check_False.clicked.connect(self.nine_check_False)
        self.nine_SPC_True.clicked.connect(self.nine_spc_True)
        self.nine_SPC_False.clicked.connect(self.nine_spc_False)
        #MACD
        self.MACD_Is_True.clicked.connect(self.MACD_is_True)
        self.MACD_Is_False.clicked.connect(self.MACD_is_False)
        self.MACD_Check_True.clicked.connect(self.MACD_check_True)
        self.MACD_Check_False.clicked.connect(self.MACD_check_False)
        self.MACD_SPC_True.clicked.connect(self.MACD_spc_True)
        self.MACD_SPC_False.clicked.connect(self.MACD_spc_False)
        #RSI
        self.RSI_Is_True.clicked.connect(self.RSI_is_True)
        self.RSI_Is_False.clicked.connect(self.RSI_is_False)
        self.RSI_Check_True.clicked.connect(self.RSI_check_True)
        self.RSI_Check_False.clicked.connect(self.RSI_check_False)
        self.RSI_SPC_True.clicked.connect(self.RSI_spc_True)
        self.RSI_SPC_False.clicked.connect(self.RSI_spc_False)
        #VWAP
        self.VWAP_Is_True.clicked.connect(self.VWAP_is_True)
        self.VWAP_Is_False.clicked.connect(self.VWAP_is_False)
        self.VWAP_Check_True.clicked.connect(self.VWAP_check_True)
        self.VWAP_Check_False.clicked.connect(self.VWAP_check_False)
        self.VWAP_SPC_True.clicked.connect(self.VWAP_spc_True)
        self.VWAP_SPC_False.clicked.connect(self.VWAP_spc_False)
        #HA
        self.HA_Is_True.clicked.connect(self.HA_is_True)
        self.HA_Is_False.clicked.connect(self.HA_is_False)
        self.HA_Check_True.clicked.connect(self.HA_check_True)
        self.HA_Check_False.clicked.connect(self.HA_check_False)
        self.HA_SPC_True.clicked.connect(self.HA_spc_True)
        self.HA_SPC_False.clicked.connect(self.HA_spc_False)
        #SHAC
        self.SHAC_Is_True.clicked.connect(self.SHAC_is_True)
        self.SHAC_Is_False.clicked.connect(self.SHAC_is_False)
        self.SHAC_Check_True.clicked.connect(self.SHAC_check_True)
        self.SHAC_Check_False.clicked.connect(self.SHAC_check_False)
        self.SHAC_SPC_True.clicked.connect(self.SHAC_spc_True)
        self.SHAC_SPC_False.clicked.connect(self.SHAC_spc_False)
        #RIB
        self.RIB_Is_True.clicked.connect(self.RIB_is_True)
        self.RIB_Is_False.clicked.connect(self.RIB_is_False)
        self.RIB_Check_True.clicked.connect(self.RIB_check_True)
        self.RIB_Check_False.clicked.connect(self.RIB_check_False)
        self.RIB_SPC_True.clicked.connect(self.RIB_spc_True)
        self.RIB_SPC_False.clicked.connect(self.RIB_spc_False)
        #VPVR
        self.VPVR_Is_True.clicked.connect(self.VPVR_is_True)
        self.VPVR_Is_False.clicked.connect(self.VPVR_is_False)
        self.VPVR_Check_True.clicked.connect(self.VPVR_check_True)
        self.VPVR_Check_False.clicked.connect(self.VPVR_check_False)
        self.VPVR_SPC_True.clicked.connect(self.VPVR_spc_True)
        self.VPVR_SPC_False.clicked.connect(self.VPVR_spc_False)
        #LUX
        self.LUX_Is_True.clicked.connect(self.LUX_is_True)
        self.LUX_Is_False.clicked.connect(self.LUX_is_False)
        self.LUX_Check_True.clicked.connect(self.LUX_check_True)
        self.LUX_Check_False.clicked.connect(self.LUX_check_False)
        self.LUX_SPC_True.clicked.connect(self.LUX_spc_True)
        self.LUX_SPC_False.clicked.connect(self.LUX_spc_False)

        # self.show()

    def score(self):
        pass


    #t200
    def twohundred_is_True(self):
        pass
    def twohundred_is_False(self):
        pass
    def twohundred_check_True(self):
        pass
    def twohundred_check_False(self):
        pass
    def twohundred_spc_True(self):
        pass
    def twohundred_spc_False(self):
        pass
    #t9
    def nine_is_True(self):
        pass
    def nine_is_False(self):
        pass
    def nine_check_True(self):
        pass
    def nine_check_False(self):
        pass
    def nine_spc_True(self):
        pass
    def nine_spc_False(self):
        pass
    #MACD
    def MACD_is_True(self):
        pass
    def MACD_is_False(self):
        pass
    def MACD_check_True(self):
        pass
    def MACD_check_False(self):
        pass
    def MACD_spc_True(self):
        pass
    def MACD_spc_False(self):
        pass
    #RSI
    def RSI_is_True(self):
        pass
    def RSI_is_False(self):
        pass
    def RSI_check_True(self):
        pass
    def RSI_check_False(self):
        pass
    def RSI_spc_True(self):
        pass
    def RSI_spc_False(self):
        pass
    #VWAP
    def VWAP_is_True(self):
        pass
    def VWAP_is_False(self):
        pass
    def VWAP_check_True(self):
        pass
    def VWAP_check_False(self):
        pass
    def VWAP_spc_True(self):
        pass
    def VWAP_spc_False(self):
        pass
    #HA
    def HA_is_True(self):
        pass
    def HA_is_False(self):
        pass
    def HA_check_True(self):
        pass
    def HA_check_False(self):
        pass
    def HA_spc_True(self):
        pass
    def HA_spc_False(self):
        pass
    #SHAC
    def SHAC_is_True(self):
        pass
    def SHAC_is_False(self):
        pass
    def SHAC_check_True(self):
        pass
    def SHAC_check_False(self):
        pass
    def SHAC_spc_True(self):
        pass
    def SHAC_spc_False(self):
        pass
    #RIB
    def RIB_is_True(self):
        pass
    def RIB_is_False(self):
        pass
    def RIB_check_True(self):
        pass
    def RIB_check_False(self):
        pass
    def RIB_spc_True(self):
        pass
    def RIB_spc_False(self):
        pass
    #VPVR
    def VPVR_is_True(self):
        pass
    def VPVR_is_False(self):
        pass
    def VPVR_check_True(self):
        pass
    def VPVR_check_False(self):
        pass
    def VPVR_spc_True(self):
        pass
    def VPVR_spc_False(self):
        pass
    #LUX
    def LUX_is_True(self):
        pass
    def LUX_is_False(self):
        pass
    def LUX_check_True(self):
        pass
    def LUX_check_False(self):
        pass
    def LUX_spc_True(self):
        pass
    def LUX_spc_False(self):
        pass







def main():
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()
    home = homeScreen()
    stock = stockCheck()
    widget.addWidget(home)
    widget.addWidget(stock)

    widget.show()
    app.exec_()



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
home = homeScreen()
stock = stockCheck()
widget.addWidget(home)
widget.addWidget(stock)
widget.show()
app.exec_()


def on_clicked(msg):
    print("Button Clicked!!!")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


#if __name__ == '__main__':
    main()
