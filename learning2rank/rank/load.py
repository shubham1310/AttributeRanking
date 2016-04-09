import RankNet
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import csv
f=open("features_face_AB.csv")
X = []
k = 0
for row in csv.reader(f):
    X.append([])
    for i in row:
        X[k].append(eval(i))
    k += 1

rankarray = [[] for i in range(len(X))]

Model = RankNet.RankNet('RankNet.model')
X = np.asarray(X)
py = Model.RankNetpredict(X, batchsize=10)
for i in range(len(py)):
    rankarray[i].append(py[i])
print (rankarray)
