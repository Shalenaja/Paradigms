# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


# Выполнено в процедурной парадигме программирования для удобства восприятия при нескольких вызовах программы.
# Внутри функции императивный подход, для подробного описания действий.


def binary_search(list_num, to_search):
    first_index = 0
    last_index = len(list_num) - 1
    mid_index = (first_index + last_index) // 2
    mid_element = list_num[mid_index]

    is_found = True
    while is_found:
        if first_index == last_index:
            if mid_element != to_search:
                is_found = False
                return -1
            elif mid_element == to_search:
                return f"element {mid_element} - index {mid_index}"
        elif mid_element > to_search:
            last_index = mid_index - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"element {mid_element} - index {mid_index}"
        elif mid_element < to_search:
            first_index = mid_index + 1
            last_index = len(list_num) - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"element {mid_element} - index {mid_index}"

list_number = [1 , 3 , 4 , 7 , 8 , 10 , 13 , 14]
print(binary_search(list_number, 10))
print(binary_search(list_number, 2))