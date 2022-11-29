def coincidence(elements=False, num_range=False):
    result_list = list()
    if elements and num_range:
        num_list = list(num_range)

        for el in elements:

            if type(el) in [int, float]:
                if num_list[0] <= el <= num_list[-1]:
                    result_list.append(el)

    return result_list


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))
