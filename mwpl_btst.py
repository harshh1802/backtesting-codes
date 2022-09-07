from googlesheet import Sheet
import yfinance as yf
from datetime import datetime as d
from datetime import timedelta



sheet1 = Sheet('just_trade__')
just_trade_sheet = sheet1.getWorksheet("04052022")



win = 0
loss = 0
sum_profit = 0
sum_loss = 0
total_pl = 0





date = just_trade_sheet[0]['date']


sheet2 = Sheet("BTST Trades")
new_sheet = sheet2.addWorksheet(date)

worksheetObejct = sheet2.getWorksheetObject(date)
worksheetObejct.append_rows(values=[['symbol','date','buy','sell','%']])

for stock in just_trade_sheet:
	try:
			dt = stock['date'].split('-')



			tkr = yf.Ticker(stock['symbol']+".ns")

			data = tkr.history(start=(d(int(dt[2]),int(dt[1]),int(dt[0]))),end=(d(int(dt[2]),int(dt[1]),int(dt[0])))+timedelta(10)).fillna(0)

			buy = data['Close'][0]
			sell = data['Open'][1]
			pl = ((sell-buy)/buy)*100

			if pl > 0:
				win += 1
				sum_profit += pl 
				total_pl += pl
			else:
				loss += 1
				sum_loss += pl
				total_pl += pl

			worksheetObejct.append_rows(values=[[stock['symbol'],stock['date'],round(data['Close'][0],2),round(data['Open'][1],2),round(pl,2)]])


	except Exception as e:
		print(e)


dateX = date.split("-")

nifty = yf.Ticker("^nsei")
nifty_data = nifty.history(start=d(int(dateX[2]),int(dateX[1]),int(dateX[0])),end=(d(int(dateX[2]),int(dateX[1]),int(dateX[0]))+timedelta(10))).fillna(0)

nifty_close = nifty_data['Close'][0]
nifty_open = nifty_data['Open'][1]

nifty_pl = ((nifty_open-nifty_close)/nifty_close)*100


mwpl_avg = total_pl/(win+loss)

worksheetObejct.update(
	'G2:H12',
	[["win",win],
	["loss",loss],
	[" "," "],
	['profit',round(sum_profit,2)],
	['loss',round(sum_loss,2)],
	[" "," "],
	["avg_profit",round((sum_profit/win),2)],
	# ["avg_profit",round((sum_profit),2)],
	# ["avg_loss",round((sum_loss/loss),2)],
	["avg_loss",round((sum_loss),2)],
	[" "," "],
	["MWPL average",round(mwpl_avg,2)],
	["Nifty",round(nifty_pl,2)],


	])



