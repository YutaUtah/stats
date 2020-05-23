# ROC AUC

#### 1. confusion matrix

classification model falls in 4 types: TP, FP, TN, FN 

TP: 真陽性 

FP: 偽陽性 

TN: 真陰性 

FN: 偽陰性 

#### accuracy 

全体のデータの中で正しく分類できたTPとTNがどれだけあるかという指標。高いほど性能が良い。

TP + FN / TP + FP + FN + TN

#### precision

Positiveと分類されたデータ(TP + FP)の中で実際にPositiveだったデータ(TP)数の割合。この値が高いほど性能が良く、間違った分類が少ないということを意味する。

TP / TP + FP

#### recall

取りこぼし無くPositiveなデータを正しくPositiveと推測できているかどうか。

この値が高いほど性能がよく、間違ったPositiveの判断が少ないということ。別の言い方をすれば本来Positiveと推測すべき全データの内、どれほど回収できたかという指標。

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

面積が大きいということはすなわち機械学習モデルがNegative と推測すべきものを間違えてPositive と推測している傾向が少なく、Positive と推測すべきものをしっかりとPositive と推測できている状態です。

