import pandas as pd

import math

import core.utils.plots as plots

def print_eda(input_data):
	print()
	print(" ----------------------------------------------------")
	print("              Exploratory Data Analysis")
	print(" ----------------------------------------------------")
	print()
	print()
	df = input_data

	print("Dataset Sample")
	print()
	print(df.head(20))
	input()

	total = len(df)
	genuine = len(df[df["isFraud"]==0])
	fraud = len(df[df["isFraud"]==1])
	print("Total amount of transactions: " + str(total) + " (" + str(round(total/total, 4)) + "%)")
	print("Total amount of genuine transactions: " + str(genuine) + " (" + str(round(genuine/total, 4)) + "%)")
	print("Total amount of fraud transactions: " + str(fraud) + " (" + str(round(fraud/total, 4)) + "%)")
	input()

	isFraud_skew = df["isFraud"].skew(axis=0)
	print("Skewness for the class field: " + str(round(isFraud_skew, 2)))
	input()

	print("Pearson Correlation Matrix")
	print()
	print(df.corr(method ='pearson'))
	plots.plot_fields_correlation(df).show()
	input()

	print("#########################################")
	print("Analysis field by field")

	print("_____________________________")
	print("Field: step")
	print()
	print("Field Sample")
	print()
	print(df["step"].head(20))
	input()

	print("Daily Amount of Transactions")
	plots.plot_daily_amount_of_transactions(df).show()
	input()

	print("Normalized Daily Variations in Transactions")
	plots.plot_normalized_variations_in_transactions(df).show()
	input()

	print("Normalized Trends in Transactions")
	plots.plot_normalized_trends_in_transactions(df).show()
	input()

	print("_____________________________")
	print("Field: type")
	print()
	print("Field Sample")
	print()
	print(df["type"].head(20))
	input()

	print("Normalized Distribution in Transaction Behaviours")
	plots.plot_distribution_in_transaction_behaviours(df).show()
	input()

	print("Pearson Correlation in Transaction Types")
	plots.plot_correlation_in_transaction_types(df).show()
	input()

	print("Pearson Correlation in Behavioural Transfer and Cashout Operations")
	plots.plot_correlation_in_behavioural_transfer_and_cashout_operations(df).show()
	input()

	print("_____________________________")
	print("Field: amount")
	print()
	print("Field Sample")
	print()
	print(df["amount"].head(20))
	input()

	print("Statistical info on the amount for genuine transactions:")
	print(df[df["isFraud"]==0]["amount"].describe())
	input()

	print("Statistical info on the amount for fraud transactions:")
	print(df[df["isFraud"]==1]["amount"].describe())
	input()

	print("_____________________________")
	print("Field: oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest")
	print()
	print("Field Sample")
	print()
	print(df[["oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "newbalanceDest"]].head(20))
	input()

	print("Rule for PAYMENT: \"- df2_payment['amount'] - df2_payment['orig'] < y\"")
	print("Rule for DEBIT: \"(-df2_debit['orig'] <= df2_debit['amount'] + 1) & (round(df2_debit['dest']) - round(df2_debit['amount']) < y)\"")
	print("Rule for CASH_IN: \"(df2_cashin['orig'] - df2_cashin['amount'] < y) & (- df2_cashin['dest'] - df2_cashin['amount'] < y)\"")
	print("Rule for CASH_OUT: \"(-df2_cashout['orig'] <= df2_cashout['amount'] + 1) & (round(df2_cashout['dest']) - round(df2_cashout['amount']) < y)\"")
	print("Rule for TRANSFER: \"(-df2_transfer['orig'] <= df2_transfer['amount'] + 1) & (round(df2_transfer['dest']) - round(df2_transfer['amount']) < y)\"")
	print()
	print("with y = 1, orig = newbalanceOrig-oldbalanceOrg, dest = newbalanceDest-oldbalanceDest")
	input()

	df2 = df.copy()
	df2["orig"] = df["newbalanceOrig"] - df["oldbalanceOrg"]
	df2["dest"] = df["newbalanceDest"] - df["oldbalanceDest"]
	df2_payment = df2[df2["type"]=="PAYMENT"].copy()
	df2_debit = df2[df2["type"]=="DEBIT"].copy()
	df2_cashin = df2[df2["type"]=="CASH_IN"].copy()
	df2_cashout = df2[df2["type"]=="CASH_OUT"].copy()
	df2_transfer = df2[df2["type"]=="TRANSFER"].copy()
	y = 1                # lambda
	df2_payment["rel"] = - df2_payment["amount"] - df2_payment["orig"] < y
	detection = len(df2_payment[df2_payment["rel"]==False])
	print("Amount of outliers in PAYMENT transactions: " + str(detection) + " over total of " + str(len(df2_payment)) + " >> " + str(math.trunc(detection/len(df2_payment)*100*100)/100) + "%")
	df2_debit["rel"] = (-df2_debit["orig"] <= df2_debit["amount"] + 1) & (round(df2_debit["dest"]) - round(df2_debit["amount"]) < y)
	detection = len(df2_debit[df2_debit["rel"]==False])
	print("Amount of outliers in DEBIT transactions: " + str(detection) + " over total of " + str(len(df2_debit)) + " >> " + str(math.trunc(detection/len(df2_debit)*100*100)/100) + "%")
	df2_cashin["rel"] = (df2_cashin["orig"] - df2_cashin["amount"] < y) & (- df2_cashin["dest"] - df2_cashin["amount"] < y)
	detection = len(df2_cashin[df2_cashin["rel"]==False])
	print("Amount of outliers in CASH-IN transactions: " + str(detection) + " over total of " + str(len(df2_cashin)) + " >> " + str(math.trunc(detection/len(df2_cashin)*100*100)/100) + "%")
	df2_cashout["rel"] = (-df2_cashout["orig"] <= df2_cashout["amount"] + 1) & (round(df2_cashout["dest"]) - round(df2_cashout["amount"]) < y)
	detection = len(df2_cashout[df2_cashout["rel"]==False])
	print("Amount of outliers in CASH-OUT transactions: " + str(detection) + " over total of " + str(len(df2_cashout)) + " >> " + str(math.trunc(detection/len(df2_cashout)*100*100)/100) + "%")
	df2_transfer["rel"] = (-df2_transfer["orig"] <= df2_transfer["amount"] + 1) & (round(df2_transfer["dest"]) - round(df2_transfer["amount"]) < y)
	detection = len(df2_transfer[df2_transfer["rel"]==False])
	print("Amount of outliers in TRANSFER transactions: " + str(detection) + " over total of " + str(len(df2_transfer)) + " >> " + str(math.trunc(detection/len(df2_transfer)*100*100)/100) + "%")
	input()

	print("_____________________________")
	print("Field: nameOrig, nameDest")
	print()
	print("Field Sample")
	print()
	print(df[["nameOrig", "nameDest"]].head(20))
	input()

	print("Distribution among Customers and Merchants")
	plots.plot_distribution_customers_and_merchants(df).show()
	input()

	total_genuine = len(df[df['isFraud']==0])
	clients_genuine_orig = len(df[df['isFraud']==0]['nameOrig'].unique())
	clients_genuine_dest = len(df[df['isFraud']==0]['nameDest'].unique())

	total_fraud = len(df[df['isFraud']==1])
	clients_fraud_orig = len(df[df['isFraud']==1]['nameOrig'].unique())
	clients_fraud_dest = len(df[df['isFraud']==1]['nameDest'].unique())

	print("Amount of genuine transactions in the dataset: " + str(total_genuine) + " (" + str(100*total_genuine/total_genuine) + "%)")     
	print("Amount of 'Orig' clients in the dataset over genuine transactions: " + str(clients_genuine_orig) + " (" + str(round(100*100*clients_genuine_orig/total_genuine)/100) + "%)")
	print("Amount of 'Dest' clients in the dataset over genuine transactions: " + str(clients_genuine_dest) + " (" + str(round(100*100*clients_genuine_dest/total_genuine)/100) + "%)")   
	print("Average genuine transactions per 'Orig' client: " + str(round(1000*total_genuine/clients_genuine_orig)/1000))
	print("Average genuine transactions per 'Dest' client: " + str(round(1000*total_genuine/clients_genuine_dest)/1000))
	input()

	print("Amount of fraud transactions in the dataset: " + str(total_fraud) + " (" + str(100*total_fraud/total_fraud) + "%)")     
	print("Amount of 'Orig' clients in the dataset over fraud transactions: " + str(clients_fraud_orig) + " (" + str(round(100*100*clients_fraud_orig/total_fraud)/100) + "%)")
	print("Amount of 'Dest' clients in the dataset over fraud transactions: " + str(clients_fraud_dest) + " (" + str(round(100*100*clients_fraud_dest/total_fraud)/100) + "%)")   
	print("Average fraud transactions per 'Orig' client: " + str(round(1000*total_fraud/clients_fraud_orig)/1000))
	print("Average fraud transactions per 'Dest' client: " + str(round(1000*total_fraud/clients_fraud_dest)/1000))
	input()

	print("_____________________________")
	print("Field: isFlaggedFraud")
	print()
	print("Field Sample")
	print()
	print(df["isFlaggedFraud"].head(20))
	input()

	false_flagged = len(df[df["isFlaggedFraud"]==0])
	true_flagged = len(df[df["isFlaggedFraud"]==1])
	false_perc = round(100*false_flagged/len(df))/100
	true_perc = round(100*true_flagged/len(df))/100
	print("Amount of 0 values for the field 'isFlaggedFraud': " + str(false_flagged) + " (" + str(false_perc) + "%)")
	print("Amount of 1 values for the field 'isFlaggedFraud': " + str(true_flagged) + " (" + str(true_perc) + "%)")
	input()

	print("End of Exploratory Data Analysis phase.")
	print("#########################################")
	print()
	
	print("Do you want to restart the phase?")
	print(" (1) Yes")
	print(" (0) No")
	print()    
	
	if(int(input()) == 1):
		print_eda(input_data)     

