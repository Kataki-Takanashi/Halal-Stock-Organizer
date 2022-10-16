import sys
import __init__
import random
import time as t
import json
from datetime import date
from datetime import datetime


# Settings
#Testing
testMode = False

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
today = date.today()
date = today.strftime("%d/%m/%Y")
timestamp = dt_string
# Variables
num = random.randint(0, 10000)
num2 = str(num)
# import MyGUI as MyGUI
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog

yes = ["yes", "yep", "yea", "y", "yup", "true", "t", "Yes", "Yep", "Yea", "Y", "Yup", True, "True", "T", "halal",
       "Halal", "a", "o", "A", "O", "above", "Above", "over", "Over", "g", "G", "up", "Up", "UP", "", " "]
no = ["no", "n", "false", "f", "nope", "No", "N", False, "False", "F", "Nope", "nothalal", "Nothalal", "notHalal",
      "NotHalal", "nah", "Nah", "u", "b", "U", "B", "under", "below", "Under", "Below", "down", "Down", "DOWN"]
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
        self.halalCheck_Button.clicked.connect(self.halalchic)
        self.seeHalal_Button.clicked.connect(self.goSeeHalal)
        self.seeNotHalal_Button.clicked.connect(self.goSeeNotHalal)
        self.history_Button.clicked.connect(self.goSeeHistory)
        self.ticker_history_Button.clicked.connect(self.goSeeTickerHistory)
        self.yesterday_Button.clicked.connect(self.goSeeYesterday)
        self.today_Button.clicked.connect(self.goSeeToday)

    def showStockCheck(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def halalchic(self):
        widget.setCurrentIndex(widget.currentIndex() + 2)
    def goSeeHalal(self):
        widget.setCurrentIndex(widget.currentIndex() + 3)
    def goSeeNotHalal(self):
        widget.setCurrentIndex(widget.currentIndex() + 4)
    def goSeeHistory(self):
        widget.setCurrentIndex(widget.currentIndex() + 5)
    def goSeeTickerHistory(self):
        widget.setCurrentIndex(widget.currentIndex() + 6)
    def goSeeYesterday(self):
        widget.setCurrentIndex(widget.currentIndex() + 7)
    def goSeeToday(self):
        widget.setCurrentIndex(widget.currentIndex() + 8)


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
        self.new_Ticker.hide()
        self.another_Button.hide()
        self.home_Button.hide()
        self.q_Area.setEnabled(False)

        #TODO
        # make compact ver with just one checkbox instead of two radio buttons

        # self.halal_Box.setChecked(True) # Example

        # Scoring

        #Vars
        self.twoHundred = False
        self.twoHundred_spc = False
        self.nine = False
        self.nine_spc = False
        self.MACD = False
        self.MACD_spc = False
        self.RSI = False
        self.RSI_spc = False
        self.VWAP = False
        self.VWAP_spc = False
        self.HA = False
        self.HA_spc = False
        self.SHAC = False
        self.SHAC_spc = False
        self.RIB = False
        self.RIB_spc = False
        self.VPVR = False
        self.VPVR_spc = False
        self.LUX = False
        self.LUX_spc = False

        self.indicators = []

        self.submit_Button.clicked.connect(self.score)
        #self.ticker_Input.cursorPositionChanged.connect(self.submited)
        self.ticker_Input.returnPressed.connect(self.checkHalal)
        self.ticker_Input.textEdited.connect(self.checkTicker)
        #self.ticker_Input.textEdited.connect(self.setUpper)
        self.halal_Box.clicked.connect(self.disable_Halal)
        self.another_Button.clicked.connect(self.reset)
        self.home_Button.clicked.connect(self.goHome)
        self.home_Button_2.clicked.connect(self.goHome)

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
        # self.VWAP_Check_True.clicked.connect(self.VWAP_check_True)
        # self.VWAP_Check_False.clicked.connect(self.VWAP_check_False)
        # self.VWAP_SPC_True.clicked.connect(self.VWAP_spc_True)
        # self.VWAP_SPC_False.clicked.connect(self.VWAP_spc_False)
        #HA
        self.HA_Is_True.clicked.connect(self.HA_is_True)
        self.HA_Is_False.clicked.connect(self.HA_is_False)
        # self.HA_Check_True.clicked.connect(self.HA_check_True)
        # self.HA_Check_False.clicked.connect(self.HA_check_False)
        # self.HA_SPC_True.clicked.connect(self.HA_spc_True)
        # self.HA_SPC_False.clicked.connect(self.HA_spc_False)
        #SHAC
        self.SHAC_Is_True.clicked.connect(self.SHAC_is_True)
        self.SHAC_Is_False.clicked.connect(self.SHAC_is_False)
        # self.SHAC_Check_True.clicked.connect(self.SHAC_check_True)
        # self.SHAC_Check_False.clicked.connect(self.SHAC_check_False)
        # self.SHAC_SPC_True.clicked.connect(self.SHAC_spc_True)
        # self.SHAC_SPC_False.clicked.connect(self.SHAC_spc_False)
        #RIB
        self.RIB_Is_True.clicked.connect(self.RIB_is_True)
        self.RIB_Is_False.clicked.connect(self.RIB_is_False)
        # self.RIB_Check_True.clicked.connect(self.RIB_check_True)
        # self.RIB_Check_False.clicked.connect(self.RIB_check_False)
        # self.RIB_SPC_True.clicked.connect(self.RIB_spc_True)
        # self.RIB_SPC_False.clicked.connect(self.RIB_spc_False)
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



    def submited(self):
        t.sleep(.5)
        self.submit_Button.setText("Submit")

    def setUpper(self):
        text = self.ticker_Input.text()
        self.ticker_Input.setText(text.upper())

    def checkHalal(self):
        name = self.ticker_Input.text().upper()
        # if name.lower() == "exit":
        #     self.goHome()
        self.ticker_Input.setEnabled(False)

        if name in seeStock("halal"):  # and name not in seeStock("nothalal"):
            self.halal_Box.setChecked(True)
            self.new_Ticker.hide()
            self.halal_Box.setEnabled(False)
            self.q_Area.setEnabled(True)
        elif not name in seeStock("halal"):
            self.halal_Box.setChecked(False)
            self.new_Ticker.hide()
            self.halal_Box.setEnabled(False)
            self.q_Area.setEnabled(False)
        if name not in seeStock("halal") and name not in seeStock("nothalal"):
            if name == "":
                pass
            else:
                self.halal_Box.setChecked(False)
                self.halal_Box.setEnabled(True)
                self.new_Ticker.show()

    def disable_Halal(self):
        if self.halal_Box.isChecked(): self.q_Area.setEnabled(True)
        else: self.q_Area.setEnabled(False)


    def checkTicker(self):
        new = False
        name = self.ticker_Input.text().upper()
        if name.lower() == "exit":
            self.ticker_Input.setText("")
            self.goHome()
        if name in seeStock("halal"):  # and name not in seeStock("nothalal"):
            self.halal_Box.setChecked(True)
            self.new_Ticker.hide()
            self.halal_Box.setEnabled(False)
        elif not name in seeStock("halal"):
            self.halal_Box.setChecked(False)
            self.new_Ticker.hide()
            self.halal_Box.setEnabled(False)
        if name not in seeStock("halal") and name not in seeStock("nothalal"):
            if name == "":
                pass

            else:
                self.halal_Box.setChecked(False)
                self.halal_Box.setEnabled(True)
                self.new_Ticker.show()
                new = True

        if self.halal_Box.isChecked(): self.q_Area.setEnabled(True)
        else: self.q_Area.setEnabled(False);                               #; self.q_Area.setToolTip("Stock is NOT Halal, unable to proceed, check Zoya, edit 'tickers.json' if necessary...")

            # new = True

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
    def reset(self):
        #self.submit_Button.setText("Submited!")

        self.Ticker_Box.setEnabled(True)
        self.ticker_Input.setEnabled(True)
        self.ticker_Input.setText("")
        self.halal_Box.setEnabled(False)
        self.halal_Box.setChecked(False)
        self.submit_Button.setEnabled(False)
        self.SCORE.display(0)
        self.q_Area.setEnabled(False)
        self.new_Ticker.hide()
        self.another_Button.hide()
        self.home_Button.hide()





    def score(self):
        score = 0
        self.q_Area.setEnabled(False)
        #self.Ticker_Box.setEnabled(False)
        # self._SPC.isEnabled
        #t200
        if self.twoHundred == True: score+= t200["gWeight"]; self.indicators.append("Is above the 200!")
        elif self.twoHundred == False: score+= t200["bWeight"]; self.indicators.append("Is UNDER the 200!")
        if self.twoHundred_spc == True and self.twohundred_SPC.isHidden(): score += t200["gsp"]; self.indicators.append("Is about to cross above the 200!")
        elif self.twoHundred_spc == False and self.twohundred_SPC.isHidden(): score += t200["bsp"]; self.indicators.append("Is about to cross UNDER the 200!")
        #t9
        if self.nine == True: score+= t9["gWeight"]; self.indicators.append("Is above the 9!")
        elif self.nine == False: score+= t9["bWeight"]; self.indicators.append("Is under the 9!")
        if self.nine_spc == True and self.nine_SPC.isHidden(): score += t9["gsp"]; self.indicators.append("Is one candle close above the 9!")
        elif self.nine_spc == False and self.nine_SPC.isHidden(): score += t9["bsp"]; self.indicators.append("Is one candle close UNDER the 9! (sell)")
        #MACD
        if self.MACD == True: score+= MACD["gWeight"]; self.indicators.append("MACD Is above the the red (line) or is in the green (bar)!")
        elif self.MACD == False: score+= MACD["bWeight"]; self.indicators.append("MACD Is UNDER the red (line) or is in the red (bar)!")
        if self.MACD_spc == True and self.MACD_SPC.isHidden(): score += MACD["gsp"]; self.indicators.append("MACD Is reverseing to green or crossing above the red!")
        elif self.MACD_spc == False and self.MACD_SPC.isHidden(): score += MACD["bsp"]; self.indicators.append("MACD Is reversing to red or crossing under the red!")
        #RSI
        if self.RSI == True: score+= RSI["gWeight"]; self.indicators.append("RSI is low!")
        elif self.RSI == False: score+= RSI["bWeight"]; self.indicators.append("RSI is high!")
        if self.RSI_spc == True and self.RSI_SPC.isHidden(): score += RSI["gsp"]; self.indicators.append("RSI is overbought!")
        elif self.RSI_spc == False and self.RSI_SPC.isHidden(): score += RSI["bsp"]; self.indicators.append("RSI is oversold!")
        #VWAP
        if self.VWAP == True: score+= VWAP["gWeight"]; self.indicators.append("We have GoGo Juise!")
        elif self.VWAP == False: score+= VWAP["bWeight"]; self.indicators.append("No gogo juise! :(")
        # if self.VWAP_spc == True and self.VWAP_SPC.isHidden(): score += VWAP["gsp"]
        # elif self.VWAP_spc == False and self.VWAP_SPC.isHidden(): score += VWAP["bsp"]
        #HA
        if self.HA == True: score+= HA["gWeight"]; self.indicators.append("Heiken Ashi is trending UP!")
        elif self.HA == False: score+= HA["bWeight"]; self.indicators.append("Heiken Ashi is trending DOWN!")
        # if self.HA_spc == True and self.HA_SPC.isHidden(): score += HA["gsp"]
        # elif self.HA_spc == False and self.HA_SPC.isHidden(): score += HA["bsp"]
        #SHAC
        if self.SHAC == True: score+= SHAC["gWeight"]; self.indicators.append("Smoothed Heiken Ashi Candles are trending UP!")
        elif self.SHAC == False: score+= SHAC["bWeight"]; self.indicators.append("Smoothed Heiken Ashi Candles are trending DOWN!")
        # if self.SHAC_spc == True and self.SHAC_SPC.isHidden(): score += SHAC["gsp"]
        # elif self.SHAC_spc == False and self.SHAC_SPC.isHidden(): score += SHAC["bsp"]
        #RIB
        if self.RIB == True: score+= RIB["gWeight"]; self.indicators.append("Is above the Ribbons!")
        elif self.RIB == False: score+= RIB["bWeight"]; self.indicators.append("Is BELOW the Ribbons!")
        # if self.RIB_spc == True and self.RIB_SPC.isHidden(): score += RIB["gsp"]
        # elif self.RIB_spc == False and self.RIB_SPC.isHidden(): score += RIB["bsp"]
        #VPVR
        if self.VPVR == True: score+= VPVR["gWeight"]; self.indicators.append("VPVR looks good!")
        elif self.VPVR == False: score+= VPVR["bWeight"]; self.indicators.append("VPVR looks bad!")
        if self.VPVR_spc == True and self.VPVR_SPC.isHidden(): score += VPVR["gsp"]; self.indicators.append("VPVR is about to jump UP!")
        elif self.VPVR_spc == False and self.VPVR_SPC.isHidden(): score += VPVR["bsp"]; self.indicators.append("VPVR is about to jump DOWN!")
        #LUX
        if self.LUX == True: score+= LUX["gWeight"]; self.indicators.append("LUX looks good!")
        elif self.LUX == False: score+= LUX["bWeight"]; self.indicators.append("LUX looks bad!")
        if self.LUX_spc == True and self.LUX_SPC.isHidden(): score += LUX["gsp"]; self.indicators.append("Is near or in the buy cloud!")
        elif self.LUX_spc == False and self.LUX_SPC.isHidden(): score += LUX["bsp"]; self.indicators.append("Is near or in the sell cloud!")
        score = round(score, 2)
        self.SCORE.display(score)
        indicators = self.indicators
        pack = [score, indicators]
        name = self.ticker_Input.text()

        stuffy = pack

        # TODO0
        # enable saving
        timestamp = time("time")
        if not testMode:
            save({"ticker": name, "time": timestamp, "packet": [timestamp, stuffy]}, "save_data.json")



        self.another_Button.show()
        self.home_Button.show()
        self.submit_Button.setEnabled(False)
        self.ticker_Input.setEnabled(False)


        #return pack

    #t200
    def twohundred_is_True(self):
        self.twoHundred = True
    def twohundred_is_False(self):
        self.twoHundred = False
    def twohundred_check_True(self):
        pass
    def twohundred_check_False(self):
        pass
    def twohundred_spc_True(self):
        self.twoHundred_spc = True
    def twohundred_spc_False(self):
        self.twoHundred_spc = False
    #t9
    def nine_is_True(self):
        self.nine = True
    def nine_is_False(self):
        self.nine = False
    def nine_check_True(self):
        pass
    def nine_check_False(self):
        pass
    def nine_spc_True(self):
        self.nine_spc = True
    def nine_spc_False(self):
        self.nine_spc = False
    #MACD
    def MACD_is_True(self):
        self.MACD = True
    def MACD_is_False(self):
        self.MACD = False
    def MACD_check_True(self):
        pass
    def MACD_check_False(self):
        pass
    def MACD_spc_True(self):
        self.MACD_spc = True
    def MACD_spc_False(self):
        self.MACD_spc = False
    #RSI
    def RSI_is_True(self):
        self.RSI = True
    def RSI_is_False(self):
        self.RSI = False
    def RSI_check_True(self):
        pass
    def RSI_check_False(self):
        pass
    def RSI_spc_True(self):
        self.RSI_spc = True
    def RSI_spc_False(self):
        self.RSI_spc = False
    #VWAP
    def VWAP_is_True(self):
        self.VWAP = True
    def VWAP_is_False(self):
        self.VWAP = False
    def VWAP_check_True(self):
        pass
    def VWAP_check_False(self):
        pass
    def VWAP_spc_True(self):
        self.VWAP_spc = True
    def VWAP_spc_False(self):
        self.VWAP_spc = False
    #HA
    def HA_is_True(self):
        self.HA = True
    def HA_is_False(self):
        self.HA = False
    def HA_check_True(self):
        pass
    def HA_check_False(self):
        pass
    def HA_spc_True(self):
        self.HA_spc = True
    def HA_spc_False(self):
        self.HA_spc = False
    #SHAC
    def SHAC_is_True(self):
        self.SHAC = True
    def SHAC_is_False(self):
        self.SHAC = False
    def SHAC_check_True(self):
        pass
    def SHAC_check_False(self):
        pass
    def SHAC_spc_True(self):
        self.SHAC_spc = True
    def SHAC_spc_False(self):
        self.SHAC_spc = False
    #RIB
    def RIB_is_True(self):
        self.RIB = True
    def RIB_is_False(self):
        self.RIB = False
    def RIB_check_True(self):
        pass
    def RIB_check_False(self):
        pass
    def RIB_spc_True(self):
        self.RIB_spc = True
    def RIB_spc_False(self):
        self.RIB_spc = False
    #VPVR
    def VPVR_is_True(self):
        self.VPVR = True
    def VPVR_is_False(self):
        self.VPVR = False
    def VPVR_check_True(self):
        pass
    def VPVR_check_False(self):
        pass
    def VPVR_spc_True(self):
        self.VPVR_spc = True
    def VPVR_spc_False(self):
        self.VPVR_spc = False
    #LUX
    def LUX_is_True(self):
        self.LUX = True
        self.submit_Button.setEnabled(True)
    def LUX_is_False(self):
        self.LUX = False
        self.submit_Button.setEnabled(True)
    def LUX_check_True(self):
        pass
    def LUX_check_False(self):
        pass
    def LUX_spc_True(self):
        self.LUX_spc = True
        self.submit_Button.setEnabled(True)
    def LUX_spc_False(self):
        self.LUX_spc = False
        self.submit_Button.setEnabled(True)

def error(error):
    """
    #TODO | OUTDATED USE LOGGING INSTEAD

    prints and saves errors
    :param error:
    :return:
    """
    print(error)
    with open('errors.json') as e:
        thetime = time("time")
        thedate = time("date")
        data = json.load(e)
        temp = data["logs"]
        new_data = {thedate: [{"timestamp": thetime, "error": error}]}
        temp.append(new_data)
        write_json(data, "errors.json")

def time(dateortime):
    from datetime import date
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    today = date.today()
    date = today.strftime("%d/%m/%Y")
    time = dt_string
    try:
        if dateortime == "date":
            return date
        elif dateortime == "time":
            return time
    except:
        error("Error not an option, try again.")

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def save(datas, filename):
    thetime = time("time")
    thedate = time("date")
    # with open('save_data.txt', 'a') as file:
    #     file.write(f"{date}\n")
    # file.write({"date" : date, "ticker" : "TSLA"})

    with open(filename) as file:
        # file.write(json.dumps({date : [{"ticker" : "TSLA", "indicator" : VPVR}]}, indent=2))
        # stand it data btw will pass in from func
        data = json.load(file)
        temp = data["logs"]
        # new_data = {thedate : [{"timestamp": thetime, "packet": [{"ticker": "TSLA", "indicator": VPVR}]}]}
        # new_data = {thedate: [{"timestamp": thetime, "packet": datas}]}
        temp.append(datas)
        write_json(data, filename)

def load(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        # print(data["logs"][0][date][0]["dat"][0]["#data here"])
        stuff = data["logs"]
        return data

def seeStock(halalornothalal):
    """
    :param halalornothalal:
    :return list of either all the halal stocks or all the non-halal stocks:
    """
    stuff = load("tickers.json")
    halal = []
    nothalal = []
    for i in stuff["logs"]:
        things = i["ticker"]
        if i["halal"] == True:
            halal.append(things)
        elif i["halal"] == False:
            nothalal.append(things)
    if halalornothalal in yes:
        return halal
    elif halalornothalal in no:
        return nothalal
    else:
        error("Error: Check parameters.")

def halalCheck(ticker):
    """
    :param ticker:
    :return "halal" if the ticker is halal and "nothalal" if it isent, or "new" if its new:
    """
    stuff = load("tickers.json")
    halal = []
    nothalal = []
    for i in stuff["logs"]:
        things = i["ticker"]
        if i["halal"] == True:
            halal.append(things)
        elif i["halal"] == False:
            nothalal.append(things)

    if ticker in halal:
        return "halal"
    elif ticker in nothalal:
        return "nothalal"
    else: return "new"


class halalChic(QDialog):
    def __init__(self):
        super(halalChic, self).__init__()
        uic.loadUi("halalCheck.ui", self)

        self.lotso_Input.hide()
        self.lotso_Box.clicked.connect(self.lotsoCheck)
        self.ticker_Input.returnPressed.connect(self.process)
        self.submit_Button.clicked.connect(self.process)
        self.submit_Ticker_Button.clicked.connect(self.process_New)
        self.home_Button.clicked.connect(self.goHome)

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def lotsoCheck(self):
        if self.lotso_Box.isChecked(): self.lotso_Input.show()
        else: self.lotso_Input.hide(); self.lotso_Input.setText("")

    def process(self):
        halal_Stocks = []
        non_halal_Stocks = []
        new_Stocks = []

        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)

        if not self.ticker_Input.text() == "" and self.lotso_Input.toPlainText() == "":
            tickers = self.ticker_Input.text().upper()
        elif not self.ticker_Input.text() == "" and not self.lotso_Input.toPlainText() == "":
            tickers = self.ticker_Input.text().upper() + ',' + self.lotso_Input.toPlainText().upper()
        else: tickers = self.lotso_Input.toPlainText().upper()
        tickers = tickers.replace(' ', '')
        tickers = tickers.split(",")

        for i in tickers:
            if i in seeStock("halal"): halal_Stocks.append(i)
            if i in seeStock("nothalal"): non_halal_Stocks.append(i)
            if i not in seeStock("halal") and i not in seeStock("nothalal"): new_Stocks.append(i)

        # Adding tickers. . .
        label = QLabel("Halal Tickers:")
        label.setFont(QFont("Arial", 16))
        self.verticalLayout_3.addWidget(label)

        for i in halal_Stocks:
            label = QLabel(i)
            self.verticalLayout_3.addWidget(label)

        label = QLabel("Non-Halal Tickers:")
        label.setFont(QFont("Arial", 16))
        self.verticalLayout_3.addWidget(label)

        for i in non_halal_Stocks:
            label = QLabel(i)
            self.verticalLayout_3.addWidget(label)

        label = QLabel("New Tickers:")
        label.setFont(QFont("Arial", 16))
        self.verticalLayout_3.addWidget(label)

        self.new_Ticker_Boxes = []

        for i in new_Stocks:
            g = QGroupBox()
            l = QHBoxLayout()
            g.setTitle('')
            t = QLabel(i)
            c = QCheckBox()
            c.setText("Halal")
            l.addWidget(t)
            l.addWidget(c)
            g.setLayout(l)
            self.new_Ticker_Boxes.append((t, c))
            self.verticalLayout_3.addWidget(g)


    def process_New(self):
        """
        saves the new tickers
        :return:
        """
        for i in self.new_Ticker_Boxes:
            if i[1].isChecked():
                if not testMode:
                    save({"ticker": i[0].text().upper(), "halal": True}, "tickers.json")
            elif not i[1].isChecked():
                if not testMode:
                    save({"ticker": i[0].text().upper(), "halal": False}, "tickers.json")

        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)

class seeHalal(QDialog):
    def __init__(self):
        super(seeHalal, self).__init__()
        uic.loadUi("seeHalal.ui", self)

        self.home_Button.clicked.connect(self.goHome)

        for i in seeStock("halal"):
            l = QLabel(i)
            self.verticalLayout_2.addWidget(l)

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 3)


class seeNotHalal(QDialog):
    def __init__(self):
        super(seeNotHalal, self).__init__()
        uic.loadUi("seeNotHalal.ui", self)

        self.home_Button.clicked.connect(self.goHome)

        for i in seeStock("nothalal"):
            l = QLabel(i)
            self.verticalLayout_3.addWidget(l)

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 4)

class seeHistory(QDialog):
    def __init__(self):
        super(seeHistory, self).__init__()
        uic.loadUi("seeHistory.ui", self)

        self.home_Button.clicked.connect(self.goHome)

        blocks = []
        """
        Note todo:
        in blocks use the push buttons as keys and the stuff in history["logs"] as values
        ahh, have fun. .. 
        """

        history = load("save_data.json")
        for block in history["logs"]:
            p = QPushButton(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]}')
            p.setFlat(True)
            #p.clicked.connect(lambda: self.viewBlock(i))
            self.connectBlock(p, block)
            blocks.append((p,block))
            self.verticalLayout_2.addWidget(p)

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 5)

    def connectBlock(self, button, block):
        button.clicked.connect(lambda: self.viewBlock(block))

    def viewBlock(self, block):
        l = QLabel(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]} and was:')
        self.verticalLayout_3.addWidget(l)
        for i in block["packet"][1][1]:
            l = QLabel(i)
            self.verticalLayout_3.addWidget(l)
        h = QFrame(self)
        h.setFrameShape(QtWidgets.QFrame.HLine)
        h.setFrameShadow(QtWidgets.QFrame.Sunken)
        h.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addWidget(h)

class seeTickerHistory(QDialog):
    def __init__(self):
        super(seeTickerHistory, self).__init__()
        uic.loadUi("seeTickerHistory.ui", self)

        self.history = load("save_data.json")

        self.home_Button.clicked.connect(self.goHome)
        self.ticker_Input.textEdited.connect(lambda: self.getTicker(self.ticker_Input.text().upper()))
        self.ticker_Input.returnPressed.connect(lambda: self.getTicker(self.ticker_Input.text().upper()))

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 6)

    def getTicker(self, ticker):
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)

        if ticker in seeStock("halal"):
            self.lock(lock=False)
            for block in self.history["logs"]:
                if block["ticker"] == ticker:
                    p = QPushButton(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]}')
                    p.setFlat(True)
                    #p.clicked.connect(lambda: self.viewBlock(block))
                    self.connectBlock(p,block)
                    # blocks.append((p, block))
                    self.verticalLayout_2.addWidget(p)
        else:
            self.lock(lock=True)

    def connectBlock(self, button, block):
        #TODO
        # make it so when a button is clicked it cant be clicked again until another button is clicked (to prevent duplicates)
        button.clicked.connect(lambda: self.viewBlock(block))

    def viewBlock(self, block):
        l = QLabel(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]} and was:')
        self.verticalLayout_3.addWidget(l)
        for i in block["packet"][1][1]:
            l = QLabel(i)
            self.verticalLayout_3.addWidget(l)
        h = QFrame(self)
        h.setFrameShape(QtWidgets.QFrame.HLine)
        h.setFrameShadow(QtWidgets.QFrame.Sunken)
        h.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addWidget(h)

    def lock(self, lock=True):
        self.scrollArea.setDisabled(lock)
        self.line.setDisabled(lock)
        #self.scrollArea_2.setDisabled(lock)

class seeYesterday(QDialog):
    def __init__(self):
        super(seeYesterday, self).__init__()
        uic.loadUi("seeYesterday.ui", self)

        from datetime import date, timedelta
        todays = date.today()
        yesterday = todays - timedelta(days=1)  # FIX FORMAT
        yesterday = yesterday.strftime('%d/%m/%Y')

        self.home_Button.clicked.connect(self.goHome)

        history = load("save_data.json")
        for block in history["logs"]:
            stRing = block["time"]
            dateChar = stRing[0: 10]
            if yesterday == dateChar:
                p = QPushButton(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]}')
                p.setFlat(True)
                #p.clicked.connect(lambda: self.viewBlock(i))
                self.connectBlock(p, block)
                #blocks.append((p,block))
                self.verticalLayout_2.addWidget(p)

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 7)

    def connectBlock(self, button, block):
        button.clicked.connect(lambda: self.viewBlock(block))

    def viewBlock(self, block):
        l = QLabel(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]} and was:')
        self.verticalLayout_3.addWidget(l)
        for i in block["packet"][1][1]:
            l = QLabel(i)
            self.verticalLayout_3.addWidget(l)
        h = QFrame(self)
        h.setFrameShape(QtWidgets.QFrame.HLine)
        h.setFrameShadow(QtWidgets.QFrame.Sunken)
        h.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addWidget(h)

class seeToday(QDialog):
    def __init__(self):
        super(seeToday, self).__init__()
        uic.loadUi("seeToday.ui", self)

        theday = time("date")

        self.home_Button.clicked.connect(self.goHome)

        history = load("save_data.json")
        for block in history["logs"]:
            stRing = block["time"]
            dateChar = stRing[0: 10]
            if theday == dateChar:
                p = QPushButton(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]}')
                p.setFlat(True)
                #p.clicked.connect(lambda: self.viewBlock(i))
                self.connectBlock(p, block)
                #blocks.append((p,block))
                self.verticalLayout_2.addWidget(p)


    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 8)

    def connectBlock(self, button, block):
        button.clicked.connect(lambda: self.viewBlock(block))

    def viewBlock(self, block):
        l = QLabel(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]} and was:')
        self.verticalLayout_3.addWidget(l)
        for i in block["packet"][1][1]:
            l = QLabel(i)
            self.verticalLayout_3.addWidget(l)
        h = QFrame(self)
        h.setFrameShape(QtWidgets.QFrame.HLine)
        h.setFrameShadow(QtWidgets.QFrame.Sunken)
        h.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addWidget(h)


def main():
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()
    home = homeScreen()
    stock = stockCheck()
    halal = halalChic()
    seehalal = seeHalal()
    seenotHalal = seeNotHalal()
    history = seeHistory()
    seetickerhistory = seeTickerHistory()
    yesterday = seeYesterday()
    today = seeToday()
    widget.addWidget(home)
    widget.addWidget(stock)
    widget.addWidget(halal)
    widget.addWidget(seehalal)
    widget.addWidget(seenotHalal)
    widget.addWidget(history)
    widget.addWidget(seetickerhistory)
    widget.addWidget(yesterday)
    widget.addWidget(today)

    widget.show()
    app.exec_()



app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
home = homeScreen()
stock = stockCheck()
halal = halalChic()
seehalal = seeHalal()
seenotHalal = seeNotHalal()
history = seeHistory()
seetickerhistory = seeTickerHistory()
yesterday = seeYesterday()
today = seeToday()
widget.addWidget(home)
widget.addWidget(stock)
widget.addWidget(halal)
widget.addWidget(seehalal)
widget.addWidget(seenotHalal)
widget.addWidget(history)
widget.addWidget(seetickerhistory)
widget.addWidget(yesterday)
widget.addWidget(today)
widget.show()
app.exec_()


def on_clicked(msg):
    """
    What?? where did this come from?
    :param msg:
    :return:
    """
    print("Button Clicked!!!")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

# if __name__ == '__main__':
#     main()
