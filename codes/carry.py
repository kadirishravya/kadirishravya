carry = 0
res = []
s = ''
num1 = "11111"
num2 = "123"

l = max(len(num1), len(num2))
print(l)

for i in range(l - 1, -1, -1):
    su = 0
    su += int(num1[i]) + int(num2[i]) + carry
    print(su)
    carry, res = su // 10, res.append(su % 10)


res = res[::-1]
print(res)
s = ''.join(res)

print(s)