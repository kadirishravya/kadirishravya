# s="aababa"
# s=list(s)
# cnt=0
# for i in range(len(s)):
#     if s[i]=="a":
#         cnt+=1
#         if cnt<2:
#             s.insert(i,"a")

# sm=1000000000000000000000000000000
# for i in range(len(lis)+1):
#     try:
#         if sm>lis[i]:
#             sm=lis[i]
#     except:pass
# lis.remove(sm)
# try:
#     for i in range(len(lis)):
#         lis.remove(sm)
# except:pass
# #print(len(lis),lis)
# sm=1000000000000000000000000000000
# for i in range(len(lis)+1):
#     try:
#         if sm>lis[i]:
#             sm=lis[i]
#     except:pass
# print(lis)
# print(sm)
'''
val=3
import math
lis=[1,2,3,4]
p = math.prod(lis)
pos=0
ex=lis
lis1=[]
import math
try:
    for i in range(len(lis)):
        lis[i] = p//lis[i]
        ex.remove(ex[i])
        print(ex)
        pro=math.prod(ex)
        lis1.append(pro)
        pro=1
        ex = lis
        print(lis)
except:pass
print(lis)'''
s = 'abaababaaaabaaa'
l = len(s)
temp = 0
count = 0
i = 0
while(i < l):
    if s[i] == 'a':
        count += 1
    else:
        if count != 2:
            temp += 1
        #temp += count
        count = 0
    i += 1
if count > 0 and count != 2:
    temp += 1
print(temp)
# for i in range(len(s)):
#     if s[i]=="a":
#         count+=1
#     else:
#         if count!=2:
#             temp+=1
#         count=0
#     i+=1


