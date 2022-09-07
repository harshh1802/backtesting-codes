import schedule
import yfinance as yf
from googlesheet import Sheet
import requests
import time



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
            url = f"https://api.telegram.org/bot5298366099:AAHeZkCzOz7W31QZoL9a_Zb4gdG-3uIBIFM/sendMessage?chat_id=@megatrade18&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)

        elif instrument == "Nifty":
            msg = f'Trade {instrument} {round50(nifty["Close"][-1])} CE PE ({qty1})'
            url = f"https://api.telegram.org/bot5298366099:AAHeZkCzOz7W31QZoL9a_Zb4gdG-3uIBIFM/sendMessage?chat_id=@megatrade18&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)

    else:
        if instrument == "Bank Nifty":
            msg = f"""Trade {instrument} {round100(bankNifty["Close"][-1])} CE PE ({qty1}) (This week)
Trade {instrument} {round100(bankNifty["Close"][-1])} CE PE ({qty2}) (Next week)"""
            url = f"https://api.telegram.org/bot5298366099:AAHeZkCzOz7W31QZoL9a_Zb4gdG-3uIBIFM/sendMessage?chat_id=@megatrade18&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)
            

        elif instrument == "Nifty":
            msg = f"""Trade {instrument} {round50(nifty["Close"][-1])} CE PE ({qty1}) (This week )
Trade {instrument} {round50(nifty["Close"][-1])} CE PE ({qty2}) (Next Week)"""
            url = f"https://api.telegram.org/bot5298366099:AAHeZkCzOz7W31QZoL9a_Zb4gdG-3uIBIFM/sendMessage?chat_id=@megatrade18&text={msg}"
            requests.get(url)
            # log_sheet.append_rows([[current_time,msg]])
            time.sleep(1)

            




a= Sheet("NOCD")
data = a.getWorksheet("Monday")


for a in data:



    aday = a["day"]
    trigger_time = a["time"]
    instrument = a["instrument"]
    qty1= a["qty1"]
    qty2 = a["qty2"]
    trigger = a["trigger"]

    if aday == "monday":
        schedule.every().monday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

    elif aday == "tuesday":
        schedule.every().tuesday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

    elif aday == "wednesday":
        schedule.every().wednesday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

    elif aday == "thursday":
        schedule.every().thursday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

    elif aday == "friday":
        schedule.every().friday.at(trigger_time).do(send_msg,instrument,qty1,qty2,trigger)

    


print(schedule.get_jobs())


while 1:
    schedule.run_pending()