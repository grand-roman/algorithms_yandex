#https://contest.yandex.ru/contest/18285/run-report/38072944/
not_found_index = -1

def binary_search(arr: list, element: int, start: int = 0, stop: int = None):
    stop = stop if stop is not None else len(arr)

    if stop == start:
        return not_found_index

    if stop - start == 1:
        return start if arr[start] == element else not_found_index

    is_sorted = arr[stop - 1] > arr[start]
    middle_index = (start + stop) // 2

    if is_sorted:
        if element < arr[middle_index]:
            return binary_search(arr, element, start=start, stop=middle_index)
        else:
            return binary_search(arr, element, start=middle_index, stop=stop)
    else:
        index_left = binary_search(arr, element, start=start, stop=middle_index)
        index_right = binary_search(arr, element, start=middle_index, stop=stop)

        return index_left if index_left != not_found_index else index_right


col = int(input())
need_find = int(input())
mas = [int(i) for i in input().split(' ')]

print(binary_search(mas,need_find))
