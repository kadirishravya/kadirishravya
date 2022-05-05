lis=[1,2,3,2,3,3,4,3]
try:
    for i in range(len(lis)):
        for j in range(len(lis)):
            if i<j and lis[i]==lis[j]:
                lis.remove(lis[j])
except:pass
print(lis)
