import yfinance as yf
import pandas as pd
from datetime import date as d
from datetime import timedelta
import time
import csv
from googlesheet import Sheet


date = "07/02/2022"
a = Sheet("BTST Trades")
data = a.getWorksheet(date)



#==============================================================================================================


for stock in data:
		try:
			dt = stock['date'].split('-')



			tkr = yf.Ticker(stock['symbol']+".ns")

			data = tkr.history(start=(d(int(dt[2]),int(dt[1]),int(dt[0]))),end=(d(int(dt[2]),int(dt[1]),int(dt[0])))+timedelta(10)).fillna(0)

			print(stock['symbol'],stock['date'],data['Close'][0],data['Open'][1])



		except Exception as e:
			print(stock,e)


dateX = date.split("/")
