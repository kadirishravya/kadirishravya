arr=[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
lis=[[1],[1,1]]
k=0
while k<len(arr):
    for i in range(len(lis)):
        lis2=lis[i]
        r=[1]
        try:
            for j in range(len(lis2)):
                s=lis2[j]+lis2[j+1]
                print(s)
                r.append(s)
                print(r)
            r.append(1)
            print(r)
            lis.append(r)
            print(lis)
            r=[]
        except:pass
    k+=1

print(lis)

