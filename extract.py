from tqdm import tqdm
import numpy as np
f = open('updated_pubfig_attributes.txt','r')
a = f.read()
a = a.split('\n')
print (len(a))
mat = [[] for i in range(len(a))]
for i in range(len(a)):
    mat[i] = a[i].split('\t')
no_att = len(mat[0])
print (no_att)
for i in tqdm(range(len(mat)-1)):
    mat[i][0] = mat[i][0].split('_')
    if((mat[i][0][1].isdigit() == False)):
        mat[i][0][0] = mat[i][0][0]+mat[i][0][1]
    # print (i)
    for j in range(1,no_att):
        mat[i][j] = mat[i][j].split(' ')

dic = {
"AlexRodriguez" : {},
"CliveOwen" : {},
"HughLaurie" : {},
"JaredLeto" : {},
"MileyCyrus" : {},
"ScarlettJohansson" : {},
"ViggoMortensen" : {},
"ZacEfron" : {},
"AbhishekBachan" : {},
"BarackObama" : {},
"Shakira" : {}
}
atts = [
1,
3,
7,
20,
32,
35,
37,
40,
41,
53
]
for i in dic.keys():
    dic[i]["num"] = 0
    for j in atts:
        dic[i][j] = 0
for i in range(len(mat)-1):
    name = mat[i][0][0]
    if(name in dic.keys()):
        dic[name]["num"]+=1
        for j in atts:
            dic[name][j] += float(mat[i][j][1])
for i in dic.keys():
    print (i, dic[i]["num"])
    for j in dic[i].keys():
        if(j != "num"):
            dic[i][j] /= dic[i]["num"]
    # print(i,dic[i])
names = []
for i in dic.keys():
    names.append(i)
names = sorted(names)
true_rank = [[0 for i in range(len(atts))] for j in range(len(names))]

for i in range(len(names)):
    print (names[i])
    for j in range(len(atts)):
        true_rank[i][j] = dic[names[i]][atts[j]]
    # print (true_rank[i])
true_rank = np.asarray(true_rank)
np.savetxt("yeshi_true_rank.csv", true_rank, delimiter=",")
