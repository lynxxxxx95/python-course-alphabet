import random

our_new_awesome_func = lambda x, y: x * y

print(our_new_awesome_func)

print(type(our_new_awesome_func))

print(our_new_awesome_func(100, 100))


data = [random.randint(-100, 100) for _ in range(10)]
print(data)

print(sum(data))

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


def variant_with_loop(data):
    sum_age = 0
    for member in data:
        sum_age += member.get('age', 0)
    return sum_age

def get_key_from_dict(some_dict):
    return some_dict.get("age")

def with_lambda(data):
    return sum(map(get_key_from_dict, data))


def our_map(function, data):
    for d in data:
        function(d)

# print(variant_with_loop(members))

print(with_lambda(members))

# k = ["hello", "world"]


