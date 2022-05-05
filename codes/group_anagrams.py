# d = {}
strs=["eat","tea","tan","ate","nat","bat"]
# print(sorted(strs))
# for w in sorted(strs):
#     key = tuple(sorted(w))
#     print(key)
#     d[key] = d.get(key, []) + [w]
#     print(d)
#     print(d[key])
# print(d)
# print(d.values())



ga = {}

for i in strs:
    y = "".join(sorted(i))
    if y not in ga.keys():
        ga[y] = [i]
        print(ga)
    else:
        ga[y].append(i)
print(ga)

print([ga[i] for i in ga.keys()])