my_array = [3, 8, 2, 10, 5]
sum = 0 # here we can use sum() as well
len_array = 0

for element in my_array:
    sum += element
    len_array += 1

average = sum/len(my_array) # using built in len()
# or
averageN = sum/len_array # using for loop
print(sum)
print(average)
print(averageN)