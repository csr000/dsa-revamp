def insertion_sort(arr):
    for i in range(1, len(arr)):
        while arr[i] < arr[i - 1] and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


arr = [9, 3, 8, 5, 7, 6, 2, 4, 1, 0]
result = insertion_sort(arr)
print(result)

"""


"""
