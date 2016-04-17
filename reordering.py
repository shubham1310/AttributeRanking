import numpy as np
from numpy import genfromtxt
import csv
# X = genfromtxt('features_face_AB.csv', delimiter=',')

f = open('train_ranks_SVM.txt', 'r')
b = f.read()
X = eval(b)

label_file = 'labels.txt'
f2 = open(label_file,'r')
l = f2.read().split('\n')

freq = []
for i in range(1,9):
    freq.append(l.count(str(i)))

X_tr = []
X_ts = []

index = 0
for p in freq:
    i = index
    j = index + 85
    k = index + p

    X_tr.extend(X[i:j])
    X_ts.extend(X[j:k])

X_tr.extend(X_ts)

print (len(X_tr))
