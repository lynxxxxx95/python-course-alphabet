data = [x for x in range(0, 100)]

print(data)

# print(filter(lambda x: x % 2 == 0, data))

new_data = list(filter(lambda x: x % 2 == 0, data))

members = [
    {'age': 43, 'name': 'Denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'Spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'Claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'Homer'}
]
print([x for x in members if x.get('age') > 49])

print(list(filter(lambda x: x.get('age', 0) > 49, members)))




