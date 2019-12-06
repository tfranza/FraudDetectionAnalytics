import pandas as pd
import pickle as pk

from core.utils.io import save_data 

def print_preprocessing(input_data):
	print()
	print()
	print(" ----------------------------------------------------")
	print("                  Data Preprocessing                 ")
	print(" ----------------------------------------------------")
	print()
	print()
	data = input_data

	print("Beginning Dataset Sample")
	print()
	print(data.head(20))
	print()
	print("#########################################")
	print("Step 1: Preprocessing along tuples")
	print()	
	print("Removing PAYMENT, DEBIT and CASH-IN transaction types...")
	data = data[(data["type"]=="TRANSFER") | (data["type"]=="CASH_OUT")]
	print("Done!")
	print()

	print("Removing isFlaggedFraud==1 ...")
	data = data[data["isFlaggedFraud"]==0]
	print("Done!")
	print()

	print("End of Preprocessing along tuples.")
	print()

	print("#########################################")
	print("Step 2: Preprocessing along fields")
	print()

	print("Adjusting 'oldbalanceOrg' to 'oldbalanceOrig'...")
	data.rename(columns={'oldbalanceOrg':"oldbalanceOrig"}, inplace=True)
	print("Done!")
	print()

	print("Modifying 'step' field in order to contain data divided per hour...")
	data["step"] = data["step"]%24
	print("Done!")
	print()

	print("Removing 'nameOrig' and 'nameDest' fields...")
	data = data.loc[:, (data.columns != ('nameOrig')) & (data.columns != ('nameDest'))]
	print("Done!")
	print()

	print("Creating 'balanceOrig' as the difference between 'newbalanceOrig' and 'oldbalanceOrig' fields...")
	data["balanceOrig"] = data["newbalanceOrig"]-data["oldbalanceOrig"]
	print("Done!")

	print()

	print("Removing 'oldbalanceOrig' and 'newbalanceOrig' fields...")
	data = data.loc[:, (data.columns != ('oldbalanceOrig')) & (data.columns != ('newbalanceOrig'))]
	print("Done!")
	print()

	print("Removing 'oldbalanceDest' and 'newbalanceDest' fields...")
	data = data.loc[:, (data.columns != ('oldbalanceDest')) & (data.columns != ('newbalanceDest'))]
	print("Done!")
	print()

	print("Removing 'isFlaggedFraud' field...")
	data = data.loc[:, data.columns != ('isFlaggedFraud')]
	print("Done!")
	print()

	print("End of Preprocessing along tuples.")
	print()
	
	print("Preprocessed Dataset Sample")
	print()
	print(data.head(20))
	print()

	print("Amount of fraud overall transactions: " + str(len(data[data["isFraud"]==1])) )
	print("Amount of genuine overall transactions: " + str(len(data[data["isFraud"]==0])) )

	print("Amount of fraud TRANSFER transactions: " + str(len(data[(data["type"]=="TRANSFER") & (data["isFraud"]==1)])) )
	print("Amount of genuine TRANSFER transactions: " + str(len(data[(data["type"]=="TRANSFER") & (data["isFraud"]==0)])) )

	print("Amount of fraud CASH-OUT transactions: " + str(len(data[(data["type"]=="CASH_OUT") & (data["isFraud"]==1)])) )
	print("Amount of genuine CASH-OUT transactions: " + str(len(data[(data["type"]=="CASH_OUT") & (data["isFraud"]==0)])) )

	print()
	print("Saving the preprocessed dataset in the folder \"~/data/preprocessed\" ...")
	save_data(data, "preprocessing")
	print("Done!")
	print()
		
	print("End of Data Preprocessing phase.")
	print("#########################################")
	print()

	print("Do you want to restart the phase?")
	print(" (1) Yes")
	print(" (0) No")
	print()    
	
	if(int(input()) == 1):
		return print_preprocessing(input_data)    
	else: 
		return data

