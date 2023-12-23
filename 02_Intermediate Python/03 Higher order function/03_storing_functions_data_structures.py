def square(x):
    return x ** 2


def cube(x):
    return x ** 3


operations = [square, cube]

result_square = operations[0](3)  # 0 meaning index 0(square) and x = 3
result_cube = operations[1](3)    # 1 meaning index 1(cube) and x = 3
print(result_square)
print(result_cube)