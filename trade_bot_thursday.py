import yfinance as yf
import pytz
from datetime import datetime
import requests
import time
from googlesheet import Sheet


IST = pytz.timezone("Asia/Kolkata")
#now = datetime.now()

#current_time = now.strftime("%H:%M")


# timeList = ["09:21","09:31","09:41","09:51","09:57","10:07","10:17","10:27","11:04","11:11","11:21","12:33","12:36","13:34","13:41"]


bank_nifty_time = ["09:22:00","10:17:00","12:31:00","13:09:00","13:41:00","14:06:00"]
nifty_time = ["09:51:00","11:10:00"]

sheet = Sheet("ATM ALERT LOG")
log_sheet = sheet.getWorksheetObject("Sheet1")


bank_nifty_qty = 30
nifty_qty = 30

def round50(x, base=50):
	return base * round(x/base)

def round100(x, base=100):
	return base * round(x/base)

def get_qty(qty):
	return (-1*qty*25)

def generate_msg(instrument,strike_price,qty,trigger):
	if trigger == int(0):
		if instrument == "Bank Nifty":
			msg = f"Trade {instrument} {round100(strike_price)} CE PE ({-1*qty*25}) (This week)"
			return msg

		elif instrument == "Nifty":
			msg = f"Trade {instrument} {round50(strike_price)} CE PE ({-1*qty*50}) (This week )"
			return msg
	else:
		if instrument == "Bank Nifty":
			msg = f"""Trade {instrument} {round100(strike_price)} CE PE ({-1*qty*25}) (This week)
Trade {instrument} {round100(strike_price)} CE PE (-300) (Next week)"""
			return msg

		elif instrument == "Nifty":
			msg = f"""Trade {instrument} {round50(strike_price)} CE PE ({-1*qty*50}) (This week )
Trade {instrument} {round50(strike_price)} CE PE (-300) (Next Week)"""
			return msg
		



while 1:

	try:

		now = datetime.now(IST)
		current_time = now.strftime("%H:%M:%S")

		if current_time in bank_nifty_time:

			if current_time == "14:06:00":

				bankNifty = yf.download(tickers='^nsebank', period='5m', interval='5m')
				msg = generate_msg("Bank Nifty",bankNifty["Close"][-1],(bank_nifty_qty/2),trigger=0)
				url = f"https://api.telegram.org/bot5221990842:AAGxq3dWcoz-gv1bqrk_xJDawyKPWT3gSfs/sendMessage?chat_id=@niftyatm18&text={msg}"
				requests.get(url)
				log_sheet.append_rows([[current_time,msg]])
				time.sleep(1)

			elif current_time in ["09:22:00","10:17:00"]:
				bankNifty = yf.download(tickers='^nsebank', period='5m', interval='5m')
				msg = generate_msg("Bank Nifty",bankNifty["Close"][-1],bank_nifty_qty,trigger=1)
				url = f"https://api.telegram.org/bot5221990842:AAGxq3dWcoz-gv1bqrk_xJDawyKPWT3gSfs/sendMessage?chat_id=@niftyatm18&text={msg}"
				requests.get(url)
				log_sheet.append_rows([[current_time,msg]])
				time.sleep(1)


			else:
				bankNifty = yf.download(tickers='^nsebank', period='5m', interval='5m')
				msg = generate_msg("Bank Nifty",bankNifty["Close"][-1],bank_nifty_qty,trigger=0)
				url = f"https://api.telegram.org/bot5221990842:AAGxq3dWcoz-gv1bqrk_xJDawyKPWT3gSfs/sendMessage?chat_id=@niftyatm18&text={msg}"
				requests.get(url)
				log_sheet.append_rows([[current_time,msg]])
				time.sleep(1)



		if current_time in nifty_time:

			nifty = yf.download(tickers='^nsei', period='5m', interval='5m')
			msg = generate_msg("Nifty",nifty["Close"][-1],nifty_qty,trigger=1)
			url = f"https://api.telegram.org/bot5221990842:AAGxq3dWcoz-gv1bqrk_xJDawyKPWT3gSfs/sendMessage?chat_id=@niftyatm18&text={msg}"
			requests.get(url)
			log_sheet.append_rows([[current_time,msg]])
			time.sleep(1)

		if current_time == "09:00:00":
			msg = "Nifty ATM Telegram Bot is ACTIVE"
			url = f"https://api.telegram.org/bot5221990842:AAGxq3dWcoz-gv1bqrk_xJDawyKPWT3gSfs/sendMessage?chat_id=@niftyatm18&text={msg}"
			requests.get(url)
			time.sleep(1)

	except Exception as e:
		url = f"https://api.telegram.org/bot5221990842:AAGxq3dWcoz-gv1bqrk_xJDawyKPWT3gSfs/sendMessage?chat_id=@niftyatm18&text=Error at Telegram Bot"
		log_sheet.append_rows([[current_time,"Error"]])
		requests.get(url)
		print(e)


