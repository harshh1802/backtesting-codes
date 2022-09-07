import gspread
from oauth2client.service_account import ServiceAccountCredentials



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

class Sheet:

	

	def __init__(self,sheetName):
		self.sheetName = sheetName



	def getWorksheet(self,worksheetName):
		sheet = client.open(self.sheetName)
		main = sheet.worksheet(worksheetName)
		return main.get_all_records()


	def getCell(self,worksheetName,cell):
		sheet = client.open(self.sheetName)
		main = sheet.worksheet(worksheetName)
		return main.acell(cell).value

	def updateCell(self,worksheetName,cell,value):
		sheet = client.open(self.sheetName)
		main = sheet.worksheet(worksheetName)
		main.update(cell,value)

	def getWorksheetObject(self,worksheetName):
		sheet = client.open(self.sheetName)
		main = sheet.worksheet(worksheetName)
		return main

	def addWorksheet(self,newWorksheetName):
		sheet = client.open(self.sheetName)
		sheet.add_worksheet(title=newWorksheetName, rows="1000", cols="50")


def getLongTarget(buy,sl,rr):
	diff = buy - sl
	target = buy + (diff * rr)
	return target


def getShortTarget(sell,sl,rr):
	diff = sl - sell
	target = sell - (diff * rr)
	return target 


def getLongRR(buy,sell,sl):
	rr = (sell-buy)/(buy-sl)
	return rr 

def getShortRR(sell,buy,sl):
	rr = (sell-buy)/(sl-sell)
	return rr 

	