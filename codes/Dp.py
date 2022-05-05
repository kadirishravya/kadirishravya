def Dp(lis_m):
    lis=[1]*len(lis_m)
    try:
        for i in range(1,len(lis)):
            sub_problems=[lis[k] for k in range(i) if lis_m[k]<lis_m[i]]
            print(sub_problems)
            lis[i]=1+max(sub_problems)
    except:pass
    return max(lis)
se=[5,2,8,6,3,6,9,5]
print(Dp(se))