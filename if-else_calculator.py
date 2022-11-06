num1=int(input('enter 1st number'))
num2=int(input('enter 2nd number'))
op=input('enter operator')
if op=='+':
	total1=num1+num2
	print(total1)
elif op=='-':
	total2=num1-num2
	print(total2)
elif op=='/':
	total3=num1/num2
	print(total3)
elif op=='*':
	total4=num1*num2
	print(total4)
elif op=='\\':
	total5=num1//num2
	print(total5)
elif op=='%':
	total6=num1%num2
	print(total6)