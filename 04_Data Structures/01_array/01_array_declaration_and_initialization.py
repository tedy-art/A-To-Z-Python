# declaration of an array
my_array = [1, 2, 3, 4, 5]

# initialization of an array with default and specific values

# default values
default_values = [0 for _ in range(5)]
print(f"default value array : {default_values}")

# default using `*`
default_values = [1]*5
print(f"default value array using `*` : {default_values}")
print()
# specific values
specific_values = [1, 4, 6, 8, 10]
print(f"specific value array : {specific_values}")

# default using `*`
specific_values = [0]*5
print(f"specific value array using `*` : {specific_values}")
