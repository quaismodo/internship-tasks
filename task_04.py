def sort_list(list):
    if list:
        min_num = min(list)
        max_num = max(list)
        for i in range(len(list)):
            if list[i] == min_num:
                list[i] = max_num
            elif list[i] == max_num:
                list[i] = min_num
        list.append(min_num)
    return list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))
