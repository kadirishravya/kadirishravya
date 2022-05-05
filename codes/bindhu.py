st="434256810"
l=len(st)-1
lis=[]
su=0
try:
    for i in range((len(st)//2)):
        a=int(st[i])+int(st[l-i])
        lis.append(a)
except:pass
str2=''
for i in range(len(lis)):
    str2+=str(lis[i])
if len(st)%2==0:
    print(str2)
else:
    str2+=st[len(st)//2]
    print(str2)

# else:
#     for i in range
