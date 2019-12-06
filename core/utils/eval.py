import pandas as pd

import sklearn.metrics as metrics

from core.utils.io import save_data
import core.utils.plots as plots

def evaluate_model(y_test, y_pred):

	confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
	print("Confusion Matrix: ")
	print(confusion_matrix)
	input()

	precision_score = round(1000*metrics.precision_score(y_test, y_pred, average='binary'))/1000
	print("Precision Score: " + str(precision_score) )

	recall_score = round(1000*metrics.recall_score(y_test, y_pred, average='binary'))/1000
	print("Recall Score: " + str(recall_score) )

	f1_score = round(1000*metrics.f1_score(y_test, y_pred, average='binary'))/1000
	print("F1 Score: " + str(f1_score) )
	input()

	print("Precision-Recall Curve.")
	precision, recall, _ = metrics.precision_recall_curve(y_test, y_pred)
	average_precision = metrics.average_precision_score(y_test, y_pred)
	plots.plot_precision_recall_curve(precision, recall, average_precision).show()
	input()

	print("Receiver Operating Characteristics.")
	fpr, tpr, _ = metrics.roc_curve(y_test, y_pred)
	roc_auc = metrics.auc(fpr, tpr)
	plots.plot_roc_curve(fpr, tpr, roc_auc).show()
	input()

	print("Saving the results in the folder \"~/data/results\" ...")
	results = pd.DataFrame(pd.DataFrame([['tp', 'fp', 'tn', 'fn', 'precision', 'recall', 'f1']]))
	results = results.append([[
		str(confusion_matrix[0][0]), str(confusion_matrix[0][1]), str(confusion_matrix[1][0]), str(confusion_matrix[1][1]), 
		str(precision_score),
		str(recall_score),
		str(f1_score)
		]])
	save_data(results, "results")
	print("Done!")
	print()
	
