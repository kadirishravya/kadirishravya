a="zzacaabba"
a="zzxzzzdccdddddfgfgfghujujh"
cnt=0
#try:
for i in range(len(a)):
    for j in range(len(a)+1):
        if i<j:
            s=a[i:j]
            print(s)
            if s==s[::-1] and len(s)>cnt:
                cnt=len(s)
                ab=s
#except:pass
print(cnt,ab)
