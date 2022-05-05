lis=[1,2,3,1,1,3]
dic={}
for i in range(len(lis)):
    if lis[i] not in dic:
        dic[lis[i]]=lis.count(lis[i])
print(dic)
