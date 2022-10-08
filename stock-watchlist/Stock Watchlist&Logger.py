# Max score: ~22.6 or 23 Min score: ~-13

# Imports
import logging
import random

import finviz
import pickle
import time
import pandas
import json
from datetime import date
from datetime import datetime
import stuffy as stuffyimportsys

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
today = date.today()
date = today.strftime("%d/%m/%Y")
timestamp = dt_string
# Variables
num = random.randint(0, 10000)
num2 = str(num)
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

# files
"""
file = open('save_data.txt', 'r') this is to read
file = open('save_data.txt', 'w') this is to write
file = open('save_data.txt', 'a') this is to append (to file)
file = open('save_data.txt', 'r+') this is to read and write
"""


# with open('save_data', 'r') as file:
# pass


# Functions
def error(error):
    """
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
    # with open('save_data.txt', 'r') as file:
    #     contents = file.read()
    #     print(contents, end='')

    with open(filename, 'r') as file:
        data = json.load(file)
        # print(data["logs"][0][date][0]["dat"][0]["#data here"])
        stuff = data["logs"]
        return data


def questioner(aCount, question, answers):
    # for i in answers:
    #     answers.append("\n")
    while True:
        print(question)
        for i in answers:
            print(i)
        q1 = int(input(">>> "))
        if q1 == 0:
            break
        elif q1 <= aCount:
            return q1
        else:
            error("Error: Line 77, wrong aCount, check parameters.")
            print("Or wrong option.")


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


def newStock(ticker):
    halal = input("Is it halal?\n>>> ")
    if halal in yes:
        save({"ticker": ticker, "halal": True}, "tickers.json")
        # again = input("Another one?\n>>> ").lower()
        # if again in yes:
        #     pass

    elif halal in no:
        save({"ticker": ticker, "halal": False}, "tickers.json")
        # again = input("Another one?\n>>> ").lower()
        # if again in yes:
        #     pass


# def askindicator(indicator, question):
#     indi = input(question)
def score():
    # The 200!
    score = 0
    # print(score)
    indicators = []
    the200 = input("Is above the 200 or below the 200? y/n\n>>> ")
    if the200 in yes:
        score += t200["gWeight"]
        indicators.append("Is above the 200!")
    elif the200 in no:
        score += t200["bWeight"]
        indicators.append("Is UNDER the 200!")
    the200 = input(f'{t200["spc"]} y/n\n>>> ')
    if the200 in no:
        pass
    else:
        the200 = input(f'{t200["spc"]} y/n\n>>> ')
        if the200 in yes:
            score += t200["gsp"]
            indicators.append("Is about to cross above the 200!")
        elif the200 in no:
            score += t200["bsp"]
            indicators.append("Is about to cross UNDER the 200!")

    print(score)

    # The 9!
    quizz = input("Is it above The 9? y/n\n>>> ")
    if quizz in yes:
        score += t9["gWeight"]
        indicators.append("Is above the 9!")
    elif quizz in no:
        score += t9["bWeight"]
        indicators.append("Is under the 9!")
    quizz = input(f'{t9["spc"]} y/n\n>>> ')
    if quizz in no:
        pass
    else:
        quizz = input(f'{t9["spc"]} y/n\n>>> ')
        if quizz in yes:
            score += t9["gsp"]
            indicators.append("Is one candle close above the 9!")
        elif quizz in no:
            score += t9["bsp"]
            indicators.append("Is one candle close UNDER the 9! (sell)")
    print(score)
    # The MACD!
    quizz = input("Is the MACD above the the red or below the red/Is it in the green or red? y/n\n>>> ")
    if quizz in yes:
        score += MACD["gWeight"]
        indicators.append("MACD Is above the the red (line) or is in the green (bar)!")
    elif quizz in no:
        score += MACD["bWeight"]
        indicators.append("MACD Is UNDER the red (line) or is in the red (bar)!")
    quizz = input(f'{MACD["spc"]} y/n\n>>> ')
    if quizz in no:
        pass
    else:
        quizz = input(f'{MACD["spc"]} y/n\n>>> ')
        if quizz in yes:
            score += MACD["gsp"]
            indicators.append("MACD Is reverseing to green or crossing above the red!")
        elif quizz in no:
            score += MACD["bsp"]
            indicators.append("MACD Is reversing to red or crossing under the red!")

    print(score)
    # The RSI!
    quizz = input("Is the RSI low(good)(y) or high(bad)(n)? y/n\n>>> ")
    if quizz in yes:
        score += RSI["gWeight"]
        indicators.append("RSI is low!")
    elif quizz in no:
        score += RSI["bWeight"]
        indicators.append("RSI is high!")
    quizz = input(f'{RSI["spc"]} y/n\n>>> ')
    if quizz in no:
        pass
    else:
        quizz = input(f'{RSI["spc"]} y/n\n>>> ')
        if quizz in yes:
            score += RSI["gsp"]
            indicators.append("RSI is overbought!")
        elif quizz in no:
            score += RSI["bsp"]
            indicators.append("RSI is oversold!")

    print(score)
    # The VWAP!
    quizz = input("Is it above or below the VWAP? (above/on is gogo juise! VWAP above 9 is gogo) y/n\n>>> ")
    if quizz in yes:
        score += VWAP["gWeight"]
        indicators.append("We have GoGo Juise!")
    elif quizz in no:
        score += VWAP["bWeight"]
        indicators.append("No gogo juise! :(")

    print(score)
    # Heiken Ashi!
    quizz = input("Is the Heiken Ashi trending up or down? y/n\n>>> ")
    if quizz in yes:
        score += HA["gWeight"]
        indicators.append("Heiken Ashi is trending UP!")
    elif quizz in no:
        score += HA["bWeight"]
        indicators.append("Heiken Ashi is trending DOWN!")

    print(score)
    # Smoothed Heiken Ashi Candles!
    quizz = input("Is the Smoothed Heiken Ashi Candles trending up or down? y/n\n>>> ")
    if quizz in yes:
        score += SHAC["gWeight"]
        indicators.append("Smoothed Heiken Ashi Candles are trending UP!")
    elif quizz in no:
        score += SHAC["bWeight"]
        indicators.append("Smoothed Heiken Ashi Candles are trending DOWN!")

    print(score)
    # Ribbons
    quizz = input("Is above or below the Ribbons? y/n\n>>> ")
    if quizz in yes:
        score += RIB["gWeight"]
        indicators.append("Is above the Ribbons!")
    elif quizz in no:
        score += RIB["bWeight"]
        indicators.append("Is BELOW the Ribbons!")

    print(score)
    # VPVR
    quizz = input("Is there VPVR? y/n\n>>> ")
    if quizz in yes:
        score += VPVR["gWeight"]
        indicators.append("VPVR looks good!")
    elif quizz in no:
        score += VPVR["bWeight"]
        indicators.append("VPVR looks bad!")
    quizz = input(f'{VPVR["spc"]} y/n\n>>> ')
    if quizz in no:
        pass
    else:
        quizz = input(f'{VPVR["spc"]} y/n\n>>> ')
        if quizz in yes:
            score += VPVR["gsp"]
            indicators.append("Is about to jump UP!")
        elif quizz in no:
            score += VPVR["bsp"]
            indicators.append("Is about to jump DOWN!")

    print(score)
    # LUX Algo Premium!
    quizz = input("Is LUX good? y/n\n>>> ")
    if quizz in yes:
        score += LUX["gWeight"]
        indicators.append("LUX looks good!")
    elif quizz in no:
        score += LUX["bWeight"]
        indicators.append("LUX looks bad!")
    quizz = input(f'{LUX["spc"]} y/n\n>>> ')
    if quizz in no:
        pass
    else:
        quizz = input(f'{LUX["spc"]} y/n\n>>> ')
        if quizz in yes:
            score += LUX["gsp"]
            indicators.append("Is near or in the buy cloud!")
        elif quizz in no:
            score += LUX["bsp"]
            indicators.append("Is near or in the sell cloud!")

    # if scoreORindicators == "score" or scoreORindicators in yes:
    #     return score
    # elif scoreORindicators == "indicators" or scoreORindicators in no:
    #     return indicators
    print(score)

    pack = [score, indicators]
    return pack


def q1():
    name = input("What is the ticker?\n>>> ").upper()
    if name in seeStock("halal"):  # and name not in seeStock("nothalal"):
        print("Stock is halal, proceeding...")
        stuff = score()
        stuffy = [round(stuff[0], 2), stuff[1]]
        #stuffy = score()

        timestamp = time("time")
        save({"ticker": name, "time": timestamp, "packet": [timestamp, stuffy]}, "save_data.json")
    elif name in seeStock("nothalal"):  # and name not in seeStock("halal"):
        print("Stock is NOT Halal, unable to proceed, check Zoya, edit 'tickers.json' if nessesary...")
    elif name not in seeStock("halal") and name not in seeStock("nothalal"):
        # ticker = input("What is the ticker?\n>>> ").upper()
        print("Not registerd, makeing new stock log...")
        newStock(name)

def q2():
    while True:
        qqq = questioner(4, "What do you want to do?",
                         ["1. Check if a stock is halal.", "2. View halal stocks.",
                          "3. View NOT halal stocks.", "4. Exit..."])
        if qqq == 1:
            flag = False
            while flag == False:
                flag = False
                ticker = input("What is the ticker?\n>>> ").upper()

                if ticker in seeStock("halal"):
                    qq = input("Ticker is Halal. Another ticker? y/n\n>>> ")
                    if qq in yes: pass
                    else:flag=True

                elif ticker in seeStock("nothalal"):
                    qq = input("Ticker is NOT Halal. Another ticker? y/n\n>> ")
                    if qq in yes: pass
                    else:flag=True

                elif ticker not in seeStock("halal") and ticker not in seeStock("nothalal"):
                    newStock(ticker)
                    again = input("Another ticker? y/n\n>>> ").lower()
                    if again in yes:
                        pass
                    else:
                        flag = True
                    # newStock(ticker)
                    # halal = input("Is it halal?\n>>> ")
                    # if halal in yes:
                    #     save({"ticker": ticker, "halal": True}, "tickers.json")

                else:
                    pass

        elif qqq == 2:
            print(' '.join(seeStock("halal")))
            break
        elif qqq == 3:
            print(' '.join(seeStock("nothalal")))
            break
        elif qqq == 3:
            break
        else:
            break
        #  ticker = input("What is the ticker?\n>>> ").upper()
        # # stuff = load("tickers.json")
        # # stuffs = []
        # # nothalal = []
        # # for i in stuff["logs"]:
        # #     things = i["ticker"]
        # #     if i["halal"] == True:
        # #         stuffs.append(things)
        # #     elif i["halal"] == False:
        # #         nothalal.append(things)
        #
        # if halalCheck(ticker) == "halal":
        #     qq = input("Ticker is Halal. Another ticker?\n>>> ")
        #     if qq in yes:
        #
        # elif ticker in nothalal:
        #     qq = input("Ticker is NOT Halal. See Not Halal tickers?")
        #     if qq in yes:
        #         print(nothalal)
        #         again = input("Another ticker?\n>>> ").lower()
        #         if again in yes:
        #             pass
        #         else:
        #             break
        #     elif qq in no:
        #         again = input("Another ticker?\n>>> ").lower()
        #         if again in yes:
        #             pass
        #         else:
        #             break
        #     else:
        #         again = input("Another ticker?\n>>> ").lower()
        #         if again in yes:
        #             pass
        #         else:
        #             break
        # if ticker not in stuffs and ticker not in nothalal:
        #     halal = input("Is it halal?\n>>> ")
        #     if halal in yes:
        #         save({"ticker": ticker, "halal": True}, "tickers.json")
        #         again = input("Another one?\n>>> ").lower()
        #         if again in yes:
        #             pass
        #         else:
        #             break
        #     elif halal in no:
        #         save({"ticker": ticker, "halal": False}, "tickers.json")
        #         again = input("Another one?\n>>> ").lower()
        #         if again in yes:
        #             pass
        #         else:
        #             break
        #
        #     else:
        #         break
        # else:
        #     pass


def q3():
    while True:
        q = questioner(5, "What do you want to do?", ["1. View history.", "2. View ticker history.", "3. Yesterday.", "4. Today.", "5. Exit... "])
        if q == 1:
            history = load("save_data.json")
            # print(history)
            for i in history["logs"]:
                print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
            qs = input("Do you want to look at a block?\n>>> ")
            # if qs in yes:
            #     theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
            #     for block in history["logs"]:
            #         while True:
            #             if block["time"] == theblock:
            #                 for i in block["packet"][1][1]:
            #                     print(i)
            #                 break
            #             else:
            #                 error("Wrong TimeStamp! make sure its n the (d/m/y h/m/s) format!")
            #                 break
            if qs in yes:
                theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
                for block in history["logs"]:
                    if block["time"] == theblock:
                        for i in block["packet"][1][1]:
                            print(i)
                        print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
            elif qs in no:
                pass
            else:
                error("Error: not an option, try again. Exit Code [4]")
                pass
        elif q == 2:
            history = load("save_data.json")
            name = input("What is the ticker?\n>>> ").upper()
            if name in seeStock("halal"):  # and name not in seeStock("nothalal"):
                print("Stock is halal, proceeding...")
                for i in history["logs"]:
                    if i["ticker"] == name:
                        print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
                qs = input("Do you want to look at a block?\n>>> ")
                if qs in yes:
                    theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
                    for block in history["logs"]:
                        if block["time"] == theblock:
                            for i in block["packet"][1][1]:
                                print(i)
                            print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
                elif qs in no:
                    pass
                else:
                    error("Error: not an option, try again. Exit Code [4]")
                    pass
            elif name in seeStock("nothalal"):  # and name not in seeStock("halal"):
                print("Stock is NOT Halal, unable to proceed, check Zoya, edit 'tickers.json' if nessesary...")
            elif name not in seeStock("halal") and name not in seeStock("nothalal"):
                # ticker = input("What is the ticker?\n>>> ").upper()
                print("Not registerd, makeing new stock log...")
                newStock(name)
        elif q == 3:
            from datetime import date, timedelta
            todays = date.today()
            yesterday = todays - timedelta(days=1)  # FIX FORMAT
            yesterday = yesterday.strftime('%d/%m/%Y')
            history = load("save_data.json")
            for i in history["logs"]:
                stRing = i["time"]
                dateChar = stRing[0: 10]
                if yesterday == dateChar:
                    print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
            qs = input("Do you want to look at a block?\n>>> ")
            if qs in yes:
                theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
                for block in history["logs"]:
                    if block["time"] == theblock:
                        for i in block["packet"][1][1]:
                            print(i)
                        print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
            elif qs in no:
                pass
            else:
                error("Error: not an option, try again. Exit Code [4]")
                pass
        elif q == 4:
            theday = time("date")
            history = load("save_data.json")
            for i in history["logs"]:
                stRing = i["time"]
                dateChar = stRing[0: 10]
                if theday == dateChar:
                    print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
            qs = input("Do you want to look at a block?\n>>> ")
            if qs in yes:
                theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
                for block in history["logs"]:
                    if block["time"] == theblock:
                        for i in block["packet"][1][1]:
                            print(i)
                        print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
            elif qs in no:
                pass
            else:
                error("Error: not an option, try again. Exit Code [4]")
                pass
        elif q == 5:
            break
        # history = load("save_data.json")
        # # print(history)
        # for i in history["logs"]:
        #     print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
        # qs = input("Do you want to look at a block?\n>>> ")
        # # if qs in yes:
        # #     theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
        # #     for block in history["logs"]:
        # #         while True:
        # #             if block["time"] == theblock:
        # #                 for i in block["packet"][1][1]:
        # #                     print(i)
        # #                 break
        # #             else:
        # #                 error("Wrong TimeStamp! make sure its n the (d/m/y h/m/s) format!")
        # #                 break
        # if qs in yes:
        #     theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
        #     for block in history["logs"]:
        #         if block["time"] == theblock:
        #             for i in block["packet"][1][1]:
        #                 print(i)
        #             print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
        # elif qs in no:
        #     pass
        # else:
        #     error("Error: not an option, try again. Exit Code [4]")
        #     pass

# def q4():
#     """
#     takes yesterdays stocks and prints them
#     :return:
#     """
#     from datetime import date, timedelta
#     today = date.today()
#     yesterday = today - timedelta(days=1) #FIX FORMAT
#     yesterday = yesterday.strftime('%d/%m/%Y')
#     history = load("save_data.json")
#     for i in history["logs"]:
#         stRing = i["time"]
#         dateChar = stRing[0 : 10]
#         if yesterday == dateChar:
#             print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
#     qs = input("Do you want to look at a block?\n>>> ")
#     if qs in yes:
#         theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
#         for block in history["logs"]:
#             if block["time"] == theblock:
#                 for i in block["packet"][1][1]:
#                     print(i)
#                 print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
#     elif qs in no:
#         pass
#     else:
#         error("Error: not an option, try again. Exit Code [4]")
#         pass




# def q5():
#     """
#     Takes todays stocks and prints them
#     :return:
#     """
#     theday = time("date")
#     history = load("save_data.json")
#     for i in history["logs"]:
#         stRing = i["time"]
#         dateChar = stRing[0: 10]
#         if theday == dateChar:
#             print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
#     qs = input("Do you want to look at a block?\n>>> ")
#     if qs in yes:
#         theblock = input("Enter the timestamp: (d/m/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
#         for block in history["logs"]:
#             if block["time"] == theblock:
#                 for i in block["packet"][1][1]:
#                     print(i)
#                 print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
#     elif qs in no:
#         pass
#     else:
#         error("Error: not an option, try again. Exit Code [4]")
#         pass


# save()
# load()
# print(t200["name"], MACD["name"], RSI["name"])
# print(VPVR )

# Close the file!
# make list of tickers in file



# Main
# while True:
#     try:
#         q = questioner(4, "What do you want to do?",
#                        ["1. Do a stock check.", "2. Check if your stock is halal.", "3. View history.", "4. Exit... "])
#
#         if q == 1:
#             name = input("What is the ticker?\n>>> ").upper()
#             if name in seeStock("halal"):  # and name not in seeStock("nothalal"):
#                 print("Stock is halal, proceeding...")
#                 stuffy = score()
#                 save({"ticker": name, "time": timestamp, "packet": [timestamp, stuffy]}, "save_data.json")
#             elif name in seeStock("nothalal"):  # and name not in seeStock("halal"):
#                 print("Stock is NOT Halal, unable to proceed, check Zoya, edit 'tickers.json' if nessesary...")
#             elif name not in seeStock("halal") and name not in seeStock("nothalal"):
#                 # ticker = input("What is the ticker?\n>>> ").upper()
#                 print("Not registerd, makeing new stock log...")
#                 newStock(name)
#
#         elif q == 2:
#             while True:
#                 qqq = questioner(4, "What do you want to do?",
#                                  ["1. Check if a stock is halal.", "2. View halal stocks.",
#                                   "3. View NOT halal stocks.", "4. Exit..."])
#                 if qqq == 1:
#                     pass
#                 elif qqq == 2:
#                     print(seeStock("halal"))
#                     break
#                 elif qqq == 3:
#                     print(seeStock("nothalal"))
#                     break
#                 elif qqq == 3:
#                     break
#                 else:
#                     break
#                 ticker = input("What is the ticker?\n>>> ").upper()
#                 stuff = load("tickers.json")
#                 stuffs = []
#                 nothalal = []
#                 for i in stuff["logs"]:
#                     things = i["ticker"]
#                     if i["halal"] == True:
#                         stuffs.append(things)
#                     elif i["halal"] == False:
#                         nothalal.append(things)
#
#                 if ticker in stuffs:
#                     qq = input("Ticker is Halal. See more?\n>>> ")
#                     if qq in yes:
#                         print(stuffs)
#                         again = input("Another ticker?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#                     elif qq in no:
#                         again = input("Another ticker?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#                     else:
#                         again = input("Another ticker?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#                 elif ticker in nothalal:
#                     qq = input("Ticker is NOT Halal. See Not Halal tickers?")
#                     if qq in yes:
#                         print(nothalal)
#                         again = input("Another ticker?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#                     elif qq in no:
#                         again = input("Another ticker?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#                     else:
#                         again = input("Another ticker?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#                 if ticker not in stuffs and ticker not in nothalal:
#                     halal = input("Is it halal?\n>>> ")
#                     if halal in yes:
#                         save({"ticker": ticker, "halal": True}, "tickers.json")
#                         again = input("Another one?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#                     elif halal in no:
#                         save({"ticker": ticker, "halal": False}, "tickers.json")
#                         again = input("Another one?\n>>> ").lower()
#                         if again in yes:
#                             pass
#                         else:
#                             break
#
#                     else:
#                         break
#                 else:
#                     pass
#
#
#         elif q == 3:
#             history = load("save_data.json")
#             # print(history)
#             for i in history["logs"]:
#                 print(f'On {i["time"]} {i["ticker"]} had a score of {i["packet"][1][0]}')
#             qs = input("Do you want to look at a block?\n>>> ")
#             if qs in yes:
#                 theblock = input("Enter the timestamp: (m/d/y h/m/s)   Ex:12/06/2022 01:44:53\n>>> ")
#                 for block in history["logs"]:
#                     if block["time"] == theblock:
#                         for i in block["packet"][1][1]:
#                             print(i)
#             print(f'{block["ticker"]} had a score of {block["packet"][1][0]}')
#             if qs in no:
#                 break
#             else:
#                 error("Error: not an option, try again. Exit Code [3]")
#                 break
#         elif q == 4 or q == "e".lower():
#             break
#         else:
#             error("Error: Not an option, try again1.")
#     except:
#         error("Error: Not an option, try again2.")

 # Main
flag = False
while True:
    q = questioner(4, "What do you want to do?", ["1. Do a stock check.", "2. Check if your stock is halal.", "3. View history.", "4. Exit... "])
    if q == 1:
        flag = False
        while flag == False:
            flag = False
            q1()
            q = input("Another ticker? y/n\n>>> ")
            if q in yes: pass
            else: flag = True
    elif q == 2:
        q2()
    elif q == 3:
        q3()
    elif q == 4:
        break
        #q4()
    elif q == 5:
        break
        #q5()
    elif q == 6 or q == "e".lower():
        break
