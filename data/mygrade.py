import os 
g1 = int(input("Your Quiz 01 Score: "))
g2 = int(input("Your Quiz 02 Score: "))
g3 = int(input("Your Lab 01 Score: "))
g4 = int(input("Your Lab 02 Score: "))
g5 = int(input("Your Lab 03 Score: "))
numberofclasses = int(input("Enter the number of classes that you are entrolled in: "))
totalscore = g1 + g2 + g3 + g4 + g5
youroverallscore = totalscore / numberofclasses
print("Your overall score is", youroverallscore, "%")
os.system('adminterminal.py')