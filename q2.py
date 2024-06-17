from functools import reduce
def multiply_list(my_list):
    result = 1
    for x in my_list:
        result *= x
    return result

sample_list = [8, 2, 3, -1, 7]
output = multiply_list(sample_list)
print(output)  



multiply = lambda x, y: x * y
result = reduce(multiply, sample_list)
print(result)  

