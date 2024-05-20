def binary_search(arr, target):
    size = len(arr) - 1
    l, r = 0, size

    while l <= r:
        mid = (l + r) // 2  # midpoint

        print("target", target, "left", arr[l], "midpoint", arr[mid], "right", arr[r])

        if target == arr[mid]:
            print("target == center")
            return True

        if target > arr[mid]:
            print("go right")
            l = mid + 1

        if target < arr[mid]:
            print("go left")
            r = mid - 1

    return False


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = binary_search(arr, target)
print(result)

"""
set l and r point
get size of the array = 9
get middle value = 5

if target == middle number:
    return the middle number as found
    
if target > middle:
    move the l to middle + 1
else:
    vice versa
"""
