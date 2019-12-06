import pandas as pd
import pickle as pk

from core.utils.io import save_data

import sklearn

def print_transformation(input_data):
	print()
	print()
	print(" ----------------------------------------------------")
	print("                  Data Transformation")
	print(" ----------------------------------------------------")
	print()
	print()
	data = input_data

	print("Preprocessed Dataset Sample")
	print()
	print(data.head(20))
	print()

	print("Resizing and shuffling genuine transactions...")
	genuine = data[data["isFraud"]==0]    
	fraud = data[data["isFraud"]==1]

	transfers_fraud = data[(data["type"]=="TRANSFER") & (data["isFraud"]==1)]    
	cashouts_fraud = data[(data["type"]=="CASH_OUT") & (data["isFraud"]==1)]    

	transfers_genuine = data[(data["type"]=="TRANSFER") & (data["isFraud"]==0)]    
	cashouts_genuine = data[(data["type"]=="CASH_OUT") & (data["isFraud"]==0)]    

	transfers_genuine = sklearn.utils.shuffle(transfers_genuine)
	cashouts_genuine = sklearn.utils.shuffle(cashouts_genuine)

	transfers_genuine = transfers_genuine[:len(transfers_fraud)]
	cashouts_genuine = cashouts_genuine[:len(cashouts_fraud)]

	genuine = transfers_genuine.append(cashouts_genuine)
	genuine = sklearn.utils.shuffle(genuine)

	data = genuine.append(fraud)
	data = sklearn.utils.shuffle(data)
	print("Done!")
	print()

	print("Changing transaction types into numbers: TRANSFER=1 and CASH_OUT=2...")
	data["type"]=data["type"].map({"TRANSFER":1, "CASH_OUT":2})
	print("Done!")
	print()

	print("Splitting into features and class...")
	X = data.drop("isFraud", axis=1).values
	y = data["isFraud"].values
	print("Done!")
	print()

	test_size = int(len(data)/5)

	print("Generating training data...")
	X_train = X[:-test_size]
	y_train = y[:-test_size]
	print("Done!")
	print()

	print("Generating test data...")
	X_test = X[-test_size:]
	y_test = y[-test_size:]
	print("Done!")
	print()

	training = [X_train, y_train]
	test = [X_test, y_test]

	print("Saving the training set in the folder \"~/data/training\" ...")
	save_data(training, "transformation_training")
	print("Done!")
	print()
	
	print("Saving the test set in the folder \"~/data/test\" ...")
	save_data(test, "transformation_test")
	print("Done!")
	print()
			
	print("End of Data Transformation phase.")
	print("#########################################")
	print()
	
	print("Do you want to restart the phase?")
	print(" (1) Yes")
	print(" (0) No")
	print()    
	
	if(int(input()) == 1):
		return print_transformation(input_data)    
	else: 
		return [training, test]

