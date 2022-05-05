def somefun():
    lis=[4,5,0,7,0,0,6]
    #lis=list(map(int,input().split()))
    print(lis)
    lis1=[]
    li2=[]
    for i in lis:
        if i==0:
            li2.append(i)
        else:
            lis1.append(i)
    t=lis1+li2
    #---way1-------------
    print(*t,sep=",")
    #print("1st way----------------")
    print(*t)

    print("--------------check it out-----------ABOVE")
    print("----------way2---------")
    for j in range(len(t)):
        t[j]=str(t[j])
    print(" ".join(t))


    print("----------------3rd way------------")
    print(str(t)[1:-1])
    return

#print(lis1+li2)
print(somefun())