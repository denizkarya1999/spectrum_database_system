import os 
User = input("User@System: ")

if user == str("studentlist"):
	os.system('studentlist.py')
elif user == str("exit"):
        quit()
else:
	print("Wrong")
	os.system('terminal.py')
