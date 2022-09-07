from email.utils import encode_rfc2231
from googlesheet import Sheet

sheet = Sheet("Indian Stocks Option Impulse")




stock = ['BAJF30']





for ab in stock:
	data = sheet.getWorksheet(ab)
	dataset = len(data)
	for i in range(dataset):
		if data[i]['close'] > data[i]['EMA HIGH'] and data[i]['open'] < data[i]['EMA HIGH']:
			entry = data[i+1]['open']



			for a in range(i+1, dataset):
				if data[a]['low'] <= data[a]['EMA LOW']:
					print(data[a]['symbol'],data[a]['time'], entry, data[a]['EMA LOW'],"LONG")
					break

				else:
					pass

		elif data[i]['close'] < data[i]['EMA LOW'] and data[i]['open'] > data[i]['EMA LOW']:
			entry = data[i+1]['open']

			for a in range(i+1,dataset):
				
				if data[a]['high'] >= data[a]['EMA HIGH']:
					print(data[a]['symbol'],data[a]['time'],data[a]['EMA HIGH'],entry,"SHORT")
					break
					
				else:

					pass
			
			
		
		else:

			# print('NT')
			pass