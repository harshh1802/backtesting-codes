#Add 1 extra word at last

status = """

win
loss
loss
loss
loss
loss
win
loss
win
loss
loss
loss
win
loss
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
win
loss
loss
loss
win
win
win
win
win
win
win
loss
loss
win
win
loss
loss
loss
win
win
win
loss
win
loss
loss
loss
loss
loss
loss
loss
win
win
loss
loss
loss
win
loss
loss
loss
loss
loss
loss
win
win
loss
loss
win
win
loss
loss
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
loss
loss
loss
loss
win
win
loss
loss
loss
loss
win
win
loss
loss
loss
loss
win
loss
loss
win
win
win
win
loss
loss
win
win
loss
win
win
win
win
loss
win
loss
win
win
win
loss
win
loss
loss
loss
loss
loss
win
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
loss
loss
win
loss
loss
loss
win
win
win
win
loss
loss
win
win
loss
win
loss
loss
loss
loss
loss
win
win
loss
win
loss
loss
win
win
loss
loss
loss
loss
loss
loss
loss
win
win
loss
win
loss
loss
win
win
loss
win
loss
win
win
loss
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
win
loss
loss
loss
loss
loss
loss
win
win
win
loss
win
loss
loss
loss
win
loss
loss
loss
win
loss
loss
loss
loss
loss
loss
loss
win
win
loss
loss
win
loss
win
win
loss
win
win
loss
loss
loss
win
loss
loss
loss
win
loss
loss
loss
loss
loss
win
loss
win
loss
win
loss
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
win
loss
win
loss
loss
win
win
win
win
win
loss
loss
win
loss
win
loss
win
loss
loss
win
loss
loss
loss
loss
loss
loss
win
loss
win
loss
loss
win
loss
win
loss
loss
win
loss
loss
loss
win
win
loss
win
win
loss
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
win
win
loss
win
loss
loss
loss
win
loss
loss
loss
win
loss
loss
win
loss
loss
loss
loss
loss
loss
loss
win
win
win
win
win
loss
loss
loss
win
win
win
win
win
loss
win
win
win
loss
win
win
win
win
loss
loss
loss
loss
loss
loss
loss
win
loss
loss
loss
loss
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
loss
loss
loss
win
loss
loss
loss
loss
loss
win
loss
loss
loss
loss
loss
win
loss
loss
win
win
win
loss
loss
win
win
loss
loss
win
loss
loss
win
loss
win
loss
win
loss
win
loss
loss
loss
win
win
loss
loss
win
loss
loss
loss
loss
win
win
loss
loss
win
win
win
win
loss
loss
loss
win
win
win
win
win
loss
loss
loss
loss
win
loss
loss
loss
loss
loss
win
loss
loss
win
loss
win
win
win
loss
win
loss
loss
loss
loss
win
win
loss
win
loss
loss
loss
loss
win
loss
win
win
loss
loss
loss
loss
loss
loss
win
loss
loss
loss
win
loss
loss
loss
loss
loss
loss
loss
loss
loss
loss
win
loss
loss
loss
loss
loss
loss
loss
win
win
win
loss
win
loss
loss
loss
loss
loss
win
win
loss
loss
win
loss
loss
loss
loss
win
loss
win
win
loss
loss
loss
loss
loss
loss
hello
"""

str2 = status.split()
srk = 1

lst = []

for i in range(1,len(str2)):


	if str2[i] == str2[i-1]:
		srk = srk+1

	else:
		lst.append(f'{str2[i-1]}{srk}')

		srk = 1

print(lst)

win = []
loss = []

for i in lst:
	if "win" in i:
		win.append(i)
	elif "loss" in i:
		loss.append(i)

	else:
		pass


print(loss)

stloss = []

for i in loss:
	a = i.replace("loss","")
	stloss.append(int(a))

tp = []
for i in win:
	a = i.replace("win","")
	tp.append(int(a))

print(f'Winning streak {max(tp)}')
print(f'Lossing streak {max(stloss)}')

import heapq


a = heapq.nlargest(3, tp, key=None)
b = heapq.nlargest(3, stloss, key=None)

print(a,b)




