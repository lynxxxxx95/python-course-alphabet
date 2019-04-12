import string

list_1 = [x for x in string.ascii_lowercase]
list_2 = [1 for x in string.ascii_lowercase]

list_3 = list(range(0, 100, 2))

print(list_1)
print(list_2)
print(list_3)