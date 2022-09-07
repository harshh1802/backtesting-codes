import pandas as pd


closes = pd.read_csv('foban.csv')['Close']

high = closes[0]
low = closes[0]
dd = 0
ddlist = []

for pointer in closes:
	if pointer > high:
		high = pointer
		low = high
		

	if pointer < high:
		if pointer < low:
			low = pointer
			dd = ((low-high)/high)*100
			ddlist.append(dd)
			print(high,low)
		else:
			continue

	if pointer == high:
		continue

	else:

		continue 


print(high,low)

print(ddlist)

print(ddlist.index(min(ddlist)))

