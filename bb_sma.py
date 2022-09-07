from googlesheet import Sheet, getShortTarget
from googlesheet import getLongTarget
import time


sheet = Sheet("BB_SMA_SWING")

lst = ['XAUUSD','SP500']
# lst = ['GBPUSD', 'EURUSD', 'NZDUSD', 'AUDUSD', 'USDCHF', 'USDCAD', 'USDJPY', 'EURGBP', 'EURNZD', 'EURAUD', 'EURCHF', 'EURCAD', 'EURJPY', 'GBPNZD', 'GBPAUD', 'GBPCHF', 'GBPCAD', 'NZDAUD', 'NZDCHF', 'NZDCAD', 'NZDJPY', 'AUDCHF','AUDCAD','AUDJPY','CADCHF','CADJPY', 'CHFJPY']

rr = 2

for pair in lst:
    time.sleep(5)
    data = sheet.getWorksheet(pair)

    try:

        for i in range(len(data)):
            

            if data[i]["status"] == 0:
                if data[i]["close"] > data[i]["Upper"] and data[i]["open"] < data[i]["Upper"]: #Long

                

                    
                    entry = data[i+1]["open"]
                    sl = data[i+1]["Plot"]
                    target = getLongTarget(entry,sl,rr)

                    for j in range(i+1,len(data)):
                        

                        data[j]["status"] = 1
                        
                        if data[j]["high"] >= target:
                            exit = target
                            print(pair,data[i]["time"],entry,sl,exit,"L")
                            break

                        elif data[j]["low"] <= sl:
                            exit = sl
                            print(pair,data[i]["time"],entry,sl,exit,"L")
                            break



                elif data[i]["close"] < data[i]["Lower"] and  data[i]["open"] > data[i]["Lower"]: #Short

                    entry = data[i+1]["open"]
                    sl = data[i+1]["Plot"]
                    target = getShortTarget(entry,sl,rr)

                    for k in range(i+1,len(data)):
                        data[k]["status"] = 1
                        
                        if data[k]["low"] <= target:
                            exit = target
                            print(pair,data[i]["time"],exit,sl,entry,"S")
                            break

                        elif data[k]["high"] >= sl:
                            exit = sl
                            print(pair,data[i]["time"],exit,sl,entry,"S")
                            break

                else:
                    pass
            else:
                pass
    except Exception as e:
        print(e)