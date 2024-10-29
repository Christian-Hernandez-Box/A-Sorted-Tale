import random

def bubble_sort(arr, comparison_function):
    swaps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if comparison_function(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    print(f"Bubble sort: There were {swaps} swaps")
    return arr

def quicksort(arr, start, end, comparison_function):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1)
    pivot_element = arr[pivot_idx]
    arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
    less_than_pointer = start
    for i in range(start, end):
        if comparison_function(pivot_element, arr[i]):
            arr[i], arr[less_than_pointer] = arr[less_than_pointer], arr[i]
            less_than_pointer += 1
    arr[end], arr[less_than_pointer] = arr[less_than_pointer], arr[end]
    quicksort(arr, start, less_than_pointer - 1, comparison_function)
    quicksort(arr, less_than_pointer + 1, end, comparison_function)