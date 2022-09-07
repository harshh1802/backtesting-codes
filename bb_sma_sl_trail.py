from googlesheet import Sheet, getShortTarget
from googlesheet import getLongTarget
import time

sheet = Sheet("BB_SMA_SWING")

lst = ['GBPUSD', 'EURUSD', 'NZDUSD', 'AUDUSD', 'USDCHF', 'USDCAD', 'USDJPY', 'EURGBP', 'EURNZD', 'EURAUD', 'EURCHF', 'EURCAD', 'EURJPY', 'GBPNZD', 'GBPAUD', 'GBPCHF', 'GBPCAD', 'NZDAUD', 'NZDCHF', 'NZDCAD', 'NZDJPY', 'AUDCHF','AUDCAD','AUDJPY','CADCHF','CADJPY', 'CHFJPY']



for pair in lst:
    time.sleep(5)
    data = sheet.getWorksheet(pair)

    try:

        for i in range(len(data)):

            if data[i]["status"] == 0:
                if data[i]["close"] > data[i]["Upper"] and data[i]["open"] < data[i]["Upper"]: #Long
                    
                    entry = data[i+1]["open"]
                    sl = data[i+1]["Plot"]
                    target = getLongTarget(entry,sl,2)

                    candle = 0

                    for j in range(i+1,len(data)):

                        candle += 1

                        new_sl = data[j]["Plot"]

                        if new_sl > sl:
                            sl = new_sl
                        
                        data[j]["status"] = 1
                        
                        # if data[j]["high"] >= target:
                        #     exit = target
                        #     print(data[i]["time"],entry,sl,exit,"LTP")
                        #     break

                        if data[j]["low"] <= sl:
                            exit = sl
                            print(pair,data[i]["time"],entry,sl,exit,"L")
                            break



                elif data[i]["close"] < data[i]["Lower"] and  data[i]["open"] > data[i]["Lower"]: #Short

                    entry = data[i+1]["open"]
                    sl = data[i+1]["Plot"]
                    target = getShortTarget(entry,sl,2)

                    for k in range(i+1,len(data)):

                        new_sl = data[k]["Plot"]

                        if new_sl < sl:
                            sl = new_sl

                        data[k]["status"] = 1
                        
                        # if data[k]["low"] <= target:
                        #     exit = target
                        #     print(data[i]["time"],exit,sl,entry,"STP")
                        #     break

                        if data[k]["high"] >= sl:
                            exit = sl
                            print(pair,data[i]["time"],exit,sl,entry,"S")
                            break

                else:
                    pass
            else:
                pass

    except Exception as e:
        print(e)