import string

data = {k: v for v, k in enumerate(string.ascii_lowercase, start=1)}

data_keys = [f"Key is : {x}; Value is {y}" for x, y in enumerate(data.items())]
data_keys_1 = [f"Key is : {x}; Value is {y}" for x, y in data.items()]
data_keys_2 = [f"Key is : {x}; Value is {y}" for x, y, c in enumerate(data.items())]

print(data_keys)
print(type(data))
print(data)
