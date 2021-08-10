import os 
import webbrowser
import datetime
today = datetime.datetime.now()
print("Welcome to Spectrum Database Terminal.")
print("Spectrum will help you to get more info about this class. If you are new to Spectrum System please say ''I need help''.")
print("Class: COSC 146 - Applied Programming & Scripting Class")
print("Instructor: Phillip L. Francis     ", "Date: ", today)
SpectrumAdmin = input("Write something that you want to know about this class: ")
if SpectrumAdmin == str("List the students"):
	os.system('studentlist.py')
elif SpectrumAdmin == str("Show the syllabus"):
	os.system('classinfo.py')
elif SpectrumAdmin == str("What are the upcoming assignments?"):
	os.system('upcomingassignments.py')
elif SpectrumAdmin == str("What were the last assignments?"):
	os.system('lastassignments.py')
elif SpectrumAdmin == str("What's my grade? "):
	os.system('mygrade.py')
elif SpectrumAdmin == str("I would like to open Canvas"):
	webbrowser.open('https://canvas.emich.edu/courses/45310')
elif SpectrumAdmin == str("What I am running on my computer?"):
	print("Spectrum Database System for Eastern Michigan University")
	print("Version 0.1 Beta 1 2009000001")
	print("Programmed by Deniz Karya Acikbas EID Number: E01825290 E-Mail: dacikbas@emich.edu")
elif SpectrumAdmin == str("Get me out"):
        quit()
elif SpectrumAdmin == str("I need help"):
	os.system('help.py')
else:
	print("Spectrum didn`t quite understand you. Please type it again :-)")
	os.system('adminterminal.py')
