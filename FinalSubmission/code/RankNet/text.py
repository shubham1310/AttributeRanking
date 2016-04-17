# import csv
#
# f = open('rank.txt', 'r')
#
# reader = csv.reader(f, delimiter = ']')
# # print (reader)
# # Rank = []
# for row in reader:
#     Rank = row
# #     Rank.append(row)
# n = 774
#
# Rank[0] = Rank[0][2:]
# for i in range(1,n):
#     Rank[i] = Rank[i][3:]
#
# print (type(Rank[0]))
# print (Rank[1])
# for i in range(n):
#     Rank[i].split(',')
# print (type(Rank[0]))
# print (Rank[1])
# print (len(Rank[0]))
# Rank[0].split(']')
# print (len(Rank[0]))
f = open('rank.txt', 'r')
# reader = csv.reader(f, delimiter = ',')
a=f.read()
a=eval(a)
print (a[0])
