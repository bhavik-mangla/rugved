
import random

iter = 500

sum1=0
n=[]
for i in range (iter):
    temp=0
    sum1=0
    while sum1<=1:
        x=random.random()
        sum1+=x
        if x!=0:
            temp+=1
    n.append(temp)
    


print(sum(n)/len(n))