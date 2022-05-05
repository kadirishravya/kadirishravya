# n=9
# n3=3
# for i in range(1,n):
#     if n3==n:
#         print(True)
#     n3*=3
# nn=n3
# def ss(n3):
#     if n==n3:
#         return True
#     return 3*ss(n3)
# print(ss(n3))


def isPowerOfThree(n3,n):
    if n == 1:
        return True

    if n3 == n:
        return True
    else:
        n3=n3 * isPowerOfThree(n3,n)
print(isPowerOfThree(3,9))