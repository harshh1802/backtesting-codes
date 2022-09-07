import yfinance as yf
import pandas as pd
from datetime import date as d
from datetime import timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import slf
import time
import csv


 #Google Cloud Account Setup
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)


#======================== Sheet and worksheet to read data.===========================================

sheet_name = 'Weekly FIb Range Nifty'
worksheet = '25-30'
sheet = client.open(sheet_name)
main = sheet.worksheet(worksheet)


#==============================================================================================================

print('Getting data from Sheet..')
main_data = main.get_all_records()
print('Done...')

count = len(main_data)
filename = f"{sheet_name+'_'+ worksheet}.csv"

print('Process Started...')

week = 0
ur0 = 0 
ur1 = 0
ur2 = 0
ur3 = 0
lr0 = 0
lr1 = 0
lr2 = 0
lr3 = 0

yw = []

for i in range(len(main_data)):

    if main_data[i]["YW"] not in yw:
        yw.append(main_data[i]["YW"])

print(len(yw))


for a in yw:

    for data in main_data:
        if data["YW"] == a:
            if data['high'] > data['ur0']:
                ur0 += 1
                break

    for data in main_data:
        if data["YW"] == a:
            if data['low'] < data['lr0']:
                lr0 += 1
                break


    for data in main_data:
        if data["YW"] == a:
            if data['high'] > data['ur1']:
                ur1 += 1
                break

    for data in main_data:
        if data["YW"] == a:
            if data['low'] < data['lr1']:
                lr1 += 1
                break

    for data in main_data:
        if data["YW"] == a:
            if data['high'] > data['ur2']:
                ur2 += 1
                break

    for data in main_data:
        if data["YW"] == a:
            if data['low'] < data['lr2']:
                lr2 += 1
                break

    for data in main_data:
        if data["YW"] == a:
            if data['high'] > data['ur3']:
                ur3 += 1
                break

    for data in main_data:
        if data["YW"] == a:
            if data['low'] < data['lr3']:
                lr3 += 1
                break


print(f'ur0:{ur0}')
print(f'lr0:{lr0}')
print(f'ur1:{ur1}')
print(f'lr1:{lr1}')
print(f'ur2:{ur2}')
print(f'lr2:{lr2}')
print(f'ur3:{ur3}')
print(f'lr3:{lr3}')



