import requests
from zipfile import ZipFile
import pandas as pd
from datetime import timedelta,date
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from IPython.display import display, HTML
import time

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)







for i in range(1,100):
   now = date(2021,10,1)

   dt = now+timedelta(i)
   dt_string = dt.strftime("%d/%m/%Y")
   a = dt_string.replace("/","",2)
   url = f'https://www1.nseindia.com/archives/nsccl/mwpl/combineoi_{a}.zip'

   r = requests.get(url)
  

   try:

      with open(f"combineoi_{a}.zip",'wb') as f:
          f.write(r.content)
          f.close()


      with ZipFile(f'combineoi_{a}.zip', 'r') as zipObj:
         zipObj.extractall()




      f = open(f'combineoi_{a}.csv','r')
      lines = f.readlines()




      for line in lines:
         # main.append_rows(values=[[line]])
         print(f'{dt_string},{line}')
         # time.sleep(0.5)
         
      print(i)

   except Exception as e:

      print(f'error {a},{str(e)}')
      









