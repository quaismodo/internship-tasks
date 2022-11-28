def coincidence(elements=False, num_range=False):
    result_list = list()
    # создаем список final_list куда будут добавляться конечные значения
    if elements and num_range:
        # проверяем присутствуют ли аргументы функции
        num_list = list(num_range)
        # преобразуем функцию range в список

        for el in elements:
            # перебираем значения элементов списка

            if type(el) in [int, float]:
                if num_list[0] <= el <= num_list[-1]:
                    result_list.append(el)

    return result_list


number_range = range(1, 4)
el_list = [None, 1, 'foo', 4, 2, 2.5]

print(coincidence(el_list, number_range))
