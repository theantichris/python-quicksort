from random import randrange, shuffle

def quicksort(list, start, end):
    if start >= end:
        return list

    # select random element to be the pivot
    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]

    # swap the random element with the last element in the list
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements that should be to the left (lesser than) the pivot
    lesser_than_pointer = start

    for idx in range(start, end):
        # if the element is out of place
        if list[idx] < pivot_element:
            # swap the element to the right-most portion of the lesser elements
            list[idx], list[lesser_than_pointer] = list[lesser_than_pointer], list[idx]
            # increment since we have 1 more lesser than element
            lesser_than_pointer += 1

    # move the pivot to the right-most portion of the lesser elemtents
    list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]

    # sort the left and right lists
    quicksort(list, start, lesser_than_pointer - 1)
    quicksort(list, lesser_than_pointer + 1, end)

unsorted_list = [3, 7, 12, 24, 36, 42]
shuffle(unsorted_list)
print(unsorted_list)

quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)
