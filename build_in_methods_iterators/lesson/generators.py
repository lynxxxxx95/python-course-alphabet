def interger_values():
    i = 0
    while True:
        yield i
        i += 1
        yield str(i)

our_gen = interger_values()

# print(next(our_gen))

for i in range(100):
    print(id(our_gen))
    step_value = next(our_gen)
    print(step_value)