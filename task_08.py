from functools import reduce


def multiply_numbers(inputs=None):
    total = None
    if inputs:
        if any(map(str.isdigit, str(inputs))):
            total = 1
            num_list = map(int, filter(str.isdigit, str(inputs)))
            for num in num_list:
                total *= num

    return total


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))


# Второй вариант, с использованием функции reduce()
def multiply_numbers(inputs=None):
    total = None
    if inputs:
        def multiply(x, y):
            return x * y

        if any(map(str.isdigit, str(inputs))):
            total = reduce(multiply, map(int, filter(str.isdigit, str(inputs))))

    return total
