from googlesheet import Sheet
from formula import get_lot,get_pip


# pair_list = ["EURUSD","GBPUSD","NZDUSD","AUDUSD","USDCHF","USDCAD","USDJPY","EURGBP","EURNZD","EURAUD","EURCHF","EURCAD","EURJPY","GBPNZD","GBPAUD","GBPCHF","GBPCAD","NZDAUD","NZDCHF","NZDCAD","NZDJPY","AUDCHF","AUDCAD","AUDJPY","CADCHF","CADJPY","CHFJPY"]
#nzdjpy,audjpy
pair_list = ["USDCHF","USDJPY","CADJPY","EURJPY","AUDJPY"]
# pair_list = ['EURJPY']

for pair in pair_list:

	try:
		# pair = "CADJPY"
		a = Sheet("MT5 Data")
		data = a.getWorksheet(pair)




		r = 1.5#Risk Reward 

		for i in range(len(data)):
			if data[i]['time'] == '18:30:00': #13:00:00 for forex
				if data[i]['close'] > data[i]['WMA']: #Long
					high = data[i]['high']
					low = data[i]['low']
					box = high - low
					entry_above = high + box
					sl = data[i]['WMA']


					for a in range(i+1,i+45):
						if data[a]['close'] > entry_above and data[a]['open'] < entry_above:
							entry = data[a+1]['open']
							# diff = ( entry - sl) * r
							# target = entry + diff

							for b in range(a+1,a+45):
								if data[b]['low'] <= sl:
									rr = -1
									# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
									lots = get_lot(pair,data[a+1]['open'],sl)
									pips = get_pip(pair,sl,data[a+1]['open'])
									profit = lots*100*pips
									print(pair,data[i]['date'],data[b]['date'],data[a+1]['open'],sl,sl,profit,'L')
									break

								# elif data[b]['high'] >= target:
								# 	rr = (target-data[a+1]['open'])/(data[a+1]['open']-sl)
								# 	print(data[i]['date'],data[b]['date'],data[a+1]['open'],target,sl,rr,'LTP')
								# 	break



								elif data[b]['time'] == "17:00:00": #11:30:00 for forex
									# print("loop 2")
									# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
									rr = (data[b]['close']-data[a+1]['open'])/(data[a+1]['open']-sl)

									lots = get_lot(pair,data[a+1]['open'],sl)
									pips = get_pip(pair,data[b]['close'],data[a+1]['open'])
									profit = lots*100*pips
									print(pair,data[i]['date'],data[b]['date'],data[a+1]['open'],data[b]['close'],sl,profit,"L")
									break
								else:
									pass


									
							break


						else:
							pass



				else: #Short
					high = data[i]['high']
					low = data[i]['low']
					box = high - low
					entry_below = low - box
					sl = data[i]['WMA']

					for a in range(i+1,i+45):
						if data[a]['close'] < entry_below and data[a]['open'] > entry_below:
							entry = data[a+1]['open']
							diff = ( sl - entry) * r
							target = entry - diff

							for b in range(a+1,a+45):
								
								if data[b]['high'] >= sl:
									rr = -1
									lots = get_lot(pair,sl,data[a+1]['open'])
									pips = get_pip(pair,data[a+1]['open'],sl)
									profit = lots*100*pips
									# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
									print(pair,data[i]['date'],data[b]['date'],sl,data[a+1]['open'],sl,profit,"S") 
									break


								# elif data[b]['low'] <= target:
								# 	rr = r
								# 	print(data[i]['date'],data[b]['date'],data[b]['close'],target,sl,rr,"STP")
								# 	break






								elif data[b]['time'] == '17:00:00':
									# print("loop 2")
									# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
									lots = get_lot(pair,sl,data[a+1]['open'])
									pips = get_pip(pair,data[a+1]['open'],data[b]['close'])
									profit = lots*100*pips
									rr = (data[a+1]['open']-data[b]['close'])/(sl-data[a+1]['open'])
									print(pair,data[i]['date'],data[b]['date'],data[b]['close'],data[a+1]['open'],sl,profit,"S")
									break
								else:
									pass


									
							break


						else:
							pass

	except Exception as e:
		print(e)
		pass