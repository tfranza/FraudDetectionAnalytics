import matplotlib.pyplot as plt
import numpy as np

import core.utils.plots_util as util

def plot_fields_correlation(df):
    plt.matshow(df.corr(method='pearson'), cmap=plt.cm.RdYlGn)
    plt.colorbar()

    return plt

def plot_daily_amount_of_transactions(df):
    fig = plt.figure(figsize=(13,6))
    
    # data preparation 
    transactions = util.get_time_transactions(df)["all"].values
    days = [x/24.0 for x in df["step"].sort_index().unique()]

    # plot marginal details
    alpha_plot = 0.3
    color_all = '#0066ff'
    linewidth_plot = 0.9
    fontsize_labels = 13
    fontsize_title = 16
    
    # plotting data
    plt.title('DAILY AMOUNT OF TRANSACTIONS\n', fontsize=fontsize_title)
    plt.plot(days, transactions, 
             label='transactions/day', 
             color=color_all)
    plt.xticks(np.arange(np.ceil(min(days)), max(days)+1, step=7.0))
    plt.fill_between (days, transactions, 0, alpha=alpha_plot, facecolor=color_all)
    plt.xlabel('\ndays', fontsize=fontsize_labels)
    plt.ylabel('# transactions\n', fontsize=fontsize_labels)
    plt.grid(True)
    plt.legend()

    return plt

def plot_normalized_variations_in_transactions(df):
    fig = plt.figure(figsize=(13,6))

    # data preparation 
    [genuine_var, fraud_var] = util.get_transaction_variations(df)
    genuine_var = [x - genuine_var[0] for x in genuine_var]
    fraud_var = [x - fraud_var[0] for x in fraud_var]
    days = [x/24.0 for x in df["step"].sort_index().unique()[:-1]]
    
    # plot marginal details
    color_fraud = '#cc0000'
    color_genuine = '#00cc00'
    linewidth_plot = 0.9
    fontsize_labels = 13
    fontsize_title = 16
    
    # plotting data 
    ax1 = fig.add_subplot(211)
    ax1.plot(days, genuine_var, 
             label='genuine transactions variation', 
             color=color_genuine, 
             linewidth=linewidth_plot)
    ax1.set_xticks(np.arange(np.ceil(min(days)), max(days)+1, step=7))
    ax1.set_title('NORMALIZED DAILY VARIATIONS IN TRANSACTIONS\n', fontsize = fontsize_title)
    ax1.grid(True)
    ax1.legend()

    ax2 = fig.add_subplot(212)
    ax2.plot(days, fraud_var, 
             label='fraud transactions variation', 
             color=color_fraud, 
             linewidth=linewidth_plot-0.4)
    ax2.set_xticks(np.arange(np.ceil(min(days)), max(days)+1, step=7.0))
    ax2.set_xlabel('days', fontsize=fontsize_labels)
    ax2.grid(True)
    ax2.legend()

    plt.subplots_adjust(left=None, right=None, bottom=0.13, top=None, wspace=None, hspace=0.2)
    plt.ylabel('                                         variation', fontsize=fontsize_labels)

    return plt

def plot_normalized_trends_in_transactions(df):
    fig = plt.figure(figsize=(13,6))
    
    # data preparation 
    [genuine_daily, fraud_daily] = util.get_day_transactions(df)
    [genuine_weekly, fraud_weekly] = util.get_week_transactions(df)
    [genuine_hourly, fraud_hourly] = util.get_hour_transactions(df)

    days = list (range(1,32))
    week = list (range(1,8))
    hours = list (range(1,25))

    # plot marginal details
    color_fraud = '#cc0000'
    color_genuine = '#00cc00'
    linewidth_plot = 0.9
    fontsize_labels = 13
    fontsize_title = 16
   
    # plotting data 
    ax11 = fig.add_subplot(131)
    ax12 = ax11.twinx()
    ax11.plot(days, genuine_daily, 
              label='genuine daily', 
              color=color_genuine, 
              linewidth=linewidth_plot)
    ax12.plot(days, fraud_daily, 
              label='fraud daily', 
              color=color_fraud, 
              linewidth=linewidth_plot)
    ax11.set_xticks(np.arange(min(days), max(days)+1, step=7.0))
    ax12.set_yticks([])
    ax11.set_xlabel('timeline in days', fontsize=fontsize_labels)
    ax11.set_ylabel('# transactions', fontsize=fontsize_labels)
    ax11.grid(True)

    ax21 = fig.add_subplot(132)
    ax22 = ax21.twinx()
    ax21.plot(week, genuine_weekly, 
              label='genuine weekly', 
              color=color_genuine, 
              linewidth=linewidth_plot)
    ax22.plot(week, fraud_weekly, 
              label='fraud weekly', 
              color=color_fraud, 
              linewidth=linewidth_plot)
    ax21.set_xlabel('days in the week', fontsize=fontsize_labels)
    ax22.set_yticks([])
    ax21.set_title('NORMALIZED TRENDS IN TRANSACTIONS\n', fontsize=fontsize_title)
    ax21.grid(True)

    ax31 = fig.add_subplot(133)
    ax32 = ax31.twinx()
    ax31.plot(hours, genuine_hourly, 
              label='genuine hourly', 
              color=color_genuine, 
              linewidth=linewidth_plot)
    ax32.plot(hours, fraud_hourly, 
              label='fraud hourly', 
              color=color_fraud, 
              linewidth=linewidth_plot)
    ax31.set_xticks(np.arange(min(hours), max(hours)+1, step=2))
    ax32.set_yticks([])
    ax31.set_xlabel('hours in the day', fontsize=fontsize_labels)
    ax31.grid(True)

    plt.subplots_adjust(left=None, right=None, bottom=0.3, top=None, wspace=0.16, hspace=0.1)
    
    return plt
    
def plot_distribution_in_transaction_behaviours(df):
    fig = plt.figure(figsize=(13,6))

    # data preparation 
    transactions = util.get_behavioural_transactions(df)
    [genuine_transactions, fraud_transactions] = [transactions["genuine"].values, transactions["fraud"].values]
    types = transactions.index.values

    # plot marginal details
    color_fraud = '#cc0000'
    color_genuine = '#00cc00'
    fontsize_labels = 13
    fontsize_title = 16

    # plotting data
    ax1 = fig.add_subplot(121)
    ax1 = plt.bar(types, genuine_transactions, 
                  label='genuine transactions', 
                  color=color_genuine)
    plt.title('DISTRIBUTION FOR THE TRANSACTION TYPES\n', fontsize=fontsize_title)
    plt.ylabel('# transactions\n', fontsize=fontsize_labels)
    plt.xlabel('\n                                                                                               transaction type', fontsize=fontsize_labels)
    
    ax2 = fig.add_subplot(122)
    ax2 = plt.bar(types, fraud_transactions, 
                  label='fraud transactions', 
                  color=color_fraud)
            
    return plt

def plot_correlation_in_transaction_types(df):
    fig = plt.figure(figsize=(14,7))
    
    # data preparation 
    [payment_transactions, debit_transactions, cashin_transactions, cashout_transactions, transfer_transactions] = util.get_type_transactions(df)

    # plot marginal details
    fontsize_labels = 13
    fontsize_title = 16

    fig.suptitle('      CORRELATION PER FIELDS\n', fontsize=fontsize_title)
    
    # plotting data
    ax1 = fig.add_subplot(231)
    ax1.set_title('ALL\n', fontsize=fontsize_labels)
    ax1.matshow(df.corr(method='pearson'), cmap=plt.cm.RdYlGn)

    ax2 = fig.add_subplot(232)
    ax2.set_title('PAYMENT\n', fontsize=fontsize_labels)
    ax2.matshow(payment_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)
    
    ax3 = fig.add_subplot(233)
    ax3.set_title('DEBIT\n', fontsize=fontsize_labels)
    ax3.matshow(debit_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)

    ax4 = fig.add_subplot(234)
    ax4.set_title('CASH IN\n', fontsize=fontsize_labels)
    ax4.matshow(cashin_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)

    ax5 = fig.add_subplot(235)
    ax5.set_title('CASH OUT\n', fontsize=fontsize_labels)
    ax5.matshow(cashout_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)

    ax6 = fig.add_subplot(236)
    ax6.set_title('TRANSFER\n', fontsize=fontsize_labels)
    ax6.matshow(transfer_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)
    
    plt.subplots_adjust(left=None, right=None, bottom=None, top=0.85, wspace=-0.5, hspace=0.4)

    return plt

def plot_correlation_in_behavioural_transfer_and_cashout_operations(df):
    fig = plt.figure(figsize=(13,6))
    
    # data preparation 
    [cashout_transactions, transfer_transactions] = util.get_type_transactions(df)[3:5]
    genuine_cashout_transactions = cashout_transactions[cashout_transactions["isFraud"]==0]
    fraud_cashout_transactions = cashout_transactions[cashout_transactions["isFraud"]==1]
    genuine_transfer_transactions = transfer_transactions[transfer_transactions["isFraud"]==0]
    fraud_transfer_transactions = transfer_transactions[transfer_transactions["isFraud"]==1]
        
    # plot marginal details
    fontsize_labels = 13
    fontsize_title = 16

    fig.suptitle('CORRELATION PER FIELDS AND BEHAVIOUR\n', fontsize=fontsize_title)
    
    # plotting data
    ax1 = fig.add_subplot(221)
    ax1.set_title('CASH OUT GENUINE\n', fontsize=fontsize_labels)
    ax1.matshow(genuine_cashout_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)

    ax2 = fig.add_subplot(222)
    ax2.set_title('CASH OUT FRAUD\n', fontsize=fontsize_labels)
    ax2.matshow(fraud_cashout_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)
    
    ax3 = fig.add_subplot(223)
    ax3.set_title('TRANSFER GENUINE\n', fontsize=fontsize_labels)
    ax3.matshow(genuine_transfer_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)

    ax4 = fig.add_subplot(224)
    ax4.set_title('TRANSFER FRAUD\n', fontsize=fontsize_labels)
    ax4.matshow(fraud_transfer_transactions.corr(method='pearson'), cmap=plt.cm.RdYlGn)

    plt.subplots_adjust(left=None, right=None, bottom=None, top=0.85, wspace=-0.1, hspace=0.4)

    return plt

def plot_distribution_customers_and_merchants(df):
    fig = plt.figure(figsize=(13,6))
    
    # data preparation 
    amount_nameDest_customers = len( df[df["nameDest"].str.startswith("C")] )
    amount_nameDest_merchants = len( df[df["nameDest"].str.startswith("M")] )
    slices = [amount_nameDest_customers, amount_nameDest_merchants]
    
    # plot marginal details
    colours = ['c', 'y']
    fontsize_labels = 13
    fontsize_title = 16
    labels = ["# Customers", "# Merchants"]
    
    # plotting data
    ax1 = fig.add_subplot(111)
    ax1.set_title('DISTRIBUTION AMONG CUSTOMERS AND MERCHANTS\nAS "DEST" RECIPIENTS', fontsize=fontsize_title)
    ax1.pie(slices, 
            labels=labels, 
            colors=colours,
            startangle=90,
            shadow=True,
            explode=(0, 0.1),
            autopct=('%1.1f%%') )
    
    return plt

def plot_distribution_customers_and_merchants(df):
    fig = plt.figure(figsize=(4,4))
    
    # data preparation 
    amount_nameDest_customers = len( df[df["nameDest"].str.startswith("C")] )
    amount_nameDest_merchants = len( df[df["nameDest"].str.startswith("M")] )
    slices = [amount_nameDest_customers, amount_nameDest_merchants]
    
    # plot marginal details
    colours = ['c', 'y']
    fontsize_labels = 13
    fontsize_title = 16
    labels = ["# Customers", "# Merchants"]
    
    # plotting data
    ax1 = fig.add_subplot(111)
    ax1.set_title('DISTRIBUTION AMONG CUSTOMERS AND MERCHANTS\nAS "DEST" RECIPIENTS', fontsize=fontsize_title)
    ax1.pie(slices, 
            labels=labels, 
            colors=colours,
            startangle=90,
            shadow=True,
            explode=(0, 0.1),
            autopct=('%1.1f%%') )
    
    return plt

def plot_precision_recall_curve(precision, recall, average_precision):
    plt.step(recall, precision, color='b', alpha=0.2, where='post')
    plt.fill_between(recall, precision, alpha=0.2, color='b')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.ylim([0.0, 1.0])
    plt.xlim([0.0, 1.0])
    plt.title('Precision-Recall curve: Average Precision = {0:0.2f}'.format(average_precision))

    return plt

def plot_roc_curve(fpr, tpr, roc_auc):
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, 
        color='darkorange',
        lw=lw, 
        label='ROC curve (area = %0.2f)' % roc_auc
        )
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")

    return plt
