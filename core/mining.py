from core.utils.io import save_data
from core.utils.eval import evaluate_model
from core.utils.model import select_model

def print_mining(input_data):
    print()
    print()
    print(" ----------------------------------------------------")
    print("                    Data Mining")
    print(" ----------------------------------------------------")
    print()
    print()
    data = input_data

    training = data[0]
    test = data[1]
    
    X_train = training[0]
    y_train = training[1]
    
    X_test = test[0]
    y_test = test[1]

    print("Select the algorithm to train the model: ")
    print(" (1) Linear Support Vector Classifier.")
    print(" (2) Decision Trees.")
    print(" (3) Logistic Regression.")
    print(" (4) Gradient Boosting Classifier.")
    print(" (5) K-Nearest Neighbors.")
    print()

    choice = int(input())
    print()

    print("Training the model...")
    model = select_model(choice)
    model.fit(X_train, y_train)
    print("Done!")
    print()

    print("Testing the model...")
    y_pred = model.predict(X_test)
    print("Done!")
    print()

    print()
    print("Saving the model in the folder \"~/data/model\" ...")
    save_data(model, "model")
    print("Done!")
    print()
    
    evaluate_model(y_test, y_pred)

    print("End of Data Mining phase.")
    print("#########################################")
    print()

    print("Do you want to restart the phase?")
    print(" (1) Yes")
    print(" (0) No")
    print()    
    
    if(int(input()) == 1):
        return print_mining(input_data)    
    else: 
        return model
