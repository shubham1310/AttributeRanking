import RankNet
import numpy as np
import warnings
warnings.filterwarnings("ignore")

feat_file = 'feat.txt'
# X = np.loadtxt(feat_file)
f1 = open(feat_file, 'r')
a = f1.read().split('\n')
X = []

for i in range(len(a)):
    feature = a[i].split("\t")
    X.append(feature[0:512])

label_file = 'labels.txt'
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

class_strength = [
6	,
8	,
7	,
5	,
2	,
1	,
4	,
3	]

y_tr=[]
for i in range(len(l_tr)):
    y_tr.append(class_strength[int(l_tr[i])-1])

X_tr = np.array(X_tr)
y_tr = np.array(y_tr)

print (len(y_tr),len(X_tr))

Model = RankNet.RankNet()

Model.fit(X_tr,y_tr,n_iter=500)

X_ts = np.array(X_ts)

py = Model.RankNetpredict(X_ts)
print (py)
