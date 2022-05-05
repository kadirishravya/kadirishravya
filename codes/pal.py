n=121
temp=n

rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n/10
print(rev)
if temp==n:
    print("paalindrome")
else:print("not a palindrome")