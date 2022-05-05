lis=[]
for i in range(9):
    n=int(input())
    lis.append(n)
t1=(lis[0]+lis[3]+lis[6])/3
t2=(lis[1]+lis[4]+lis[7])/3
t3=(lis[2]+lis[5]+lis[8])/3
print(max([t1,t2,t3]))
print(t1,t2,t3)