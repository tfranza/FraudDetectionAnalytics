from sklearn import svm, tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier

def select_model(choice):
    model = None
    
    if (choice == 1):
        model = linearsvc()
        print("Algorithm: Linear Support Vector Classifier")
    elif (choice == 2):
        model = decisiontree()
        print("Algorithm: Decision Trees")
    elif (choice == 3): 
        model = logisticregression()
        print("Algorithm: Logistic Regression")
    elif (choice == 4):
        model = xgboost()
        print("Algorithm: Gradient Booster Classifier")
    elif (choice == 5):
        model = knn()
        print("Algorithm: K-Nearest Neighbors")
    
    return model

def linearsvc():
    return svm.SVC(
        kernel = 'rbf',
        gamma = 'scale',        
        decision_function_shape = 'ovr',
    )

def decisiontree():
    return tree.DecisionTreeClassifier(
        )

def logisticregression():
    return LogisticRegression(
        penalty = 'l2', 
        solver ='liblinear', 
    )

def xgboost():
    return XGBClassifier(
        loss = {'deviance'},
        max_depth = 3,                
        gamma=2,
        eta=0.8,
        reg_alpha=0.5,
        reg_lambda=0.5
    )

def knn():
    return KNeighborsClassifier(
        n_neighbors = 5,
        )
