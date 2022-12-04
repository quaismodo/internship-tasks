def connect_dict(dict1, dict2):
    def get_min_dict(dict_x, dict_y):
        return dict_x if sum(dict_x.values()) <= sum(dict_y.values()) else dict_y

    def get_max_dict(dict_x, dict_y):
        return dict_x if sum(dict_x.values()) > sum(dict_y.values()) else dict_y

    min_dict = get_min_dict(dict1, dict2)
    max_dict = get_max_dict(dict1, dict2)

    key_matches = dict1.keys() & dict2.keys()

    for key in key_matches:
        del min_dict[key]

    max_dict.update(min_dict)

    max_dict = filter(lambda item: item[1] >= 10, max_dict.items())
    sorted_dict = dict(sorted(max_dict, key=lambda x: x[1]))

    return sorted_dict


print(connect_dict({"a": 2, "b": 12}, {"c": 11, "e": 5}))
print(connect_dict({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))
print(connect_dict({"a": 14, "b": 12}, {"c": 11, "a": 15}))
