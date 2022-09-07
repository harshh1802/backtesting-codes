from googlesheet import Sheet
import time
import schedule
import yfinance as yf
import requests



def round50(x, base=50):
    return base * round(x/base)

def round100(x, base=100):
    return base * round(x/base)

# 5298366099:AAHeZkCzOz7W31QZoL9a_Zb4gdG-3uIBIFM

def send_msg(instrument,qty1,qty2=0,trigger=0):

    bankNifty = yf.download(tickers='^nsebank', period='5m', interval='5m')
    nifty = yf.download(tickers='^nsei', period='5m', interval='5m')

    if trigger == 0:
        if instrument == "Bank Nifty":
            msg = f'Trade {instrument} {round100(bankNifty["Close"][-1])} CE PE ({qty1})'
            url = f"https://api.telegram.org/bot5100631391:AAF-2smiWt6qylSUO2RmMl-OgisDwHgceZc/sendMessage?chat_id=@testing1802bot&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)

        elif instrument == "Nifty":
            msg = f'Trade {instrument} {round50(nifty["Close"][-1])} CE PE ({qty1})'
            url = f"https://api.telegram.org/bot5100631391:AAF-2smiWt6qylSUO2RmMl-OgisDwHgceZc/sendMessage?chat_id=@testing1802bot&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)

    else:
        if instrument == "Bank Nifty":
            msg = f"""Trade {instrument} {round100(bankNifty["Close"][-1])} CE PE ({qty1}) (This week)
Trade {instrument} {round100(bankNifty["Close"][-1])} CE PE ({qty2}) (Next week)"""
            url = f"https://api.telegram.org/bot5100631391:AAF-2smiWt6qylSUO2RmMl-OgisDwHgceZc/sendMessage?chat_id=@testing1802bot&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)
            

        elif instrument == "Nifty":
            msg = f"""Trade {instrument} {round50(nifty["Close"][-1])} CE PE ({qty1}) (This week )
Trade {instrument} {round50(nifty["Close"][-1])} CE PE ({qty2}) (Next Week)"""
            url = f"https://api.telegram.org/bot5100631391:AAF-2smiWt6qylSUO2RmMl-OgisDwHgceZc/sendMessage?chat_id=@testing1802 bot&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)

            


sheet = Sheet('Mega Trade Bot')



while 1:

    time.sleep(1)


    try:
        status = sheet.getCell('status','A2')

        if status == 'update':
   

            data = sheet.getWorksheet("main")




            for a in data:



                aday = a["day"]
                trigger_time = a["time"]
                instrument = a["instrument"]
                qty1= a["qty1"]
                qty2 = a["qty2"]
                trigger = a["trigger"]
                onoff = a["onoff"]

                if aday == "monday" and onoff == 1:
                    schedule.every().monday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

                elif aday == "tuesday" and onoff == 1:
                    schedule.every().tuesday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

                elif aday == "wednesday" and onoff == 1:
                    schedule.every().wednesday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

                elif aday == "thursday" and onoff == 1:
                    schedule.every().thursday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

                elif aday == "friday" and onoff == 1:
                    schedule.every().friday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

                elif aday == "sunday" and onoff == 1:
                    schedule.every().sunday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

            
            sheet.updateCell("status","A2","done")
            print(schedule.get_jobs())


            print('if')

        
        schedule.run_pending()
        print('else')


    except Exception as e:

        if "429" in str(e):
            print("sleeping...")
            time.sleep(5)     # url = f"https://api.telegram.org/bot5100631391:AAF-2smiWt6qylSUO2RmMl-OgisDwHgceZc/sendMessage?chat_id=@testing1802_bot&text={e}"
        # requests.get(url)
        # print(e)


