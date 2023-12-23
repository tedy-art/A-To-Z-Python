def apply_operation(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


result_add = apply_operation(add, 2, 3)
result_multi = apply_operation(multiply, 2, 3)
print(result_add)
print(result_multi)
