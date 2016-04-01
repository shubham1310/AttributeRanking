import csv
filename = 'ranking_Result1.csv'

f = open(filename,'r')
reader = csv.reader(f)

rank_list = list(reader)

tot = 0
acc = 0

for i in range(len(rank_list)):
    [a1,p1] = rank_list[i]
    a1,p1 = float(a1),float(p1)
    for j in range(i+1,len(rank_list)):
        tot += 1
        [a2,p2] = rank_list[j]
        a2,p2 = float(a2),float(p2)
        if a2-a1 != 0:
            if((a2-a1)*(p2-p1) > 0):
                acc += 1
        elif abs(p2-p1)<1:
            acc += 1
print (acc, 'out of', tot, 'correct ranking pairs.')
print ('Percentage Accuracy: ', acc*100./tot)
# print (rank_list)
