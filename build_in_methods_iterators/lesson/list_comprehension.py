import string

list_1 = [x for x in string.ascii_lowercase]
list_2 = [1 for x in string.ascii_lowercase]

list_3 = [x for x in range(0, 100) if x % 2 == 0]

list_4 = [x if x % 2 == 0 else -1 for x in range(0, 100)]

print(list_1)
print(list_2)
print(list_3)
print(list_4)
