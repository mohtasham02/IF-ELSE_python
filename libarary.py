days=int(input('enter no.of days '))
if days<5:
	print('acc.no of days books kept your charge is',days*2)
elif days<10:
	print('acc.no of days book kept your charge is',days*3)
elif days<15:
	print('acc. no of days book kept your charge is',days*4)
elif days>15:
	print('acc. no of days book kept your charge is',days*5)