# ROC AUC

#### 1. confusion matrix

classification model falls in 4 types: TP, FP, TN, FN 


#### accuracy 

TP + FN / TP + FP + FN + TN

#### precision

TP / TP + FP

#### recall

TP / TP + FN 

True negative rate 

TN / FP + TN

False negative rate 

FN / TP + FN


#### 2. ROC(Receiver Operating Characteristic)

X: False negative rate

Y: True negative rate

In this ROC curve, AUC(Area Under the Curve) is an area below ROC curve, and the bigger area it has, the better machine learning model it is. 

i.e. having bigger area means that machine learning model has less tendency in falsely detecting positive that is supposed to be detected as negative, and successfully detecting positive that is supposed to be detected as positive.  

