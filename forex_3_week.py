from googlesheet import Sheet
import googlesheet

sheet = Sheet("forex_weekly_ema")

pair_list = ["NZDJPY","AUDCHF","AUDCAD","AUDJPY","CADCHF","CADJPY","CHFJPY"]

for pair in pair_list:
    data = sheet.getWorksheet(pair)

    try:


        for i in range(len(data)):

            if data[i]['close'] > data[i]['EMA_U'] and data[i]['open'] < data[i]['EMA_U']:
                tentry = data[i+1]['open']
                texit = data[i+3]['close']
                sl = data[i+1]['EMA_L']

                for a in range(i,i+4):
                    if data[a]['low'] < sl:
                        texit = sl
                        break
                    else:
                        texit = data[a]['close']

                rr = googlesheet.getLongRR(tentry,texit,sl)

                print(pair,data[i+1]['date'],tentry,texit,rr,"Long")

            elif data[i]['close'] < data[i]['EMA_L'] and data[i]['open'] > data[i]['EMA_L']:
                tentry = data[i+1]['open']
                texit= data[i+3]['close']
                sl = data[i+1]['EMA_U']

                for a in range(i,i+4):
                    if data[a]['high'] > sl:
                        texit = sl
                        break
                    else:
                        texit = data[a]['close']

            

                rr = googlesheet.getShortRR(tentry,texit,sl)

                print(pair,data[i+1]['date'],tentry,texit,rr,"Short")

            else:
                pass
    
    except Exception as e:
        print(e)
