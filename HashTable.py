# # Q) Write a program that inserts N random int keys into a table of size N/100  using chaining,
# # then finds the length of the shortest and longest lists, for N = 10^3 , 10^4,10^5,10^6  h(k) = AK %10

import random as rd

class AdjNode:
    def __init__(self, val):
        self.val = val
        self.nt = None

def pprint(table):
    mx_size=0
    mn_size=len(table)**2
    for i in table:
        if i[1]>mx_size:
            mx_size=i[1]
        if i[1]!=0 and i[1]<mn_size:
            mn_size=i[1]
    print('longest length - ',mx_size,'smallest size - ',mn_size)


lt = [10 ** i for i in range(3, 7)]
for i in lt:
    print('SIZE OF LIST IS ',i/100)
    table = [[None, 0] for j in range(int(i / 100))]
    for j in range(i):
        x = rd.randint(1, i)
        fn = int(0.618 * x % 10)
        nd = AdjNode(x)
        nd.nt = table[fn][0]
        table[fn][0] = nd
        table[fn][1] += 1
    pprint(table)
    



## Q)Using the double hashing techniques and linear probing, resolve collision while inserting N random integers into a hashtable. two functions are
# h1 = (i+11)% M
# h2 = (i+11*k)%M

#secondary clustering , primary clustering

m= 1000
I=int(m/2)**2
n= 60
lt=[None for i in range(m)]
for i in range(n):
    x=rd.randint(1,10**3)
    fn=((I+11)%m + I*(I + 11*x) % m)%m
    count=1
    while lt[fn] is not None:
        fn=(fn+1)%m
        count+=1
    lt[fn]=(x,count)
for i in lt:
    print(i)






