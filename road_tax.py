tax=int(input('enter value'))
if tax<100000:
	tax1=int(15/100*100000)
	print('you have to pay',tax1,'of this amount',tax)
elif tax>=50000 and tax<=100000:
	tax2=int(10/100*150000)
	print('you have to pay',tax2,'of this amount',tax)
elif tax>50000:
	tax3=int(5/100*50000)
	print('you have to pay',tax3,'of this amount',tax)