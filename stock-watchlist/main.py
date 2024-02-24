import csv
import json
import random
import sys
import time as t
from datetime import date
from datetime import datetime

import finviz
import requests
import timeago
from finviz.screener import Screener
from line_profiler_pycharm import profile

import tradingview_ta_kataki as ta

# Settings
# Testing

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
today = date.today()
date = today.strftime("%d/%m/%Y")
date_ago = today.strftime("%Y-%m-%d")
timestamp = dt_string
interval = ta.Interval.INTERVAL_4_HOURS
# interval = "4h"

with open('exchanges.json', 'r') as f:
    ticker_exchanges = json.load(f)
with open('tickers.json', 'r') as f:
    tickers_data = json.load(f)["logs"]
with open('exchanges.json', 'r') as f:
    exchange_pairs = json.load(f)
# Variables
num = random.randint(0, 10000)
num2 = str(num)
# import MyGUI as MyGUI
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QSettings, QCoreApplication

yes = ["yes", "yep", "yea", "y", "yup", "true", "t", "Yes", "Yep", "Yea", "Y", "Yup", True, "True", "T", "halal",
       "Halal", "a", "o", "A", "O", "above", "Above", "over", "Over", "g", "G", "up", "Up", "UP", "", " "]
no = ["no", "n", "false", "f", "nope", "No", "N", False, "False", "F", "Nope", "nothalal", "Nothalal", "notHalal",
      "NotHalal", "nah", "Nah", "u", "b", "U", "B", "under", "below", "Under", "Below", "down", "Down", "DOWN"]
# indicators
try:
    with open("settings.json", "r") as settingsFile:
        settingsLoaded = json.load(settingsFile)


        def getWeight(spinbox: str):
            for i in settingsLoaded["weights"]:
                try:
                    return i[spinbox]
                except KeyError:
                    pass
            raise Exception(f"EOF: Invalid SpinBox ({spinbox})")


        def getBox(checkbox: str):
            for i in settingsLoaded["boxes"]:
                try:
                    return i[checkbox]
                except KeyError:
                    pass
            raise Exception(f"EOF: Invalid CheckBox ({checkbox})")


        def get_line_edit(line_edit: str):
            for i in settingsLoaded["line_edits"]:
                try:
                    return i[line_edit]
                except KeyError:
                    pass
            raise Exception(f"EOF: Invalid Line Edit ({line_edit})")


        has_apikey = get_line_edit("APIKey_edit")

        t200 = {"name": "The 200!", "gWeight": getWeight("doubleSpinBox_57"), "bWeight": getWeight("doubleSpinBox_58"),
                "spc": "Is the 200 crossing up or down?", "gsp": getWeight("doubleSpinBox_59"),
                "bsp": getWeight("doubleSpinBox_60"), "notes": ""}
        t9 = {"name": "The 9!", "gWeight": getWeight("doubleSpinBox_53"), "bWeight": getWeight("doubleSpinBox_54"),
              "spc": "Is it One candle close above or below thw nine the 9? (Means get in or watch or get out if below)",
              "gsp": getWeight("doubleSpinBox_55"), "bsp": getWeight("doubleSpinBox_56"),
              "notes": "Prob close when under 9"}
        MACD = {"name": "MACD", "gWeight": getWeight("doubleSpinBox_45"), "bWeight": getWeight("doubleSpinBox_46"),
                "spc": "Is the MACD reversing up or down, is it crossing?",
                "gsp": getWeight("doubleSpinBox_47"), "bsp": getWeight("doubleSpinBox_48"), "notes": ""}
        RSI = {"name": "RSI", "gWeight": getWeight("doubleSpinBox_65"), "bWeight": getWeight("doubleSpinBox_66"),
               "spc": "Is the RSI  Oversold(good)(y) or Overbought(bad)(n)?", "gsp": getWeight("doubleSpinBox_67"),
               "bsp": getWeight("doubleSpinBox_68"), "notes": "over bought for selling only"}
        VWAP = {"name": "VWAP", "gWeight": getWeight("doubleSpinBox_73"), "bWeight": getWeight("doubleSpinBox_74"),
                "spc": "None/WIP", "gsp": getWeight("doubleSpinBox_75"), "bsp": getWeight("doubleSpinBox_76"),
                "notes": ""}
        HA = {"name": "Heiken Ashi", "gWeight": getWeight("doubleSpinBox_69"), "bWeight": getWeight("doubleSpinBox_70"),
              "spc": "None/WIP", "gsp": getWeight("doubleSpinBox_72"), "bsp": getWeight("doubleSpinBox_72"),
              "notes": ""}
        SHAC = {"name": "Smoothed Ha Candles", "gWeight": getWeight("doubleSpinBox_49"),
                "bWeight": getWeight("doubleSpinBox_50"), "spc": "None/WIP", "gsp": getWeight("doubleSpinBox_51"),
                "bsp": getWeight("doubleSpinBox_52"),
                "notes": ""}
        RIB = {"name": "Ribbons", "gWeight": getWeight("doubleSpinBox_61"), "bWeight": getWeight("doubleSpinBox_62"),
               "spc": "None/WIP", "gsp": getWeight("doubleSpinBox_63"), "bsp": getWeight("doubleSpinBox_64"),
               "notes": ""}
        VPVR = {"name": "VPVR", "gWeight": getWeight("doubleSpinBox_77"), "bWeight": getWeight("doubleSpinBox_78"),
                "spc": "Is it Jump Up/Jump Down?", "gsp": getWeight("doubleSpinBox_79"),
                "bsp": getWeight("doubleSpinBox_80"),
                "notes": "Good for crypto."}
        # t9 = {"name" : "The 9!", "gWeight" : 1.5, "bWeight" : -1.5, "spc" : "Is it One candle close above or below thw nine the 9? (Means get in or watch or get out if below)", "gsp" : 1.5, "bsp" : -1.5, "notes" : "Prob close when under 9"}
        others = ["Support", "Resistance", "Moveing Averages", "VBottoms (for entry) and etc...", "Wedges and etc...",
                  "Divergence (really bad)", "Earnings Call (bad)"]
        # LUX = "Is it neer a cloud?"
        LUX = {"name": "LUX", "gWeight": getWeight("doubleSpinBox"), "bWeight": getWeight("doubleSpinBox_2"),
               "spc": "Is it neer a cloud? Buy Cloud(y) Sell Cloud(n)",
               "gsp": getWeight("doubleSpinBox_3"), "bsp": getWeight("doubleSpinBox_4"),
               "notes": "Prob close when under 9"}
except Exception as e:
    print(e)
    settingsLoaded = {
        "boxes": [
            {"testMode_Box": False},
            {"autoFilter_Box": False},
            {"showFilter_Box": True},
            {"savespot_Box": False},
            {"clear_Box": False},
        ],
        "line_edits": [{"APIKey_edit": ""}],
        "currentFilter": 0,
        "filters": [
            {
                "Filter 1": [
                    "fa_salesqoq_o30",
                    "ind_stocksonly",
                    "ipodate_prev3yrs",
                    "sh_avgvol_o500",
                    "sh_short_o5",
                    "ta_changeopen_u",
                    "ta_sma20_pa",
                    "ta_sma200_pa",
                    "ta_sma50_pa",
                ]
            },
            {"Filter 2": ["cap_midover", "sh_curvol_o1000", "ta_sma20_pa10"]},
        ],
        "db_last_update": "2024-01-23",
        "weights": [
            {"doubleSpinBox_61": 1.0},
            {"doubleSpinBox_62": -1.0},
            {"doubleSpinBox_63": 0.0},
            {"doubleSpinBox_64": 0.0},
            {"doubleSpinBox_49": 1.0},
            {"doubleSpinBox_50": -1.0},
            {"doubleSpinBox_51": 0.0},
            {"doubleSpinBox_52": 0.0},
            {"doubleSpinBox_65": 1.0},
            {"doubleSpinBox_66": -1.0},
            {"doubleSpinBox_67": 1.5},
            {"doubleSpinBox_68": -1.0},
            {"doubleSpinBox_69": 1.0},
            {"doubleSpinBox_70": -1.0},
            {"doubleSpinBox_71": 0.0},
            {"doubleSpinBox_72": 0.0},
            {"doubleSpinBox_73": 1.5},
            {"doubleSpinBox_74": -1.5},
            {"doubleSpinBox_75": 0.0},
            {"doubleSpinBox_76": 0.0},
            {"doubleSpinBox_77": 1.5},
            {"doubleSpinBox_78": 0.0},
            {"doubleSpinBox_79": 2.0},
            {"doubleSpinBox_80": -2.0},
            {"doubleSpinBox": 1.0},
            {"doubleSpinBox_2": -1.0},
            {"doubleSpinBox_3": 1.5},
            {"doubleSpinBox_4": -1.5},
            {"doubleSpinBox_45": 1.5},
            {"doubleSpinBox_46": -1.5},
            {"doubleSpinBox_47": 1.5},
            {"doubleSpinBox_48": -1.5},
            {"doubleSpinBox_53": 1.5},
            {"doubleSpinBox_54": -1.5},
            {"doubleSpinBox_55": 1.5},
            {"doubleSpinBox_56": -1.5},
            {"doubleSpinBox_57": 2.0},
            {"doubleSpinBox_58": -2.0},
            {"doubleSpinBox_59": 1.0},
            {"doubleSpinBox_60": -1.5},
        ],
    }


    def getWeight(spinbox: str):
        for i in settingsLoaded["weights"]:
            try:
                return i[spinbox]
            except KeyError:
                pass
        raise Exception(f"EOF: Invalid SpinBox ({spinbox})")


    def getBox(checkbox: str):
        for i in settingsLoaded["boxes"]:
            try:
                return i[checkbox]
            except KeyError:
                pass
        raise Exception(f"EOF: Invalid CheckBox ({checkbox})")


    def get_line_edit(line_edit: str):
        for i in settingsLoaded["line_edits"]:
            try:
                return i[line_edit]
            except KeyError:
                pass
        raise Exception(f"EOF: Invalid Line Edit ({line_edit})")


    has_apikey = get_line_edit("APIKey_edit")

    t200 = {"name": "The 200!", "gWeight": 2, "bWeight": -2, "spc": "Is the 200 crossing up or down?", "gsp": 1,
            "bsp": -1.5, "notes": ""}
    t9 = {"name": "The 9!", "gWeight": 1.5, "bWeight": -1.5,
          "spc": "Is it One candle close above or below thw nine the 9? (Means get in or watch or get out if below)",
          "gsp": 1.5, "bsp": -1.5, "notes": "Prob close when under 9"}
    MACD = {"name": "MACD", "gWeight": 1.5, "bWeight": -1.5, "spc": "Is the MACD reversing up or down, is it crossing?",
            "gsp": 1.5, "bsp": -1.5, "notes": ""}
    RSI = {"name": "RSI", "gWeight": 1, "bWeight": -1, "spc": "Is the RSI  Oversold(good)(y) or Overbought(bad)(n)?",
           "gsp": 1.5,
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
    LUX = {"name": "LUX", "gWeight": 1, "bWeight": -1, "spc": "Is it neer a cloud? Buy Cloud(y) Sell Cloud(n)",
           "gsp": 1.5, "bsp": -1.5,
           "notes": "Prob close when under 9"}

# Form, Window = uic.loadUiType("Stock-Watchlist-Logger.ui")

exchanges = [
    "NYSE",  # New York Stock Exchange
    "NASDAQ",
    "TSE",  # Tokyo Stock Exchange
    "SSE",  # Shanghai Stock Exchange
    "HKEX",  # Hong Kong Stock Exchange
    "ENX",  # Euronext
    "LSE",  # London Stock Exchange
    "SZSE",  # Shenzhen Stock Exchange
    "TSX",  # Toronto Stock Exchange
    "BSE",  # Bombay Stock Exchange
    "NSE",  # National Stock Exchange of India
    "DB",  # Deutsche Börse
    "ASX",  # Australian Securities Exchange
    "KRX",  # Korea Exchange
    "SIX",  # SIX Swiss Exchange
    "TWSE",  # Taiwan Stock Exchange
    "MOEX",  # Moscow Exchange
    "BME",  # Madrid Stock Exchange
    "B3",  # BM&F Bovespa
    "JSE"  # Johannesburg Stock Exchange
]


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
        self.todaystock_Button.clicked.connect(self.goSeeTodayStock)
        self.settings_Button.clicked.connect(self.goSettings)

        QCoreApplication.instance().aboutToQuit.connect(self.saveSettings)

        # self.setWindowFlags(Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)) # dident work

        # print(self.settings_Button.objectName())

        # Zoya API Support

        if settingsLoaded["db_last_update"] != '':
            ago = timeago.format(settingsLoaded["db_last_update"], date_ago)

        if settingsLoaded["db_last_update"] == '':
            self.db_last_update_label.setText("Database last updated: Never")
            # print(timeago.format("2024-1-23", today.strftime("%Y-%m-%d")))


        elif not 'month' in ago and not 'year' in ago and not 'months' in ago and not 'years' in ago:
            self.db_last_update_label.setText(f"Database last updated: {ago}")
            self.db_last_update_label.setStyleSheet("color: green")
            # print(timeago.format(settingsLoaded["db_last_update"], today.strftime("%Y-%m-%d")))

        else:
            # print("long ago")
            self.db_last_update_label.setText(f"Database last updated: {ago}")

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

    def goSeeTodayStock(self):
        widget.setCurrentIndex(widget.currentIndex() + 9)

    def goSettings(self):
        widget.setCurrentIndex(widget.currentIndex() + 10)

    # def moveEvent(self, e):
    #     print(self.pos())
    #     print(self.rect().height(), self.rect().width())
    #     super(homeScreen, self).moveEvent(e)

    def saveSettings(self):
        # SETTINGS.setValue("halal", json.dumps(halal.getSavables()))
        # SETTINGS.setValue("stock", json.dumps(stockT.getSavables()))
        # SETTINGS.setValue("settings", json.dumps(settings.getSavables()))
        # SETTINGS.sync()
        pass


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

        # self.aboutToQuit.connect(home.saveSettings())

        # TODO
        # make compact ver with just one checkbox instead of two radio buttons

        # self.halal_Box.setChecked(True) # Example

        # Scoring

        # Vars
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

        self.submit_Button.clicked.connect(self.do_score)
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
        # LUX
        self.LUX_Is_True.clicked.connect(self.LUX_is_True)
        self.LUX_Is_False.clicked.connect(self.LUX_is_False)
        self.LUX_Check_True.clicked.connect(self.LUX_check_True)
        self.LUX_Check_False.clicked.connect(self.LUX_check_False)
        self.LUX_SPC_True.clicked.connect(self.LUX_spc_True)
        self.LUX_SPC_False.clicked.connect(self.LUX_spc_False)

        # self.show()

        # Grab ticker data from TradingView
        self.tv_ta_ticker_data()

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
            # Stock is halal so do some analysis
            self.auto_check_ticker(name)
        elif name not in seeStock("halal"):
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
        elif name not in seeStock("halal"):
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

    def tv_ta_ticker_data(self):
        data_return = {}
        for ticker in tickers_data:
            exchange_found = True
            if ticker["halal"]:
                if not check_in(ticker["ticker"]):
                    exchange_found = False
                    for exchange in exchanges:
                        try:
                            tesla = ta.TA_Handler(
                                symbol=ticker["ticker"],
                                screener='america',
                                exchange=exchange,
                                interval=interval
                            )
                            # If analysis is successful, check if the exchange is in the existing list
                            if tesla.get_analysis().indicators:
                                exchange_pair = {ticker["ticker"]: exchange}
                                if exchange_pair not in ticker_exchanges:
                                    ticker_exchanges.append(exchange_pair)
                                    exchange_found = True
                                    print(f"Added {ticker['ticker']} to exchanges.json with exchange {exchange}")
                                break
                        except Exception as e:
                            pass

                    if not exchange_found:
                        print(f"No exchange found for {ticker['ticker']}")

                else:
                    try:
                        result = ta.TA_Handler(
                            symbol=ticker["ticker"],
                            screener='america',
                            exchange=get_exchange(ticker["ticker"]),
                            interval=interval
                        )
                        data_return[ticker["ticker"]] = result
                    except Exception:
                        print(f'Invalid Exchange: {ticker["ticker"]}')

        # Write updated ticker-exchange pairs to the exchanges.json file
        with open('exchanges.json', 'w') as f:
            json.dump(ticker_exchanges, f)

        self.data_result = data_return

    def auto_check_ticker(self, ticker):
        analysis = self.data_result[ticker]
        indicators = analysis.get_indicators()

        t200_line = indicators["SMA200"]
        t9_line = indicators["SMA9"]
        macd_line = indicators["MACD.macd"]
        macd_signal = indicators["MACD.signal"]
        rsi_line = indicators["RSI"]
        rsi_line_past1 = indicators["RSI[1]"]
        vwap_line = indicators["VWAP"]
        open = indicators["open"]
        close = indicators["close"]
        larger = (open if open > close else close)
        smaller = (close if close < open else open)
        candle_height = larger - smaller
        candle_avg = smaller + (candle_height / 2)
        percent_tolorance = 0.05
        dot_tolorance = 0.3
        normal_price_threshold = 50
        high_price_threshold = 70
        low_price_threshold = 30
        is_above = lambda price, line: True if price >= line else False
        is_below = lambda price, line: True if price <= line else False
        is_within_5_percent = lambda price, line: abs(line - price) / line <= percent_tolorance
        is_within_dot3 = lambda line1, line2: abs(line1 - line2) <= dot_tolorance
        is_contains = lambda price_larger, price_smaller, line: price_larger > line and price_smaller < line

        # t200 abouve or below
        # t200 is above
        self.twohundred_Is_True.setChecked(True if ((open >= t200_line) & (close >= t200_line)) or
                                                   is_above(candle_avg, t200_line) else False)
        # t200 is below
        if not self.twohundred_Is_True.isChecked():
            self.twohundred_Is_False.setChecked(True if ((open <= t200_line) & (close <= t200_line)) or
                                                        is_below(candle_avg, t200_line) else False)
        # t200 is crossing
        self.twohundred_Check_True.setChecked(is_within_5_percent(candle_avg, t200_line))
        if not self.twohundred_Check_True.isChecked():
            self.twohundred_Check_False.setChecked(False if is_within_5_percent(candle_avg, t200_line) else True)

        # t200 is crossing up / down
        if self.twohundred_Check_True.isChecked():
            self.twohundred_SPC_True.setChecked(is_below(candle_avg, t200_line) and is_above(candle_avg, t9_line))
            if not self.twohundred_SPC_True.isChecked():
                self.twohundred_SPC_False.setChecked(is_above(candle_avg, t200_line) and is_below(candle_avg, t9_line))

        # t9 above or below
        # t200 is above
        self.nine_Is_True.setChecked(True if ((open >= t9_line) & (close >= t9_line)) or
                                             is_above(candle_avg, t9_line) else False)
        # t29 is below
        if not self.nine_Is_True.isChecked():
            self.nine_Is_False.setChecked(True if ((open <= t9_line) & (close <= t9_line)) or
                                                  is_below(candle_avg, t9_line) else False)

        # t9 one candle close
        if not smaller >= t9_line + candle_height or not larger >= t9_line - candle_height:
            self.nine_Check_True.setChecked(True)
            self.nine_SPC_True.setChecked(is_above(smaller, t9_line))
            self.nine_SPC_False.setChecked(is_below(larger, t9_line))

        else:
            self.nine_Check_False.setChecked(True)

        # macd
        if macd_line > macd_signal:
            self.MACD_Is_True.setChecked(True)
        else:
            self.MACD_Is_False.setChecked(True)

        # macd reversing
        self.MACD_Check_True.setChecked(is_within_dot3(macd_line, macd_signal))
        if not self.MACD_Check_True.isChecked():
            self.MACD_Check_False.setChecked(False if is_within_dot3(macd_line, macd_signal) else True)

        # macd reverse up / down
        if self.MACD_Check_True.isChecked():
            self.MACD_SPC_True.setChecked(is_below(macd_line, macd_signal) and self.nine_Is_True.isChecked())
            if not self.MACD_SPC_True.isChecked():
                self.MACD_SPC_False.setChecked(is_above(macd_line, macd_signal) and not self.nine_Is_True.isChecked())

        # RSI low / high
        self.RSI_Is_True.setChecked(is_below(rsi_line, normal_price_threshold))
        if not self.RSI_Is_True.isChecked():
            self.RSI_Is_False.setChecked(is_above(rsi_line, normal_price_threshold))

        # rsi overbought / oversold
        self.RSI_Check_True.setChecked(
            is_below(rsi_line, low_price_threshold) or is_above(rsi_line, high_price_threshold))
        if not self.RSI_Check_True.isChecked():
            self.RSI_Check_False.setChecked(
                False if is_below(rsi_line, low_price_threshold) or is_above(rsi_line, high_price_threshold) else True)

        if self.RSI_Check_True.isChecked():
            self.RSI_SPC_True.setChecked(is_below(rsi_line, low_price_threshold))
            if not self.RSI_SPC_True.isChecked():
                self.RSI_SPC_False.setChecked(is_above(rsi_line, high_price_threshold))

        # VWAP
        self.VWAP_Is_True.setChecked(is_above(vwap_line, t9_line))
        if not self.VWAP_Is_True.isChecked():
            self.VWAP_Is_False.setChecked(is_below(vwap_line, t9_line))


    def score(self):
        score = 0
        self.indicators = []
        self.q_Area.setEnabled(False)
        # self.Ticker_Box.setEnabled(False)
        # self._SPC.isEnabled
        # TODO make it so that is a chekbox is not true or false than it doent apply and isent counted
        # t200
        if self.twoHundred == True:
            score += t200["gWeight"];
            self.indicators.append("Is above the 200!")
        elif self.twoHundred == False:
            score += t200["bWeight"];
            self.indicators.append("Is UNDER the 200!")
        if self.twoHundred_spc == True and not self.twohundred_SPC.isHidden():
            score += t200["gsp"];
            self.indicators.append("Is about to cross above the 200!")
        elif self.twoHundred_spc == False and not self.twohundred_SPC.isHidden():
            score += t200["bsp"];
            self.indicators.append("Is about to cross UNDER the 200!")
        # t9
        if self.nine == True:
            score += t9["gWeight"];
            self.indicators.append("Is above the 9!")
        elif self.nine == False:
            score += t9["bWeight"];
            self.indicators.append("Is under the 9!")
        if self.nine_spc == True and not self.nine_SPC.isHidden():
            score += t9["gsp"];
            self.indicators.append("Is one candle close above the 9!")
        elif self.nine_spc == False and not self.nine_SPC.isHidden():
            score += t9["bsp"];
            self.indicators.append("Is one candle close UNDER the 9! (sell)")
        # MACD
        if self.MACD == True:
            score += MACD["gWeight"];
            self.indicators.append(
                "MACD Is above the the red (line) or is in the green (bar)!")
        elif self.MACD == False:
            score += MACD["bWeight"];
            self.indicators.append("MACD Is UNDER the red (line) or is in the red (bar)!")
        if self.MACD_spc == True and not self.MACD_SPC.isHidden():
            score += MACD["gsp"];
            self.indicators.append("MACD Is reverseing to green or crossing above the red!")
        elif self.MACD_spc == False and not self.MACD_SPC.isHidden():
            score += MACD["bsp"];
            self.indicators.append("MACD Is reversing to red or crossing under the red!")
        # RSI
        if self.RSI == True:
            score += RSI["gWeight"];
            self.indicators.append("RSI is low!")
        elif self.RSI == False:
            score += RSI["bWeight"];
            self.indicators.append("RSI is high!")
        if self.RSI_spc == True and not self.RSI_SPC.isHidden():
            score += RSI["gsp"];
            self.indicators.append("RSI is overbought!")
        elif self.RSI_spc == False and not self.RSI_SPC.isHidden():
            score += RSI["bsp"];
            self.indicators.append("RSI is oversold!")
        # VWAP
        if self.VWAP == True:
            score += VWAP["gWeight"];
            self.indicators.append("We have GoGo Juise!")
        elif self.VWAP == False:
            score += VWAP["bWeight"];
            self.indicators.append("No gogo juise! :(")
        # if self.VWAP_spc == True and self.VWAP_SPC.isHidden(): score += VWAP["gsp"]
        # elif self.VWAP_spc == False and self.VWAP_SPC.isHidden(): score += VWAP["bsp"]
        # HA
        if self.HA == True:
            score += HA["gWeight"];
            self.indicators.append("Heiken Ashi is trending UP!")
        elif self.HA == False:
            score += HA["bWeight"];
            self.indicators.append("Heiken Ashi is trending DOWN!")
        # if self.HA_spc == True and self.HA_SPC.isHidden(): score += HA["gsp"]
        # elif self.HA_spc == False and self.HA_SPC.isHidden(): score += HA["bsp"]
        # SHAC
        if self.SHAC == True:
            score += SHAC["gWeight"]; self.indicators.append("Smoothed Heiken Ashi Candles are trending UP!")
        elif self.SHAC == False:
            score += SHAC["bWeight"]; self.indicators.append("Smoothed Heiken Ashi Candles are trending DOWN!")
        # if self.SHAC_spc == True and self.SHAC_SPC.isHidden(): score += SHAC["gsp"]
        # elif self.SHAC_spc == False and self.SHAC_SPC.isHidden(): score += SHAC["bsp"]
        # RIB
        if self.RIB == True:
            score += RIB["gWeight"];
            self.indicators.append("Is above the Ribbons!")
        elif self.RIB == False:
            score += RIB["bWeight"];
            self.indicators.append("Is BELOW the Ribbons!")
        # if self.RIB_spc == True and self.RIB_SPC.isHidden(): score += RIB["gsp"]
        # elif self.RIB_spc == False and self.RIB_SPC.isHidden(): score += RIB["bsp"]
        # VPVR
        if self.VPVR == True:
            score += VPVR["gWeight"];
            self.indicators.append("VPVR looks good!")
        elif self.VPVR == False:
            score += VPVR["bWeight"];
            self.indicators.append("VPVR looks bad!")
        if self.VPVR_spc == True and not self.VPVR_SPC.isHidden():
            score += VPVR["gsp"];
            self.indicators.append("VPVR is about to jump UP!")
        elif self.VPVR_spc == False and not self.VPVR_SPC.isHidden():
            score += VPVR["bsp"];
            self.indicators.append("VPVR is about to jump DOWN!")
        # LUX
        if self.LUX == True:
            score += LUX["gWeight"];
            self.indicators.append("LUX looks good!")
        elif self.LUX == False:
            score += LUX["bWeight"];
            self.indicators.append("LUX looks bad!")
        if self.LUX_spc == True and not self.LUX_SPC.isHidden():
            score += LUX["gsp"];
            self.indicators.append("Is near or in the buy cloud!")
        elif self.LUX_spc == False and not self.LUX_SPC.isHidden():
            score += LUX["bsp"];
            self.indicators.append("Is near or in the sell cloud!")
        score = round(score, 2)
        self.SCORE.display(score)
        indicators = self.indicators
        stuffy = pack = [score, indicators]
        name = self.ticker_Input.text()

        # stuffy = pack

        # TODO0
        # enable saving
        timestamp = time("time")
        if not testMode:
            return {"ticker": name.upper(), "time": timestamp, "packet": [timestamp, stuffy]}, "save_data.json"

        # TODO
        # make search only need a fe leters ex searching 't' with still bring up 'TSLA' (Ticker History) DONE!

        # return pack

    def do_score(self):
        score = self.score()
        if not testMode:
            save(score[0], score[1])
            self.another_Button.show()
            self.home_Button.show()
            self.submit_Button.setEnabled(False)
            self.ticker_Input.setEnabled(False)

    # t200
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

    # TODO
    # add notes at end


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
    if not testMode:
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
    else:
        return "new"


def convert_csv_to_json(input_file, output_file):
    input_data = []

    with open(input_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header line

        for row in reader:
            if len(row) == 3:  # Assuming three columns: Name, Symbol, and Status
                transformed_entry = {
                    "ticker": row[1].strip(),  # Assuming Symbol is the second column
                    "halal": row[2].strip() == "Pass"  # Assuming Compliance Status is the third column
                }
                input_data.append(transformed_entry)

    with open(output_file, 'w') as jsonfile:
        json.dump(input_data, jsonfile, indent=4)


def merge_json(old_file, new_file, output_file):
    # Load data from the old JSON file
    with open(old_file, 'r') as old_json:
        old_data = json.load(old_json)

    # Load data from the new JSON file
    with open(new_file, 'r') as new_json:
        new_data = json.load(new_json)

    # Update existing data and add missing data
    for new_entry in new_data:
        ticker = new_entry["ticker"]
        for old_entry in old_data["logs"]:
            if old_entry["ticker"] == ticker:
                # Update existing halal status if ticker exists in old data
                if old_entry["halal"] != new_entry["halal"]:
                    error(
                        f"{ticker}'s halal status has changed to {new_entry['halal']}! It used to be {old_entry['halal']}.")
                old_entry["halal"] = new_entry["halal"]
                break
        else:
            # Add missing ticker data from the new file to the old data
            old_data["logs"].append(new_entry)
            error(f"Added {new_entry['ticker']} to DB. It is {'halal' if new_entry['halal'] else 'not halal'}.")

    # Write the merged data to a new JSON file
    with open(output_file, 'w') as merged_json:
        json.dump(old_data, merged_json, indent=4)


def check_in(ticker):
    for i in exchange_pairs:
        try:
            i[ticker]
            return True
        except KeyError:
            pass
    return False


def get_exchange(ticker):
    for i in exchange_pairs:
        try:
            return i[ticker]
        except KeyError:
            pass
    return False


def UpdateLocalDB_api(api_key: str):
    sandbox_url = "https://sandbox-api.zoya.finance/graphql"
    sandbox_apikey = "sandbox-82dbe157-5d4e-47a8-b16b-c5b5d9fc17aa"
    zoya_url = "https://sandbox-api.zoya.finance/graphql"

    headers = {"Authorization": api_key, "Content-Type": "application/json"}
    query = """
    query ListCompliantStocks {
      basicCompliance {
        reports(input: {
          filters: { status: COMPLIANT }
        }) {
          items {
            symbol
            status
          }
          nextToken
        }
      }
    }
    """

    # Prepare the request payload
    payload = {"query": query}

    # Send the GraphQL request
    response = requests.post(zoya_url, headers=headers, json=payload)
    # print(response.json())

    new_data = {
        "logs": [
            {"ticker": item["symbol"], "halal": item["status"] == "COMPLIANT"} for item in
            response.json()["data"]["basicCompliance"]["reports"]["items"]
        ]
    }

    if not testMode:
        with open('new_data.json', 'w') as new_data_file:
            json.dump(new_data, new_data_file, indent=4)

        merge_json('tickers.json', 'new_data.json', 'new_data.json')


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
        self.savables = {"fields": [self.ticker_Input.text(), self.lotso_Input.toPlainText()], "halal": []}

        default_json = '{"fields": ["' + self.ticker_Input.text() + '", "' + self.lotso_Input.toPlainText() + '"], "halal": []}'
        self.savedables = json.loads(SETTINGS.value("halal", defaultValue=default_json))
        fields = self.savedables["fields"]
        # self.ticker_Input.setText("replace with qsettings") if fields[0] else None
        # self.lotso_Input.setText("replace with qsettings") if fields[1] else None; self.lotso_Box.setChecked(True) if fields[1] else None; self.lotso_Box.stateChanged.emit(self.lotso_Box.isChecked()) if fields[1] else None

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 2)

    def lotsoCheck(self):
        if self.lotso_Box.isChecked():
            self.lotso_Input.show()
        else:
            self.lotso_Input.hide()
            if getBox("clear_Box"):
                self.lotso_Input.setText(
                    "")  # todoDONE mapke this a setting "clear lots o tickers imput when unchecked

    def process(self):
        halal_Stocks = []
        non_halal_Stocks = []
        new_Stocks = []

        try:
            for i in reversed(range(self.verticalLayout_3.count())):
                self.verticalLayout_3.itemAt(i).widget().setParent(None)
        except AttributeError:
            print('Error deleting somthing: Empty layout (not important)')

        if not self.ticker_Input.text() == "" and self.lotso_Input.toPlainText() == "":
            tickers = self.ticker_Input.text().upper()
        elif not self.ticker_Input.text() == "" and not self.lotso_Input.toPlainText() == "":
            tickers = self.ticker_Input.text().upper() + ',' + self.lotso_Input.toPlainText().upper()
        else:
            tickers = self.lotso_Input.toPlainText().upper()
        tickers = tickers.replace(' ', '')
        tickers = tickers.split(",")

        for i in tickers:
            if i == "": continue  # TODO: save everything in new tickers and save the checkstates and add them to the new tickers on next open (should use q settings) do same for simmilar pages
            if i in seeStock("halal"): halal_Stocks.append(i)
            if i in seeStock("nothalal"): non_halal_Stocks.append(i)
            if i not in seeStock("halal") and i not in seeStock("nothalal"): new_Stocks.append(i)

        # Adding tickers. . .
        label = QLabel("Halal Tickers:")
        label.setFont(QFont("Arial", 16))
        self.verticalLayout_3.addWidget(label)

        for i in halal_Stocks:
            label = QLabel(i)
            label.setStyleSheet('color: green')
            self.verticalLayout_3.addWidget(label)

        label = QLabel("Non-Halal Tickers:")
        label.setFont(QFont("Arial", 16))
        self.verticalLayout_3.addWidget(label)

        for i in non_halal_Stocks:
            label = QLabel(i)
            label.setStyleSheet('color: red')
            self.verticalLayout_3.addWidget(label)

        label = QLabel("New Tickers:")
        label.setFont(QFont("Arial", 16))
        self.verticalLayout_3.addWidget(label)

        self.new_Ticker_Boxes = []

        if new_Stocks:
            for i in new_Stocks:
                g = QGroupBox()
                l = QHBoxLayout()
                g.setTitle('')
                t = QLabel(i)
                c = QCheckBox()
                c.setText("Halal")
                s = t, c;
                self.savables["halal"].append(s)
                l.addWidget(t)
                l.addWidget(c)
                g.setLayout(l)
                self.new_Ticker_Boxes.append((t, c))
                self.verticalLayout_3.addWidget(g)
        if self.savedables["halal"]:
            for i in self.savedables["halal"]:
                if not i[0] in new_Stocks:
                    g = QGroupBox()
                    l = QHBoxLayout()
                    g.setTitle('')
                    t = QLabel(i[0])
                    c = i[1]
                    c.setText("Halal")
                    s = t, c;
                    self.savables["halal"].append(s)
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
        self.savables["halal"], self.savedables["halal"] = [], []  #FIXME this might not work
        for i in self.new_Ticker_Boxes:
            if i[1].isChecked():
                if not testMode:
                    save({"ticker": i[0].text().upper(), "halal": True}, "tickers.json")
            elif not i[1].isChecked():
                if not testMode:
                    save({"ticker": i[0].text().upper(), "halal": False}, "tickers.json")

        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)

        self.process()

    def getSavables(self):
        return self.savables
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

        if (e := [i for i in seeStock("halal") if i.startswith(ticker)]):
            self.lock(lock=False)
            for block in self.history["logs"]:
                if block["ticker"] in e:
                    p = QPushButton(f'On {block["time"]} {block["ticker"]} had a score of {block["packet"][1][0]}')
                    p.setFlat(True)
                    # p.clicked.connect(lambda: self.viewBlock(block))
                    self.connectBlock(p, block)
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
        self.bottom()

        # self.scrollArea_2.verticalScrollBar().setValue(self.scrollArea_2.verticalScrollBar().maximum())
        # self.scrollArea_2.ensureVisible(0, self.scrollArea_2.verticalScrollBar().maximum())
        # content_widget = self.scrollArea_2.findChild(QWidget, "scrollAreaWidgetContents_2")
        # self.scrollArea_2.verticalScrollBar().setValue(content_widget.height())
        # self.scrollArea_2.ensureVisible(0, content_widget.height() + 200)
        # scroll_area = self.scrollArea_2
        # scroll_bar = scroll_area.verticalScrollBar()
        # scroll_bar.setValue(scroll_bar.maximum())
        scroll_area = self.scrollArea_2
        content_widget = self.scrollAreaWidgetContents_2
        content_widget_height = content_widget.height()
        scroll_area_height = scroll_area.viewport().height()
        scroll_area.ensureVisible(0, content_widget_height - scroll_area_height + 240, 0, 0)

    def lock(self, lock=True):
        self.scrollArea.setDisabled(lock)
        self.line.setDisabled(lock)
        # self.scrollArea_2.setDisabled(lock)

    def bottom(self):
        scroll_area = self.scrollArea_2
        content_widget = self.scrollAreaWidgetContents_2
        content_widget_height = content_widget.height()
        scroll_area_height = scroll_area.viewport().height()
        scroll_area.ensureVisible(0, content_widget_height - scroll_area_height + 240, 0, 0)


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


class todayStock(QDialog):
    def __init__(self):
        super(todayStock, self).__init__()
        uic.loadUi("TodaysStock.ui", self)

        self.prevent429 = 1.5  # how long to sleep for to avoid making too many requests to the api in a short time # TODO maybe make this a setting
        # self.filters.hide() if "QSETTINGS" else None

        self.filterCount = 1

        self.savables = {"halal": [], "filters": {
            "Default": ['fa_salesqoq_o30', 'ind_stocksonly', 'ipodate_prev3yrs', 'sh_avgvol_o500', 'sh_short_o5',
                        'ta_changeopen_u', 'ta_sma20_pa', 'ta_sma200_pa', 'ta_sma50_pa']}}  # TODO make filters editable
        # self.savedables = json.loads(SETTINGS.value("stock", defaultValue=json.dumps({"halal": [], "filters": {"Default": ['fa_salesqoq_o30', 'ind_stocksonly', 'ipodate_prev3yrs', 'sh_avgvol_o500', 'sh_short_o5',
        #            'ta_changeopen_u', 'ta_sma20_pa', 'ta_sma200_pa', 'ta_sma50_pa']}})))

        self.submit_Ticker_Button.clicked.connect(self.process_New)
        self.home_Button.clicked.connect(self.goHome)
        self.filters.currentIndexChanged.connect(self.process)

        self.filters.hide()

        try:
            self.current_filter_index = settingsLoaded["currentFilter"]
            current_filter = settingsLoaded["filters"][self.current_filter_index]
        except IndexError:
            self.current_filter_index = 0
            error(f"Warning: Missing filter index {settingsLoaded['currentFilter']}")
            current_filter = settingsLoaded["filters"][self.current_filter_index]

        self.filters.clear()  # Gets rid of the "Default" filter option

        for i in settingsLoaded["filters"]:
            self.filters.addItem(list(i.keys())[0], list(i.values())[0])

        self.filters.setCurrentIndex(self.current_filter_index)
        self.process()

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 9)

    def changeFilter(self, current_filter_index):
        self.filters.setCurrentIndex(current_filter_index)

    def get_Stock(self, filters):
        # stock_list1, stock_list2, stock_list3 = Screener(filters=filters, table='Performance',
        #                                                  order='price'), Screener(filters=filters,
        #                                                                           table='Performance'), []
        # this was not uses because it assigned variables too fast an made too many requests Too Many Requests for url: https://finviz.com/screener.ashx?

        stock_list1 = Screener(filters=filters, table='Performance', order='price')
        t.sleep(self.prevent429)
        stock_list2 = Screener(filters=filters, table='Performance')
        stock_list3 = []

        for stock in stock_list1:
            stock_list3.append(stock['Ticker'])
        for stock in stock_list2:
            if stock['Ticker'] not in stock_list3:
                stock_list3.append(stock['Ticker'])
        # for stock in stock_list3:
        #     print(stock)
        return stock_list3

    def process(self):
        halal_Stocks = []
        non_halal_Stocks = []
        new_Stocks = []

        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)

        filters = ['fa_salesqoq_o30', 'ind_stocksonly', 'ipodate_prev3yrs', 'sh_avgvol_o500', 'sh_short_o5',
                   'ta_changeopen_u', 'ta_sma20_pa', 'ta_sma200_pa',
                   'ta_sma50_pa']  # , 'ta_volatility_mo15' to test the except statement
        filters2 = ['cap_midover', 'sh_curvol_o1000', 'ta_sma20_pa10']

        current_filter_index = self.filters.currentIndex()
        current_filter = settingsLoaded["filters"][current_filter_index]

        try:
            self.submit_Ticker_Button.setEnabled(True)
            tickers = self.get_Stock(self.filters.currentData())

            for i in tickers:
                if i in seeStock("halal"): halal_Stocks.append(i)
                if i in seeStock("nothalal"): non_halal_Stocks.append(i)
                if i not in seeStock("halal") and i not in seeStock("nothalal"): new_Stocks.append(i)

            # Adding tickers. . .
            label = QLabel(
                "Halal Tickers:                                                                        ")  # buffer to fit anya
            label.setFont(QFont("Arial", 16))
            self.verticalLayout_3.addWidget(label)

            for i in halal_Stocks:
                label = QLabel(i)
                label.setStyleSheet('color: green')
                self.verticalLayout_3.addWidget(label)

            label = QLabel("Non-Halal Tickers:")
            label.setFont(QFont("Arial", 16))
            self.verticalLayout_3.addWidget(label)

            for i in non_halal_Stocks:
                label = QLabel(i)
                label.setStyleSheet('color: red')
                self.verticalLayout_3.addWidget(label)

            label = QLabel("New Tickers:")
            label.setFont(QFont("Arial", 16))
            self.verticalLayout_3.addWidget(label)

            self.new_Ticker_Boxes = []

            if new_Stocks:
                for i in new_Stocks:
                    g = QGroupBox()
                    l = QHBoxLayout()
                    g.setTitle('')
                    t = QLabel(i)
                    c = QCheckBox()
                    c.setText("Halal")
                    s = t.text(), c.isChecked()
                    self.savables["halal"].append(s)
                    l.addWidget(t)
                    l.addWidget(c)
                    g.setLayout(l)
                    self.new_Ticker_Boxes.append((t, c))
                    self.verticalLayout_3.addWidget(g)
            # if self.savedables["halal"]:
            #     for i in self.savedables["halal"]:
            #         if not i[0] in new_Stocks:
            #             g = QGroupBox()
            #             l = QHBoxLayout()
            #             g.setTitle('')
            #             t = QLabel(i[0])
            #             c = i[1]
            #             c.setText("Halal")
            #             s = t.text(), c.isChecked()
            #             self.savables["halal"].append(s)
            #             l.addWidget(t)
            #             l.addWidget(c)
            #             g.setLayout(l)
            #             self.new_Ticker_Boxes.append((t, c))self.savedables = dict(json.loads(SETTINGS.value("halal", defaultValue=json.dumps('{"fields": [self.ticker_Input.text(), self.lotso_Input.toPlainText()], "halal": []}'))))
            # ValueError: dictionary update sequence element #0 has length 1; 2 is required
            #             self.verticalLayout_3.addWidget(g)
        except (finviz.helper_functions.error_handling.NoResults,
                IndexError) as e:  # Replace with idex error if needed in testing, seems to be ide's fault
            # print(e.__traceback__.__str__())
            if getBox("autoFilter_Box"):
                if self.filterCount == 1:
                    self.filters.setCurrentIndex(0)
                if (x := self.filterCount) <= (y := self.filters.count()):
                    f = self.filterCount - 1
                    self.filters.setCurrentIndex(f)
                    self.filterCount += 1
                    self.process()
            if getBox("showFilter_Box"):
                self.filters.show()
            self.submit_Ticker_Button.setEnabled(False)
            label = QLabel(
                """Sorry,\nNo New Tickers Today\n
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠂⢉⠤⠐⠋⠈⠡⡈⠉⠐⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⢠⣤⠔⠁⢀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠀⠀⠈⠱⡤⣤⠄⣀⠀⠀⠀⠀⠀
⠀⠀⠰⠁⠀⣰⣿⠃⠀⢠⠃⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⢞⣦⡀⠈⡇⠀⠀⠀
⠀⠀⠀⢇⣠⡿⠁⠀⢀⡃⠀⣈⠀⠀⠀⠀⢰⡀⠀⠀⠀⠀⢢⠰⠀⠀⢺⣧⢰⠀⠀⠀⠀
⠀⠀⠀⠈⣿⠁⡘⠀⡌⡇⠀⡿⠸⠀⠀⠀⠈⡕⡄⠀⠐⡀⠈⠀⢃⠀⠀⠾⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠇⡇⠃⢠⠀⠶⡀⡇⢃⠡⡀⠀⠀⠡⠈⢂⡀⢁⠀⡁⠸⠀⡆⠘⡀⠀⠀⠀⠀
⠀⠀⠀⠸⠀⢸⠀⠘⡜⠀⣑⢴⣀⠑⠯⡂⠄⣀⣣⢀⣈⢺⡜⢣⠀⡆⡇⠀⢣⠀⠀⠀⠀
⠀⠀⠀⠇⠀⢸⠀⡗⣰⡿⡻⠿⡳⡅⠀⠀⠀⠀⠈⡵⠿⠿⡻⣷⡡⡇⡇⠀⢸⣇⠀⠀⠀
⠀⠀⢰⠀⠀⡆⡄⣧⡏⠸⢠⢲⢸⠁⠀⠀⠀⠀⠐⢙⢰⠂⢡⠘⣇⡇⠃⠀⠀⢹⡄⠀⠀
⠀⠀⠟⠀⠀⢰⢁⡇⠇⠰⣀⢁⡜⠀⠀⠀⠀⠀⠀⠘⣀⣁⠌⠀⠃⠰⠀⠀⠀⠈⠰⠀⠀
⠀⡘⠀⠀⠀⠀⢊⣤⠀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠄⠀⢸⠃⠀⠀⠀⠀⠀⠃⠀
⢠⠁⢀⠀⠀⠀⠈⢿⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⢀⠏⠀⠀⠀⠀⠀⠀⠸⠀
⠘⠸⠘⡀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠁⠀⠃⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⢠⠀⠀⡇
⠀⠇⢆⢃⠀⠀⠀⠀⠀⡏⢲⢤⢀⡀⠀⠀⠀⠀⠀⢀⣠⠄⡚⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀
⢰⠈⢌⢎⢆⠀⠀⠀⠀⠁⣌⠆⡰⡁⠉⠉⠀⠉⠁⡱⡘⡼⠇⠀⠀⠀⠀⢀⢬⠃⢠⠀⡆
⠀⢢⠀⠑⢵⣧⡀⠀⠀⡿⠳⠂⠉⠀⠀⠀⠀⠀⠀⠀⠁⢺⡀⠀⠀⢀⢠⣮⠃⢀⠆⡰⠀
⠀⠀⠑⠄⣀⠙⡭⠢⢀⡀⠀⠁⠄⣀⣀⠀⢀⣀⣀⣀⡠⠂⢃⡀⠔⠱⡞⢁⠄⣁⠔⠁⠀
⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀


PRO-TIP: You can use different filters/
or get Tickers from Bravo or Finviz!
____________
|HOVER HERE|
¯¯¯¯¯¯¯¯¯¯¯¯""")
            label.setFont(QFont("Arial", 16))
            label.setStyleSheet('color: rgb(244, 184, 243)')
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setToolTip(str(self.filters.currentData()))
            self.verticalLayout_3.addWidget(label)

    def process_New(self):
        """
        saves the new tickers
        :return:
        """
        # self.savables["halal"], self.savedables["halal"] = [], []  # FIXME this might not work
        for i in self.new_Ticker_Boxes:
            if i[1].isChecked():
                if not testMode:
                    save({"ticker": i[0].text().upper(), "halal": True}, "tickers.json")
            elif not i[1].isChecked():
                if not testMode:
                    save({"ticker": i[0].text().upper(), "halal": False}, "tickers.json")

        for i in reversed(range(self.verticalLayout_3.count())):
            self.verticalLayout_3.itemAt(i).widget().setParent(None)

        self.process()

    def getSavables(self):
        return self.savables

    def saveSettings(self):
        # SETTINGS.setValue("stock", json.dumps(self.savables))
        pass


class Settings(QDialog):  # TODO make sure new filters match format with regex
    def __init__(self):
        super(Settings, self).__init__()
        uic.loadUi("Settings.ui", self)

        self.scrollArea.hide()
        # self.autoFilter_Box.clicked.connect(lambda: self.showFilter_Box.setChecked(True) if "qSettings" else False)

        self.home_Button.clicked.connect(self.goHome)
        # self.filterBox.addItems(i for i in stockT.getSavables()["filters"].keys())
        # self.filterBox.currentIndexChanged.connect(self.changeFilter)
        self.saveButton.clicked.connect(self.saveSettings)
        self.UpdateLocalDB_button.clicked.connect(self.UpdateLocalDB_csv)
        self.APIKey_edit_button.clicked.connect(self.enableAPIedit)
        self.logs_Button.clicked.connect(self.viewLogs)

        self.db_updated_today = False

        self.getSavables()

        # self.savedables = json.loads(SETTINGS.value("settings", defaultValue=json.dumps({
        #     "boxes": [{self.testMode_Box.objectName(): self.testMode_Box.isChecked()} , {self.autoFilter_Box.objectName(): self.autoFilter_Box.isChecked()} , {self.showFilter_Box.objectName(): self.showFilter_Box.isChecked()} , {self.savespot_Box.objectName(): self.savespot_Box.isChecked()} , {self.clear_Box.objectName(): self.clear_Box.isChecked()} ],
        #     "currentFilter": "",
        #     "weights": [{self.doubleSpinBox_61.objectName(): self.doubleSpinBox_61.value()} , {self.doubleSpinBox_62.objectName(): self.doubleSpinBox_62.value()} , {self.doubleSpinBox_63.objectName(): self.doubleSpinBox_63.value()} , {self.doubleSpinBox_64.objectName(): self.doubleSpinBox_64.value()} , #FIXME fix these names theyre horrendous
        #                 {self.doubleSpinBox_49.objectName(): self.doubleSpinBox_49.value()} , {self.doubleSpinBox_50.objectName(): self.doubleSpinBox_50.value()} , {self.doubleSpinBox_51.objectName(): self.doubleSpinBox_51.value()} , {self.doubleSpinBox_52.objectName(): self.doubleSpinBox_52.value()} ,
        #                 {self.doubleSpinBox_65.objectName(): self.doubleSpinBox_65.value()} , {self.doubleSpinBox_66.objectName(): self.doubleSpinBox_66.value()} , {self.doubleSpinBox_67.objectName(): self.doubleSpinBox_67.value()} , {self.doubleSpinBox_68.objectName(): self.doubleSpinBox_68.value()} ,
        #                 {self.doubleSpinBox_69.objectName(): self.doubleSpinBox_69.value()} , {self.doubleSpinBox_70.objectName(): self.doubleSpinBox_70.value()} , {self.doubleSpinBox_71.objectName(): self.doubleSpinBox_71.value()} , {self.doubleSpinBox_72.objectName(): self.doubleSpinBox_72.value()} ,
        #                 {self.doubleSpinBox_73.objectName(): self.doubleSpinBox_73.value()} , {self.doubleSpinBox_74.objectName(): self.doubleSpinBox_74.value()} , {self.doubleSpinBox_75.objectName(): self.doubleSpinBox_75.value()} , {self.doubleSpinBox_76.objectName(): self.doubleSpinBox_76.value()} ,
        #                 {self.doubleSpinBox_77.objectName(): self.doubleSpinBox_77.value()} , {self.doubleSpinBox_78.objectName(): self.doubleSpinBox_78.value()} , {self.doubleSpinBox_78.objectName(): self.doubleSpinBox_78.value()} , {self.doubleSpinBox_80.objectName(): self.doubleSpinBox_80.value()} ,
        #                 {self.doubleSpinBox.objectName(): self.doubleSpinBox.value()} , {self.doubleSpinBox_2.objectName(): self.doubleSpinBox_2.value()} , {self.doubleSpinBox_3.objectName(): self.doubleSpinBox_3.value()} , {self.doubleSpinBox_4.objectName(): self.doubleSpinBox_4.value()} ,
        #                 {self.doubleSpinBox_45.objectName(): self.doubleSpinBox_45.value()} , {self.doubleSpinBox_46.objectName(): self.doubleSpinBox_46.value()} , {self.doubleSpinBox_47.objectName(): self.doubleSpinBox_47.value()} , {self.doubleSpinBox_48.objectName(): self.doubleSpinBox_48.value()} ,
        #                 {self.doubleSpinBox_53.objectName(): self.doubleSpinBox_53.value()} , {self.doubleSpinBox_54.objectName(): self.doubleSpinBox_54.value()} , {self.doubleSpinBox_55.objectName(): self.doubleSpinBox_55.value()} , {self.doubleSpinBox_56.objectName(): self.doubleSpinBox_56.value()} ,
        #                 {self.doubleSpinBox_57.objectName(): self.doubleSpinBox_57.value()} , {self.doubleSpinBox_58.objectName(): self.doubleSpinBox_58.value()} , {self.doubleSpinBox_59.objectName(): self.doubleSpinBox_59.value()} , {self.doubleSpinBox_60.objectName(): self.doubleSpinBox_60.value()}
        #                 ]
        # })))
        self.loadSettings()

        if self.APIKey_edit.text() != '':
            self.APIKey_edit.setEnabled(False)

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 10)

    def viewLogs(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def enableAPIedit(self):
        self.APIKey_edit.setEnabled(True)

    def getSavables(self):
        self.savables = {
            "boxes": [{self.testMode_Box.objectName(): self.testMode_Box.isChecked()},
                      {self.autoFilter_Box.objectName(): self.autoFilter_Box.isChecked()},
                      {self.showFilter_Box.objectName(): self.showFilter_Box.isChecked()},
                      {self.savespot_Box.objectName(): self.savespot_Box.isChecked()},
                      {self.clear_Box.objectName(): self.clear_Box.isChecked()}],
            "line_edits": [{self.APIKey_edit.objectName(): self.APIKey_edit.text()}],
            "currentFilter": self.filterBox.currentIndex(),
            "filters": settingsLoaded["filters"],
            "db_last_update": '',
            "weights": [{self.doubleSpinBox_61.objectName(): self.doubleSpinBox_61.value()},
                        {self.doubleSpinBox_62.objectName(): self.doubleSpinBox_62.value()},
                        {self.doubleSpinBox_63.objectName(): self.doubleSpinBox_63.value()},
                        {self.doubleSpinBox_64.objectName(): self.doubleSpinBox_64.value()},
                        # FIXME fix these names theyre horrendous
                        {self.doubleSpinBox_49.objectName(): self.doubleSpinBox_49.value()},
                        {self.doubleSpinBox_50.objectName(): self.doubleSpinBox_50.value()},
                        {self.doubleSpinBox_51.objectName(): self.doubleSpinBox_51.value()},
                        {self.doubleSpinBox_52.objectName(): self.doubleSpinBox_52.value()},
                        {self.doubleSpinBox_65.objectName(): self.doubleSpinBox_65.value()},
                        {self.doubleSpinBox_66.objectName(): self.doubleSpinBox_66.value()},
                        {self.doubleSpinBox_67.objectName(): self.doubleSpinBox_67.value()},
                        {self.doubleSpinBox_68.objectName(): self.doubleSpinBox_68.value()},
                        {self.doubleSpinBox_69.objectName(): self.doubleSpinBox_69.value()},
                        {self.doubleSpinBox_70.objectName(): self.doubleSpinBox_70.value()},
                        {self.doubleSpinBox_71.objectName(): self.doubleSpinBox_71.value()},
                        {self.doubleSpinBox_72.objectName(): self.doubleSpinBox_72.value()},
                        {self.doubleSpinBox_73.objectName(): self.doubleSpinBox_73.value()},
                        {self.doubleSpinBox_74.objectName(): self.doubleSpinBox_74.value()},
                        {self.doubleSpinBox_75.objectName(): self.doubleSpinBox_75.value()},
                        {self.doubleSpinBox_76.objectName(): self.doubleSpinBox_76.value()},
                        {self.doubleSpinBox_77.objectName(): self.doubleSpinBox_77.value()},
                        {self.doubleSpinBox_78.objectName(): self.doubleSpinBox_78.value()},
                        {self.doubleSpinBox_79.objectName(): self.doubleSpinBox_79.value()},
                        {self.doubleSpinBox_80.objectName(): self.doubleSpinBox_80.value()},
                        {self.doubleSpinBox.objectName(): self.doubleSpinBox.value()},
                        {self.doubleSpinBox_2.objectName(): self.doubleSpinBox_2.value()},
                        {self.doubleSpinBox_3.objectName(): self.doubleSpinBox_3.value()},
                        {self.doubleSpinBox_4.objectName(): self.doubleSpinBox_4.value()},
                        {self.doubleSpinBox_45.objectName(): self.doubleSpinBox_45.value()},
                        {self.doubleSpinBox_46.objectName(): self.doubleSpinBox_46.value()},
                        {self.doubleSpinBox_47.objectName(): self.doubleSpinBox_47.value()},
                        {self.doubleSpinBox_48.objectName(): self.doubleSpinBox_48.value()},
                        {self.doubleSpinBox_53.objectName(): self.doubleSpinBox_53.value()},
                        {self.doubleSpinBox_54.objectName(): self.doubleSpinBox_54.value()},
                        {self.doubleSpinBox_55.objectName(): self.doubleSpinBox_55.value()},
                        {self.doubleSpinBox_56.objectName(): self.doubleSpinBox_56.value()},
                        {self.doubleSpinBox_57.objectName(): self.doubleSpinBox_57.value()},
                        {self.doubleSpinBox_58.objectName(): self.doubleSpinBox_58.value()},
                        {self.doubleSpinBox_59.objectName(): self.doubleSpinBox_59.value()},
                        {self.doubleSpinBox_60.objectName(): self.doubleSpinBox_60.value()}
                        ]
        }

        if self.filterName.text() and self.filter_new_edit.toPlainText():
            self.savables["filters"].append({self.filterName.text(): self.filter_new_edit.toPlainText()})

        if settingsLoaded["db_last_update"] != '':
            self.savables["db_last_update"] = settingsLoaded["db_last_update"]

        if self.db_updated_today:
            self.savables["db_last_update"] = date_ago
            self.db_updated_today = False

        return self.savables

    def getSavedables(self):
        # return self.savedables
        pass

    # def changeFilter(self, index):
    #     # self.savables["currentFilter"] = {index: stockSettings["filters"][index]} if index != -1 else None
    #     self.saveSettings()

    def changeFilter(self, current_filter_index):
        self.filterBox.setCurrentIndex(current_filter_index)

    # TODO func to add new filter to stockT qSettings

    def saveSettings(self):
        self.getSavables()
        with open("settings.json", "w") as settingsFile:
            json.dump(self.savables, settingsFile)

    def loadSettings(self):
        # Boxes
        self.testMode_Box.setChecked(getBox(self.testMode_Box.objectName()))
        self.autoFilter_Box.setChecked(getBox(self.autoFilter_Box.objectName()))
        self.showFilter_Box.setChecked(getBox(self.showFilter_Box.objectName()))
        self.savespot_Box.setChecked(getBox(self.savespot_Box.objectName()))
        self.clear_Box.setChecked(getBox(self.clear_Box.objectName()))

        # Line Edits

        self.APIKey_edit.setText(get_line_edit(self.APIKey_edit.objectName()))

        # Filters

        try:
            current_filter_index = settingsLoaded["currentFilter"]
            current_filter = settingsLoaded["filters"][current_filter_index]
        except IndexError:
            current_filter_index = 0
            error(f"Warning: Missing filter index {settingsLoaded['currentFilter']}")
            current_filter = settingsLoaded["filters"][current_filter_index]

        self.filterBox.clear()  # Gets rid of the "Default" filter option

        for i in settingsLoaded["filters"]:
            self.filterBox.addItem(list(i.keys())[0], list(i.values())[0])

        self.filterBox.setCurrentIndex(current_filter_index)

        # Spin Boxes
        self.doubleSpinBox_61.setValue(float(getWeight(self.doubleSpinBox_61.objectName())))
        self.doubleSpinBox_62.setValue(float(getWeight(self.doubleSpinBox_62.objectName())))
        self.doubleSpinBox_63.setValue(float(getWeight(self.doubleSpinBox_63.objectName())))
        self.doubleSpinBox_64.setValue(float(getWeight(self.doubleSpinBox_64.objectName())))
        self.doubleSpinBox_49.setValue(float(getWeight(self.doubleSpinBox_49.objectName())))
        self.doubleSpinBox_50.setValue(float(getWeight(self.doubleSpinBox_50.objectName())))
        self.doubleSpinBox_51.setValue(float(getWeight(self.doubleSpinBox_51.objectName())))
        self.doubleSpinBox_52.setValue(float(getWeight(self.doubleSpinBox_52.objectName())))
        self.doubleSpinBox_65.setValue(float(getWeight(self.doubleSpinBox_65.objectName())))
        self.doubleSpinBox_66.setValue(float(getWeight(self.doubleSpinBox_66.objectName())))
        self.doubleSpinBox_67.setValue(float(getWeight(self.doubleSpinBox_67.objectName())))
        self.doubleSpinBox_68.setValue(float(getWeight(self.doubleSpinBox_68.objectName())))
        self.doubleSpinBox_69.setValue(float(getWeight(self.doubleSpinBox_69.objectName())))
        self.doubleSpinBox_70.setValue(float(getWeight(self.doubleSpinBox_70.objectName())))
        self.doubleSpinBox_71.setValue(float(getWeight(self.doubleSpinBox_71.objectName())))
        self.doubleSpinBox_72.setValue(float(getWeight(self.doubleSpinBox_72.objectName())))
        self.doubleSpinBox_73.setValue(float(getWeight(self.doubleSpinBox_73.objectName())))
        self.doubleSpinBox_74.setValue(float(getWeight(self.doubleSpinBox_74.objectName())))
        self.doubleSpinBox_75.setValue(float(getWeight(self.doubleSpinBox_75.objectName())))
        self.doubleSpinBox_76.setValue(float(getWeight(self.doubleSpinBox_76.objectName())))
        self.doubleSpinBox_77.setValue(float(getWeight(self.doubleSpinBox_77.objectName())))
        self.doubleSpinBox_78.setValue(float(getWeight(self.doubleSpinBox_78.objectName())))
        self.doubleSpinBox_79.setValue(float(getWeight(self.doubleSpinBox_79.objectName())))
        self.doubleSpinBox_80.setValue(float(getWeight(self.doubleSpinBox_80.objectName())))
        self.doubleSpinBox.setValue(float(getWeight(self.doubleSpinBox.objectName())))
        self.doubleSpinBox_2.setValue(float(getWeight(self.doubleSpinBox_2.objectName())))
        self.doubleSpinBox_3.setValue(float(getWeight(self.doubleSpinBox_3.objectName())))
        self.doubleSpinBox_4.setValue(float(getWeight(self.doubleSpinBox_4.objectName())))
        self.doubleSpinBox_45.setValue(float(getWeight(self.doubleSpinBox_45.objectName())))
        self.doubleSpinBox_46.setValue(float(getWeight(self.doubleSpinBox_46.objectName())))
        self.doubleSpinBox_47.setValue(float(getWeight(self.doubleSpinBox_47.objectName())))
        self.doubleSpinBox_48.setValue(float(getWeight(self.doubleSpinBox_48.objectName())))
        self.doubleSpinBox_53.setValue(float(getWeight(self.doubleSpinBox_53.objectName())))
        self.doubleSpinBox_54.setValue(float(getWeight(self.doubleSpinBox_54.objectName())))
        self.doubleSpinBox_55.setValue(float(getWeight(self.doubleSpinBox_55.objectName())))
        self.doubleSpinBox_56.setValue(float(getWeight(self.doubleSpinBox_56.objectName())))
        self.doubleSpinBox_57.setValue(float(getWeight(self.doubleSpinBox_57.objectName())))
        self.doubleSpinBox_58.setValue(float(getWeight(self.doubleSpinBox_58.objectName())))
        self.doubleSpinBox_59.setValue(float(getWeight(self.doubleSpinBox_59.objectName())))
        self.doubleSpinBox_60.setValue(float(getWeight(self.doubleSpinBox_60.objectName())))

    def UpdateLocalDB_csv(self):
        try:
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog

            # Display file dialog and get the selected file path
            file_name, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)", options=options)

            if file_name:
                # print("Selected file:", file_name)  # Print the selected file path
                self.selected_file = file_name  # Store the file path in a variable
                convert_csv_to_json(file_name, 'new_data.json')  # Convert the new ticker data from csv into json
                merge_json('tickers.json', 'new_data.json', 'tickers.json')

                self.db_updated_today = True

                self.saveSettings()


        except:
            self.UpdateLocalDB_button.setStyleSheet("color: red")
            self.UpdateLocalDB_button.setText("Error: Invalid File")
            t.sleep(4)
            self.UpdateLocalDB_button.setStyleSheet("color: white")
            self.UpdateLocalDB_button.setText("Update Local Tickers (.csv)")


class Logs_Viewer(QDialog):
    def __init__(self):
        super(Logs_Viewer, self).__init__()
        uic.loadUi("Logs_Viewer.ui", self)

        self.home_Button.clicked.connect(self.goHome)
        self.back_Button.clicked.connect(self.goBack)

        self.logsFile = 'errors.json'

        self.loadLogs()

    def goHome(self):
        widget.setCurrentIndex(widget.currentIndex() - 11)

    def goBack(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def loadLogs(self):
        with open(self.logsFile, 'r') as logs_file:
            loaded = json.load(logs_file)['logs']
            parsed_data_formated = ""
            for i in loaded:
                timestamp = list(i.values())[0][0]['timestamp']
                error = list(i.values())[0][0]['error']

                parsed_data_formated += 'Time: ' + timestamp + ':\n' + error + '\n\n\n'

            self.Viewer.setText(parsed_data_formated)

            # scrollbar = self.Viewer.verticalScrollBar()
            # scrollbar.setValue(scrollbar.maximum()) #FIXME: Why does this never work


@profile
def main():
    app = QApplication(sys.argv)

    QCoreApplication.setOrganizationName("FireFlies")
    QCoreApplication.setOrganizationDomain("https://github.com/Kataki-Takanashi")
    # SETTINGS = QSettings()
    testMode = getBox("testMode_Box")  # NOT DYNAMIC

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
    stockT = todayStock()
    settings = Settings()  # to find stuff that looks like this use this regex \w{0,20}\s*\=\s*[^qQ]{0,20}\(\)$ https://regex-vis.com/?r=%5Cw%7B0%2C20%7D%5Cs*%5C%3D%5Cs*%5B%5EqQ%5D%7B0%2C20%7D%5C%28%5C%29%24&e=0
    logs = Logs_Viewer()

    testMode = getBox(settings.testMode_Box.objectName())
    # Connections
    settings.filterBox.currentIndexChanged.connect(stockT.changeFilter)

    widget.addWidget(home)
    widget.addWidget(stock)
    widget.addWidget(halal)
    widget.addWidget(seehalal)
    widget.addWidget(seenotHalal)
    widget.addWidget(history)
    widget.addWidget(seetickerhistory)
    widget.addWidget(yesterday)
    widget.addWidget(today)
    widget.addWidget(stockT)
    widget.addWidget(settings)
    widget.addWidget(logs)
    widget.show()
    widget.setFixedSize(487, 1387)  # TODO setting to save current window pos and one for size as default
    widget.move(0, 0)
    app.exec_()


QCoreApplication.setOrganizationName("FireFlies")
QCoreApplication.setOrganizationDomain("https://github.com/Kataki-Takanashi")
QCoreApplication.setApplicationName("HalalStockOrganizer")
SETTINGS = QSettings()
testMode = getBox("testMode_Box")  # NOT DYNAMIC

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
stockT = todayStock()
settings = Settings()
logs = Logs_Viewer()
widget.addWidget(home)
widget.addWidget(stock)
widget.addWidget(halal)
widget.addWidget(seehalal)
widget.addWidget(seenotHalal)
widget.addWidget(history)
widget.addWidget(seetickerhistory)
widget.addWidget(yesterday)
widget.addWidget(today)
widget.addWidget(stockT)
widget.addWidget(settings)
widget.addWidget(logs)

# halalSettings = json.loads(SETTINGS.value("halal", defaultValue=json.dumps({"fields": [halal.ticker_Input.text(), halal.lotso_Input.toPlainText()], "halal": []})))
# stockSettings = json.loads(SETTINGS.value("stock", defaultValue=json.dumps({"halal": [], "filters": {"Default": ['fa_salesqoq_o30', 'ind_stocksonly', 'ipodate_prev3yrs', 'sh_avgvol_o500', 'sh_short_o5',
#                    'ta_changeopen_u', 'ta_sma20_pa', 'ta_sma200_pa', 'ta_sma50_pa']}})))
# settingsSettings = json.loads(SETTINGS.value("settings", defaultValue=json.dumps({
#             "boxes": [{settings.testMode_Box.objectName(): settings.testMode_Box.isChecked()} , {settings.autoFilter_Box.objectName(): settings.autoFilter_Box.isChecked()} , {settings.showFilter_Box.objectName(): settings.showFilter_Box.isChecked()} , {settings.savespot_Box.objectName(): settings.savespot_Box.isChecked()} , {settings.clear_Box.objectName(): settings.clear_Box.isChecked()} ],
#             "currentFilter": "",
#             "weights": [{settings.doubleSpinBox_61.objectName(): settings.doubleSpinBox_61.value()} , {settings.doubleSpinBox_62.objectName(): settings.doubleSpinBox_62.value()} , {settings.doubleSpinBox_63.objectName(): settings.doubleSpinBox_63.value()} , {settings.doubleSpinBox_64.objectName(): settings.doubleSpinBox_64.value()} , #FIXME fix these names theyre horrendous
#                         {settings.doubleSpinBox_49.objectName(): settings.doubleSpinBox_49.value()} , {settings.doubleSpinBox_50.objectName(): settings.doubleSpinBox_50.value()} , {settings.doubleSpinBox_51.objectName(): settings.doubleSpinBox_51.value()} , {settings.doubleSpinBox_52.objectName(): settings.doubleSpinBox_52.value()} ,
#                         {settings.doubleSpinBox_65.objectName(): settings.doubleSpinBox_65.value()} , {settings.doubleSpinBox_66.objectName(): settings.doubleSpinBox_66.value()} , {settings.doubleSpinBox_67.objectName(): settings.doubleSpinBox_67.value()} , {settings.doubleSpinBox_68.objectName(): settings.doubleSpinBox_68.value()} ,
#                         {settings.doubleSpinBox_69.objectName(): settings.doubleSpinBox_69.value()} , {settings.doubleSpinBox_70.objectName(): settings.doubleSpinBox_70.value()} , {settings.doubleSpinBox_71.objectName(): settings.doubleSpinBox_71.value()} , {settings.doubleSpinBox_72.objectName(): settings.doubleSpinBox_72.value()} ,
#                         {settings.doubleSpinBox_73.objectName(): settings.doubleSpinBox_73.value()} , {settings.doubleSpinBox_74.objectName(): settings.doubleSpinBox_74.value()} , {settings.doubleSpinBox_75.objectName(): settings.doubleSpinBox_75.value()} , {settings.doubleSpinBox_76.objectName(): settings.doubleSpinBox_76.value()} ,
#                         {settings.doubleSpinBox_77.objectName(): settings.doubleSpinBox_77.value()} , {settings.doubleSpinBox_78.objectName(): settings.doubleSpinBox_78.value()} , {settings.doubleSpinBox_78.objectName(): settings.doubleSpinBox_78.value()} , {settings.doubleSpinBox_80.objectName(): settings.doubleSpinBox_80.value()} ,
#                         {settings.doubleSpinBox.objectName(): settings.doubleSpinBox.value()} , {settings.doubleSpinBox_2.objectName(): settings.doubleSpinBox_2.value()} , {settings.doubleSpinBox_3.objectName(): settings.doubleSpinBox_3.value()} , {settings.doubleSpinBox_4.objectName(): settings.doubleSpinBox_4.value()} ,
#                         {settings.doubleSpinBox_45.objectName(): settings.doubleSpinBox_45.value()} , {settings.doubleSpinBox_46.objectName(): settings.doubleSpinBox_46.value()} , {settings.doubleSpinBox_47.objectName(): settings.doubleSpinBox_47.value()} , {settings.doubleSpinBox_48.objectName(): settings.doubleSpinBox_48.value()} ,
#                         {settings.doubleSpinBox_53.objectName(): settings.doubleSpinBox_53.value()} , {settings.doubleSpinBox_54.objectName(): settings.doubleSpinBox_54.value()} , {settings.doubleSpinBox_55.objectName(): settings.doubleSpinBox_55.value()} , {settings.doubleSpinBox_56.objectName(): settings.doubleSpinBox_56.value()} ,
#                         {settings.doubleSpinBox_57.objectName(): settings.doubleSpinBox_57.value()} , {settings.doubleSpinBox_58.objectName(): settings.doubleSpinBox_58.value()} , {settings.doubleSpinBox_59.objectName(): settings.doubleSpinBox_59.value()} , {settings.doubleSpinBox_60.objectName(): settings.doubleSpinBox_60.value()}
#                         ]
#         })))
# SETTINGS.clear()
windowSettings = SETTINGS.value("window", defaultValue=[False, False], type=list)

# testMode = settings.getSavedables()["boxes"][0]
testMode = getBox(settings.testMode_Box.objectName())
# Connections
settings.filterBox.currentIndexChanged.connect(lambda: stockT.changeFilter(settings.filterBox.currentIndex()))
stockT.filters.currentIndexChanged.connect(lambda: settings.changeFilter(stockT.filters.currentIndex()))
# print(getBox(settings.testMode_Box.objectName()))
if has_apikey:
    home.Update_Button.clicked.connect(lambda: UpdateLocalDB_api(has_apikey))
    settings.db_updated_today = True
    settings.saveSettings()
else:
    home.Update_Button.clicked.connect(settings.UpdateLocalDB_csv)

widget.show()
if getBox("savespot_Box"):
    widget.setFixedSize(487, 1387)  # if windowSettings[0] else None
    widget.move(0, 0)  # if windowSettings[1] else None
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
