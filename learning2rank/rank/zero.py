# import csv
import numpy as np
from sklearn import mixture
from scipy.stats import multivariate_normal
from sklearn import metrics
f = open('rank.txt', 'r')
a=f.read()
a=eval(a)
trueRank = np.asarray(a)
f = open('../../nlabel.txt', 'r')
labels = [eval(line.strip()) for line in f]

n_att = len(a[0])
n_class= max(labels)
n = len(labels)
### Rank to be loaded from rank.txt
Rank = np.zeros((n,n_att))
data= [[] for i in range(n_class)]
train_len=680
for i in range(train_len):
	data[labels[i]-1].append(trueRank[i])
# for i in range(n_class):
# 	print(len(data[i-1]))
gaudist=[]
mean=[]
covar=[]
unseen = [[3,8], [4,7]]
for i in range(n_class):
	g=mixture.GMM(n_components=1,covariance_type='full')
	g.fit(data[i])
	mean.append(g.means_[0])
	covar.append(g.covars_[0])
	# print (covar)
	gaudist.append(g)
# while 1:
# 	a=0
for i in range(len(unseen)):
	mean.append((mean[unseen[i][0]-1] + mean[unseen[i][1]-1])/2)
	covar.append((covar[unseen[i][0]-1] + covar[unseen[i-1][1]-1])/2)
	# [sum(x)/2 for x in zip(mean[unseen[i][0]], mean[unseen[i][1]])]
# for i in range(len(mean)):
# 	print (mean[i])
# 	print (covar[i])
predclass=[]
for i in range(len(labels[train_len:])):
	p=0
	clas=1
	for j in range(len(mean)):
		temp=multivariate_normal(mean[j],covar[j]).pdf(trueRank[train_len+i])
		# print(temp)
		if(temp> p):
			# print ('hi')
			p=temp
			clas=j+1
	predclass.append(clas)
	print (clas,labels[train_len+i])
	# print('\n\n')
	# calculate accuracy
print(metrics.classification_report(predclass,labels[train_len:]))