def max_odd(array):
    num_list = list()
    for i in array:
        if type(i) in [float, int] and i % 2 != 0:
            num_list.append(int(i))

    return max(num_list) if num_list else None


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))
