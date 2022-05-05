# Python3 code to demonstrate
# finding None indices in list
# using list comprehension + enumerate

test_list = [1, None, 4, None, None, 5]
print("The original list : " + str(test_list))

res = [i for i in range(len(test_list)) if test_list[i] == None]
print("The None indices list is : " + str(res))
