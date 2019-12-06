from core.eda import print_eda
from core.mining import print_mining
from core.preprocessing import print_preprocessing
from core.transformation import print_transformation
from core.utils.io import load_data

from os import system, name

def main():
	print()
	print("---->> FRAUD DETECTION FOR FINANCIAL SERVICES <<----")
	print("      exploiting Big Data Analytics techniques")
	print()
	print("This simple tool learns from the PaySim dataset to predict fraudulent") 
	print("behaviour in balance transactions.")
	print()
	print("Select the starting phase among the options: ")
	print(" (1) Exploratory Data Analysis.")
	print(" (2) Data Preprocessing.")
	print(" (3) Data Transformation.")
	print(" (4) Data Mining.")
	print(" (5) Exit")
	print()

	choice = int(input())
	print()
	data = load_data(choice)

	if (choice <= 1):
		print_eda(data)
	if (choice <= 2):
		data = print_preprocessing(data)
	if (choice <= 3):
		data = print_transformation(data)
	if (choice <= 4):
		data = print_mining(data)

	print()
	print("End of execution.")
	print("----------------------------------------------------")
	print()
	print("Do you want to restart the tool?")
	print(" (1) Yes")
	print(" (0) No")
	print()

	if(int(input()) == 1):
		print("----------------------------------------------------")
		print()
		if name == 'nt': 
			system('cls')
		else:
			system('clear') 
		main()
	else:
		print()
		print("Bye bye!")
		print("----------------------------------------------------")
		print()
		print()	

main()

