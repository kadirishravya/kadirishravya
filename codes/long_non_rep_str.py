s="ckilbkd"
lis=[]
l=0
for i in range(len(s)):
    try:
        if s[i] not in lis and s[i]!=s[i+1]:
            lis.append(s[i])
            if l<len(lis):
                l=len(lis)
    except:pass
    else:
        print(lis)
        lis=[]
print(l)

#a,l=1
#[],
#b,1
#b,a 2
