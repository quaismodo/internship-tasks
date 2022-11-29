from functools import reduce


def multiply_numbers(inputs=None):
    inputs_str = str(inputs)
    result = None
    if any(map(str.isdigit, inputs_str)):
        num_list = map(int, filter(str.isdigit, inputs_str))
        result = 1
        for i in num_list:
            result *= i

    return result


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))


# Второй вариант, с использованием фукнции reduce()
def multiply_numbers(inputs=None):
    def multiply(x, y):
        return x * y

    inputs_str = str(inputs)
    result = None
    if any(map(str.isdigit, inputs_str)):
        result = reduce(multiply, map(int, filter(str.isdigit, inputs_str)))

    return result
