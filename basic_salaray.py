basic_salary=int(input('enter salary'))
if basic_salary<=10000:
	HRA=(10000*20)/100
	DA=(10000*80)/100
	gross_salary=int(basic_salary+HRA+DA)
	print('gross_salary',gross_salary)
elif basic_salary<=20000:
	HRA=(20000*25)/100
	DA=(20000*90)/100
	gross_salary=int(basic_salary+HRA+DA)
	print('gross_salary',gross_salary)
elif basic_salary>2000:
	HRA=(20000*30)/100
	DA=(2000*95)/100
	gross_salary=int(basic_salary+HRA+DA)
	print('gross_salary',gross_salary)
else:
	print('no salary')