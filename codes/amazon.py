# n=int(input())
# n=str(n)
# nrev=n[::-1]
# if n==nrev:
#     print("they are palindrome")
# else:print("the given no is not a palindrome")
n=input("enter a no")
lis=list(n)
su=0
for i in range(len(lis)):
    su+=int(lis[i])
print("the sum of given no is")
print(su)