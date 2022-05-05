# print(200-2)
#
#
# def isPowerOfTwo(self, n: int) -> bool:
#     if n == 0:
#         return True
#
#     return isPowerOfTwo(n / 2)
# print(isPowerOfTwo(16))
def num(n,temp):

    if n==temp:
        return n
    print(temp)
    return num(n,temp+1)
print(num(36,1))