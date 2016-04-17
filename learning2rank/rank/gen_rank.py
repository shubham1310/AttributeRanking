import numpy as np
from numpy import genfromtxt
import csv
# X = genfromtxt('features_face_AB.csv', delimiter=',')

f = open('features_face_Shakira.csv', 'r')
reader = csv.reader(f, delimiter = ',')
X = list(reader)
for i in range(len(X)):
    for j in range(len(X[0])):
        X[i][j] = eval(X[i][j])
X = np.asarray(X)

n_att = 10
weights = np.zeros((4096,10))
for i in range(1,n_att+1):
    f = open('weight'+str(i)+'.txt', 'r')
    weights[:, i-1] = [line.strip() for line in f]
# print (X.shape)
# print (weights.shape)
rank = np.dot(X,weights)
rank = rank.tolist()
print (rank)
