#from collections import defaultdict
import collections

my_list = [['A','B',15],['B','A',3],['B','A',2],['B','C',10]]
dict = {}
for i in my_list:
    for p in i:
        var1 = i[0]+i[1]
        var2 = i[2]
    if var1 in dict:
        dict[var1] = dict[var1] + var2
    else:
        dict[var1] = var2
    #print(var1)
print(dict)

dict1 = {}

for i in dict.keys():
     for j in dict.keys():
           if i == ''.join(reversed(j)):
                dict[i] = dict[i] - dict[j]
                 #print(i)
           #else:
                 #dict[i] = dict[j]
                 #print(i)
     print(dict)
