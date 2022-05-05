list=[1,2,3,7,1,8,6,9]
lis=[]
for i in range(1,(len(list))-1):
    if list[i]>list[i-1] and list[i]>list[i+1]:
        lis.append(list[i])
print(lis)
print(min(lis))