from googlesheet import Sheet

a = Sheet("bajfin_wma")
data = a.getWorksheet("Sheet1")




r = 1.5#Risk Reward 

for i in range(len(data)):
	if data[i]['time'] == '9:15:00': #13:00:00 for forex
		if data[i]['close'] > data[i]['WMA']: #Long
			high = data[i]['high']
			low = data[i]['low']
			box = high - low
			entry_above = high + box
			sl = data[i]['WMA']


			for a in range(i+1,i+25):
				if data[a]['close'] > entry_above and data[a]['open'] < entry_above:
					entry = data[a+1]['open']
					# diff = ( entry - sl) * r
					# target = entry + diff

					for b in range(a+1,a+25):
						if data[b]['low'] <= sl:
							rr = -1
							# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
							print(data[i]['date'],data[b]['date'],data[a+1]['open'],sl,sl,rr,'L')
							break

						# elif data[b]['high'] >= target:
						# 	rr = (target-data[a+1]['open'])/(data[a+1]['open']-sl)
						# 	print(data[i]['date'],data[b]['date'],data[a+1]['open'],target,sl,rr,'LTP')
						# 	break



						elif data[b]['time'] == "3:00:00": #11:30:00 for forex
							# print("loop 2")
							# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
							rr = (data[b]['close']-data[a+1]['open'])/(data[a+1]['open']-sl)
							print(data[i]['date'],data[b]['date'],data[a+1]['open'],data[b]['close'],sl,rr,"L")
							break
						else:
							pass


							
					break


				else:
					pass



		# else: #Short
		# 	high = data[i]['high']
		# 	low = data[i]['low']
		# 	box = high - low
		# 	entry_below = low - box
		# 	sl = data[i]['WMA']

		# 	for a in range(i+1,i+45):
		# 		if data[a]['close'] < entry_below and data[a]['open'] > entry_below:
		# 			entry = data[a+1]['open']
		# 			diff = ( sl - entry) * r
		# 			target = entry - diff

		# 			for b in range(a+1,a+45):
		# 				if data[b]['high'] >= sl:
		# 					rr = -1
		# 					# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
		# 					print(data[i]['date'],data[b]['date'],sl,data[b]['open'],sl,rr,"S")
		# 					break


		# 				# elif data[b]['low'] <= target:
		# 				# 	rr = r
		# 				# 	print(data[i]['date'],data[b]['date'],data[b]['close'],target,sl,rr,"STP")
		# 				# 	break






		# 				elif data[b]['time'] == '17:00:00':
		# 					# print("loop 2")
		# 					# print(data[i]['date'],data[b]['date'],data[b]['open'],data[b]['close'])
		# 					rr = (data[a+1]['open']-data[b]['close'])/(sl-data[a+1]['open'])
		# 					print(data[i]['date'],data[b]['date'],data[b]['close'],data[a+1]['open'],sl,rr,"S")
		# 					break
		# 				else:
		# 					pass


							
		# 			break


				# else:
				# 	pass