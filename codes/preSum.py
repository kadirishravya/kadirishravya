arr=[10, 20, 10, 5, 15]
sum=0
presum=[]
for i in arr:
    sum+=i
    presum.append(sum)
print(presum)