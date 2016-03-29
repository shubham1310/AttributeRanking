import RankNet
import numpy as np
feat_file = 'feat_Face.txt'
# X = np.loadtxt(feat_file)
f1 = open(feat_file, 'r')
a = f1.read().split('\n')
X = []

for i in range(len(a)):
    feature = a[i].split("\t")
    X.append(feature[0:512])

label_file = 'labels_face.txt'
f2 = open(label_file,'r')
l = f2.read().split('\n')

freq = []
for i in range(1,9):
    freq.append(l.count(str(i)))
# print (freq)
X_tr = []
l_tr = []
X_ts = []
l_ts = []

index = 0
for p in freq:
    i = index
    j = index + 85
    k = index + p

    X_tr.extend(X[i:j])
    l_tr.extend(l[i:j])
    X_ts.extend(X[j:k])
    l_ts.extend(l[j:k])

    index += p

print (len(X_tr))

