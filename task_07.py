def combine_anagrams(words_array):
    list_now = [[''.join(sorted(i.lower())), i] for i in words_array]
    dict_sort = {}
    for i in range(len(list_now)):
        if list_now[i][0] in dict_sort:
            print(list_now[i][1])
            dict_sort[list_now[i][0]].append(list_now[i][1])
        else:
            dict_sort[list_now[i][0]] = [list_now[i][1]]

    return list(dict_sort.values())


print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
                        "creams", "scream"]))
