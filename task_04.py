def sort_list(num_list):
    if num_list:
        min_num = min(num_list)
        max_num = max(num_list)

        for i in range(len(num_list)):
            if num_list[i] == min_num:
                num_list[i] = max_num
            elif num_list[i] == max_num:
                num_list[i] = min_num
        num_list.append(min_num)
    return num_list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1]))
