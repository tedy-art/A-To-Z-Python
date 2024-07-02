def create_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


multiple_by_2 = create_multiplier(2)
result = multiple_by_2(5)
print(multiple_by_2)
print(result)
