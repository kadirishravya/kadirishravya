arr=[3,4,5]
st="PNP"
lis=[]
for i in range(len(arr)):
    if st[i]=="P" and arr[i]<0:
        arr[i]=-1*(arr[i])
    if st[i]=="P" and arr[i]>0:
        arr[i]=arr[i]
    if st[i]=="N" and arr[i]<0:
        arr[i]=1*arr[i]
    if st[i]=="N" and arr[i]>0:
        arr[i]=-1*arr[i]
print(sum(arr)*100)
