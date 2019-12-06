import matplotlib.pyplot as plt
import numpy as np

def normalize(list):
    return [float('%.2f'%( (x-min(list)) / (max(list)-min(list)) ) ) for x in list]

#######################################################################
def get_time_transactions(df): 
    time_transactions = df[["step", "isFraud"]].groupby("step").sum()
    time_transactions["all"] = df["step"].value_counts()
    time_transactions = time_transactions[["all", "isFraud"]]
    time_transactions["isGenuine"] = time_transactions["all"]-time_transactions["isFraud"]
    time_transactions.columns = ["all", "fraud", "genuine"]
    
    return time_transactions

def get_day_transactions (df):
    time_transactions = get_time_transactions(df)
    transactions = [time_transactions["genuine"].values, time_transactions["fraud"].values]
    counters = [[0]*31, [0]*31]
    index = 0
    while index < 2:
        day_counter = [0]*31
        i = 0
        for j in range (0, len(transactions[index])):
            if j==24*(i+1):
                i += 1
            day_counter[i] += transactions[index][j] 
        counters[index] = normalize(day_counter)
        index += 1
        
    return counters

def get_week_transactions (df):
    day_transactions = get_day_transactions(df)
    counters = [[0]*7, [0]*7]
    index = 0
    while index < 2:
        week_counter = [0]*7
        for i in range (0, len(day_transactions[index])):
            week_counter[i%7] += day_transactions[index][i]
        counters[index] = normalize(week_counter)
        index += 1
    
    return counters

def get_hour_transactions (df):
    time_transactions = get_time_transactions(df)
    transactions = [time_transactions["genuine"].values, time_transactions["fraud"].values]
    counters = [[0]*24, [0]*24]
    index = 0
    while index < 2:
        hour_counter = [0]*24
        for i in range (0, len(transactions[index])):
            hour_counter[i%24] += transactions[index][i]
        counters[index] = normalize(hour_counter)
        index += 1
        
    return counters

def get_transaction_variations (df):
    time_transactions = get_time_transactions(df)
    transactions = [time_transactions["genuine"].values, time_transactions["fraud"].values]
    counters = [[], []]
    index = 0
    while index < 2:
        variations = []
        for i in range(1,len(transactions[index])):
            variations.append(transactions[index][i] - transactions[index][i-1])
        counters[index] = normalize(variations)
        index += 1
        
    return counters

#######################################################################

def get_behavioural_transactions(df): 
    behav_transactions = df[["type", "isFraud"]].groupby("type").sum()
    behav_transactions["all"] = df["type"].value_counts()
    behav_transactions = behav_transactions[["all", "isFraud"]]
    behav_transactions["isNotFraud"] = behav_transactions["all"]-behav_transactions["isFraud"]
    behav_transactions.columns = ["all", "fraud", "genuine"]
    
    return behav_transactions

def get_type_transactions(df): 
    payments = df[df["type"]=="PAYMENT"]
    debits = df[df["type"]=="DEBIT"]
    cash_ins = df[df["type"]=="CASH_IN"]
    cash_outs = df[df["type"]=="CASH_OUT"]
    transfers = df[df["type"]=="TRANSFER"]
    
    return [payments, debits, cash_ins, cash_outs, transfers]

def get_amount_transactions(df):
    amount_genuine_ts = df[df["isFraud"]==0][["amount"]]
    amount_fraud_ts = df[df["isFraud"]==1][["amount"]]
    
    bins = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
    genuine_bins = [0]*8
    fraud_bins = [0]*8
    i = 0
    for x in bins:
        if (i==0 | i==7):
            genuine_bins[i] = amount_genuine_ts[amount_genuine_ts["amount"]<=bins[i]].count() 
            fraud_bins[i] = amount_fraud_ts[amount_fraud_ts["amount"]<=bins[i]].count() 
        else:
            genuine_bins[i] = amount_genuine_ts[(amount_genuine_ts["amount"]>bins[i-1]) & (amount_genuine_ts["amount"]<=bins[i])].count() 
            fraud_bins[i] = amount_fraud_ts[(amount_fraud_ts["amount"]>bins[i-1]) & (amount_fraud_ts["amount"]<=bins[i])].count() 
        i += 1
    
    return [genuine_bins, fraud_bins]
