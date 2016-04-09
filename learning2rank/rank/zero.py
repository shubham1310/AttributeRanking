# import csv
import numpy as np
from sklearn import mixture
f = open('rank.txt', 'r')
a=f.read()
a=eval(a)
trueRank = np.asarray(a)
f = open('nlabel.txt', 'r')
labels = [line.strip() for line in f]

n_att = len(a[0])
n_class= max(labels)
n = len(labels)
### Rank to be loaded from rank.txt
Rank = np.zeros((n,n_att))
data= [[] for i in range(len(n_class))]

for i in range(len(labels)):
	data[labels[i]].append(trueRank[i])
g=[]
for i in range(n_class):
	