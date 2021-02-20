from django.shortcuts import render


import pandas as pd
import numpy as np



from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


from pathlib import Path
import os 
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.
def homeView(request):
    return render(request,"home.html",{})


def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = pd.read_csv(os.path.join(BASE_DIR,"diabetes.csv"))

    X = data.drop("Outcome",axis=1)
    Y = data["Outcome"]
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2)

    model = LogisticRegression()
    model.fit(X_train,Y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    l = [val1,val2,val3,val4,val5,val6,val7,val8]
    l = np.array(l)

    pred = model.predict([l])
    returnVal = None
    if pred == [1]:
        returnVal = "Positive"
    else:
        returnVal = "Negative"


    return render(request, 'predict.html',{"result_prediction":returnVal})