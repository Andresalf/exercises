def has_all_unique_chars_by_sort(array):
    arr_list = list(array)
    arr_list.sort()

    if len(arr_list) < 2:
        return True

    n = len(arr_list)
    for i in range(n):
        if i < n - 1 and arr_list[i] == arr_list[i+1]:
            return False

    return True


def has_all_unique_chars_by_hash(array):
    table = set()
    for c in array:
        if c in table:
            return False
        table.add(c)

    return True

arr = "linhgbi"
#print(has_all_unique_chars_by_sort(arr))
print(has_all_unique_chars_by_hash(arr))