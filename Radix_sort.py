a=[15,59,8,41,35,57,10,88,119,148]
mx_num=max(a)
mx_digit=0
while mx_num:
    mx_digit+=1
    mx_num//=10
for i in range(mx_digit):
    c=[0 for _ in a]
    b=c[:]
    for j in a:
        c[(j//10**i)%10]+=1
    for j in range(1,len(a)):
        c[j]+=c[j-1]
    for j in a[::-1]:
        c[(j//10**i)%10]-=1
        b[c[(j//10**i)%10]]=j
    a=b[:]
print(a)