import pandas as pd
import pickle as pk

import datetime
import json

with open('config.json','rb') as handle:
	config = json.load(handle)		

def load_data(choice):
	if (choice <= 2):
		dataset = None
		print("Loading dataset...")
		dataset = pd.read_csv(config["folder"]["dataset"] + config["artifact"]["dataset"])
		print("Dataset loaded!")
		print()
		return dataset

	elif (choice == 3):
		prep_dataset = None
		print("Loading preprocessed dataset...")
		with open(config["folder"]["preprocessed"] + config["artifact"]["preprocessed"],'rb') as handle:
			prep_dataset = pk.load(handle)
		print("Preprocessed Dataset loaded!")
		print()	
		return prep_dataset

	elif (choice == 4):
		training_set = None
		test_set = None
		print("Loading training set...")
		with open(config["folder"]["training"] + config["artifact"]["training"], 'rb') as handle:
			training_set = pk.load(handle)
		print("Training set loaded!")
		print()
		print("Loading test set...")
		with open(config["folder"]["test"] + config["artifact"]["test"], 'rb') as handle:
			test_set = pk.load(handle)
		print("Test set loaded!")
		print()
		return [training_set, test_set]

def save_data(data, operation):
	now = datetime.datetime.now()
	time = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)

	if (operation == "preprocessing"):
		filename = "preprocessed_"+time
		with open(config["folder"]["preprocessed"] + filename + '.pk', 'wb') as handle:
			pk.dump(data, handle, protocol=pk.HIGHEST_PROTOCOL)

	if (operation == "transformation_training"):
		filename = "training_"+time
		with open(config["folder"]["training"] + filename + '.pk', 'wb') as handle:
			pk.dump(data, handle, protocol=pk.HIGHEST_PROTOCOL)

	if (operation == "transformation_test"):
		filename = "test_"+time
		with open(config["folder"]["test"] + filename + '.pk', 'wb') as handle:
			pk.dump(data, handle, protocol=pk.HIGHEST_PROTOCOL)

	if (operation == "model"):
		filename = "model_"+time
		with open(config["folder"]["model"] + filename + '.pk', 'wb') as handle:
			pk.dump(data, handle, protocol=pk.HIGHEST_PROTOCOL)

	if (operation == "results"):
		filename = "results_"+time
		data.to_csv(config["folder"]["results"] + filename + '.csv', sep=',', index=False)
		
	return now
