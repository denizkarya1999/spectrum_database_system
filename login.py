import os 
print("Welcome to Spectrum Database System. In order to log in to your PC, PC please fill out the following information: ")
input("Press Enter to continue to fill out the form...")
selection = input("To continue press 1, to login as an Adminstrator press 2: ")
if selection == str("1"):
	name = input("Your Name: ")
	password = input("Your Password: ")
	username = input("Your Username: ")
	spectrumID = int(input("Your SpectrumID: S"))
	company = int(input("Your company's SpectrumID: "))
	if (spectrumID == 202321 or 267686 or 953459 or 432342) and (selection == 1):
		print("You are successfully logged into Spectrum Database System...")
		os.system('terminal.py')
	else:
		print("We are unable to log you into Spectrum Database System, Please contact with your adminstrator")

elif selection == str("2"):
	adminusername = input("Your Username: ")
	adminpassword = input("Your Password: ")
	if adminusername == str("SpectrumAdmin") and adminpassword == str("XS1105"):
		print("You are successfully logged into Spectrum Database System...")
		os.system('adminterminal.py')
		pass
	else:
		print("We are unable to log you into Spectrum Database System, Please contact with your adminstrator")
else:
	print("We are unable to log you into Spectrum Database System, Please contact with your adminstrator")