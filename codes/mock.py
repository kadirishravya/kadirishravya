s_main="abcdefghijklmnopqrstuvwxyz"
string="All The Best"
ac=""
k=2
# for i in range(len(string)):
#     for j in range(len(s_main)):
#         if string[i].isupper() and string[i].lower()==s_main[j]:
#             ac+=s_main[i+1].upper()
#         elif string[i].lower()==s_main[j]:
#             ac+=s_main[i+1]
#         else:print("#")
# print(ac)
for i in range(len(string)):
    if string[i].isupper():
        z=s_main.index(string[i].lower())
        ac+=s_main[z+k].upper()
    elif string[i]==" ":
        ac+=" "
    elif string[i].islower():
        z=s_main.index(string[i])
        ac+=s_main[z+k].lower()
    else:print("#")
print(ac)
