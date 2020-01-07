from random import randrange

def quicksort(list, start, end):
    if start >= end:
        return list

    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]
    list[end], list[pivot_idx] = pivot_element, list[end]

    print(list[start])
    start += 1
    return quicksort(list, start, end)

my_list = [32, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)
