a="customer"
b="currency"
k=3
cnt=0
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]!=b[i]:
            cnt+=1
    if cnt==0:
        print(1)
    elif cnt<k:
        print(2)
    elif cnt==k:
        print(3)
    elif cnt>k:
        print(4)
