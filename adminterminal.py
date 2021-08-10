import os 
SpectrumAdmin = input("SpectrumAdmin@System: ")

if SpectrumAdmin == str("studentlist"):
	os.system('studentlist.py')
elif SpectrumAdmin == str("exit"):
        quit()
else:
	print("Wrong")
	os.system('adminterminal.py')
