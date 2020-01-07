from random import randrange

def quicksort(list, start, end):
    if start >= end:
        return list

    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    lesser_than_pointer = start

    for idx in range(start, end):
        if list[idx] < pivot_element:
            list[idx], list[lesser_than_pointer] = list[lesser_than_pointer], list[idx]
            lesser_than_pointer += 1

    list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]

    print(list[start])
    start += 1
    return quicksort(list, start, end)

my_list = [42, 103, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)
