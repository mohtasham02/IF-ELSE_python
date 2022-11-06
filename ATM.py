print("WELCOME TO CANARA BANK")

lang=int(input("enter the language"))
if lang==1:
	print("english")
elif lang==2:
	print("hindi")
else:
	print("please choose a language")
print("please insert your credit card")
user_pin=0000
user_pin=int(input("enter the pin"))
if user_pin==0000:
	print("correct pin")
else:
	print("incorrect pin")
balance=10000
if user_pin==0000:
	choose=int(input("Please choose an option from the following:-  1.WITHDRAW 2.BALANCE 3.DEPOSIT"))
	if choose==1:
		print("withdraw")
		withdraw=int(input("enter the withdraw amount"))
		if withdraw<balance:
			balanace=balance-withdraw
			print("withdraw amount is",withdraw,"and the remaining balance is",balanace)
		else:
			print("INSUFFICIENT BALANCE")
	elif choose==2:
		print("balance")
		print("the current balance in your account is",balance)
	elif choose==3:
		print("deposit")
		deposit=int(input("enter the deposit amount"))
		deposit=balance+deposit
		print("so now the total balance is",deposit)
	else:
		print("INSUFFICIENT BALANCE")
else:
	print("wrong pin")
print("THANK YOU FOR VISITING")