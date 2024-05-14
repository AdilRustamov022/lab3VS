#14
# İki ölçülü A(n,n) ədədi massivinin baş dioqonalda
# yerləşən elementlərinin həndəsi ortasını hesablayan alqoritm tərtib etməli.
import random

n=2
v=[]

for i in range(n):
    v.append([])
    
    for j in range(n):
        v[i].append(random.randint(2,6))

def diognal_find(b):
    diognal_tim = 1

    for x in range(len(b)):
        diognal_tim*=b[x][x]

    return (diognal_tim)**(1/len(b))

ret=diognal_find(v)

print(ret)
    