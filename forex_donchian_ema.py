from googlesheet import Sheet


a = Sheet("FOREX DN EMA","CHFJPY")
data = a.getSheet()

for i in range(len(data)):
	if data[i]["close"] < data[i]["EMA low"] and data[i]["open"] > data[i]["EMA low"]: #Short
		entry = data[i+1]["open"]
		sl = data[i+1]["Upper"]
		diff = ( sl - entry) * 2
		target = entry - diff

		for a in range(i+1,len(data)):
			new_sl = data[a]["Upper"]

			if sl > new_sl:
				sl = new_sl

			if data[a]["high"] >= sl :
				print(data[i]['date'],data[a]['date'],"short","SL",sl,entry)
				# print(entry,sl,data[a]["high"])
				break

			elif data[a]["low"] <= target:
				print(data[i]['date'],data[a]['date'],"short","TP",target,entry)
				break
			else:
				pass



	elif data[i]["close"] > data[i]["EMA high"] and data[i]["open"] < data[i]["EMA high"]: #Long
		entry = data[i+1]["open"]
		sl = data[i+1]["Lower"]
		diff = ( entry - sl) * 2
		target = entry + diff

		for a in range(i+1,len(data)):
			new_sl = data[a]["Lower"]

			if sl < new_sl:
				sl = new_sl

			if data[a]["high"] >= target :
				print(data[i]['date'],data[a]['date'],"long","TP",entry,target)
				# print(entry,sl,data[a]["high"])
				break

			elif data[a]["low"] <= sl:
				print(data[i]['date'],data[a]['date'],"long","SL",entry,sl)
				break

			else:
				pass

	else:
		pass
