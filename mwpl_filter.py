import csv
import json
import time
from datetime import date
from datetime import date as d
from datetime import timedelta

import gspread
import pandas as pd
import requests
import yfinance as yf
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


#======================== Sheet and worksheet to read data.===========================================

all_range=['1020','2030','3040','4050','5060','6070','7080','8090']

sheet_name = 'just_trade__' #hnavadiya1802

sheet = client.open(sheet_name)

mwpl = sheet.worksheet('just_trade')
mwpl_data = mwpl.get_all_records()
status = sheet.worksheet('status')
state = status.acell('A2').value
final_list = sheet.worksheet("final_list")




def sorting():

    try:
        print("Checking")

        state = status.acell('A2').value

        if state == "Start":
            print('Starting')
            status.update('A2', 'Working')
            final_list.batch_clear(["A2:Z1000"])


            for a in all_range:
                stocks = []

                main = sheet.worksheet(a)
                main_data = main.get_all_records()

                for stock in main_data:
                    stocks.append(stock['STOCK'])

                for stock in stocks:
                    for i in range(len(mwpl_data)):
                        if stock == mwpl_data[i]['Symbol']:
                            if mwpl_data[i]['perc'] > int(a[0:2]) and mwpl_data[i]['perc'] < int(a[2:4]):
                                print(f'{stock}')
                                dateX = str(date.today()).split("-")
                                convertedDate = f"{dateX[2]}-{dateX[1]}-{dateX[0]}"
                                final_list.append_rows(values=[[stock,a,convertedDate]])
             


            print("Done")
            status.update('A2', 'Done')


    except Exception as e:
        status.update('A2', 'Error')
        print(e)


while 1:
    sorting()
    time.sleep(10)






            

        