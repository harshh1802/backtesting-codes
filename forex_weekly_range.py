from googlesheet import Sheet, Calculation

pair_list = ["EURUSD","GBPUSD","NZDUSD","AUDUSD","USDCHF","USDCAD","USDJPY","EURGBP","EURNZD","EURAUD","EURCHF","EURCAD","EURJPY","GBPNZD","GBPAUD","GBPCHF","GBPCAD","NZDAUD","NZDCHF","NZDCAD","NZDJPY","AUDCHF","AUDCAD","AUDJPY","CADCHF","CADJPY","CHFJPY"]

for pair in pair_list:

	sheet = Sheet("Forex weekly range RAW",f"{pair}")
	data = sheet.getSheet()

	def LongRR(buy,sell,sl):

		rr = (sell-buy)/(buy-sl)
		return rr 


	def ShortRR(sell,buy,sl):
		rr = (sell-buy)/(sl-sell)
		return rr 


	wy = []

	for i in range(len(data)):

	    if data[i]["wy"] not in wy:
	        wy.append(data[i]["wy"])


	cross1 = []

	for weekyear in wy:

	    for d in data:
	    	if d["wy"] == weekyear:
	            if d['close'] > d['ur1'] and d['open'] < d['ur1']:
	            	if d["wy"] == weekyear:
	            		cross1.append(weekyear)

	weekData = []

	for weekyear in cross1:
		for d in data:
			if d["wy"] == weekyear:
				weekData.append(d)


		for i in range(len(weekData)):
			if weekData[i]['close'] > weekData[i]['ur1'] and weekData[i]['open'] < weekData[i]['ur1']:

				try:
					entry = weekData[i+1]['open']
					sl = weekData[i]['sl']

					if entry != weekData[-1]['open']:

						for z in range(i+1,len(weekData)):
							if weekData[z]['low'] < sl:
								a = Calculation()
								rr = LongRR(entry,sl,sl)
								print(pair,weekData[i]['date'],entry,sl,rr,"Long")
							break

						a = Calculation()
						rr = LongRR(entry,weekData[-1]['close'],sl)
						print(pair,weekData[i]['date'],entry,weekData[-1]['close'],rr,"Long")
						break

					else:
						pass

				except:
					pass


		weekData = []

	# --------------------------------Shortttttttttttttttttttttttttttttttt

	cross2 = []

	for weekyear in wy:

	    for d in data:
	    	if d["wy"] == weekyear:
	            if d['close'] < d['lr1'] and d['open'] > d['lr1']:
	            	if d["wy"] == weekyear:
	            		cross2.append(weekyear)

	weekData = []

	for weekyear in cross2:
		for d in data:
			if d["wy"] == weekyear:
				weekData.append(d)


		for i in range(len(weekData)):
			if weekData[i]['close'] < weekData[i]['lr1'] and weekData[i]['open'] > weekData[i]['lr1']:

				try:
					entry = weekData[i+1]['open']
					sl = weekData[i]['sl']

					if entry != weekData[-1]['open']:

						for z in range(i+1,len(weekData)):
							if weekData[z]['high'] > sl:

								rr = ShortRR(entry,sl,sl)
								print(pair,weekData[i]['date'],sl,entry,rr,"Short")
							break
			


						rr = ShortRR(entry,weekData[-1]['close'],sl)
						print(pair,weekData[i]['date'],weekData[-1]['close'],entry,rr,"Short")
						break

					else:
						pass

				except:
					pass


		weekData = []



	            


			


