import requests
from bs4 import BeautifulSoup
import lxml

url = "https://justtrade.cmlinks.in/Derivatives/Derivatives.aspx?opt=14"

payload = {"Content-Length":"0",
		"Cookie":"ASP.NET_SessionId=5n1ddwncpvciew45rw14kp55",

		"Host":"justtrade.cmlinks.in",
	
		"Referer":"https://www.justtrade.in/",
		"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36"

}


response = requests.get(url,headers =payload)



soup = BeautifulSoup(response.text, "lxml")



table = soup.find("table",id = "ctl04_dgPostionLimit")


rows = table.findAll('tr')


for i in range(len(rows)):
	print(rows[i].text.strip().split())