age=int(input("Enter age "))
sex=str(input("Enter gender "))
day=int(input("Enter number of days "))
if age >= 18 and age < 30 :
	if sex == 'male':
		print("wages =",day*700,'as per day=700')
	elif sex == "female":
		print("Wages =",day*750,'as per day=750')
elif age >= 30 and age <= 40:
	if sex == "male":
		print("Wages =",day*800,'as per day =800')
	elif sex == "female":
		print("Wages =",day*850,'as per day=850')
else:
	print(" inappropriate age,do not work")