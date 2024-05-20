def bubble_sort(arr):
    flag = True

    while flag:
        flag = False

        for i in range(len(arr) - 1):
            l, r = i, i + 1
            if arr[l] > arr[r]:
                arr[l], arr[r] = arr[r], arr[l]  # swapping
                flag = True

    return arr


arr = [9, 3, 8, 5, 7, 6, 2, 4, 1, 0]
result = bubble_sort(arr)
print(result)

"""
[9,3,8,5,7,6,2,4,1,0]
 | |

[3,9,8,5,7,6,2,4,1,0]
   | |

[3,8,9,5,7,6,2,4,1,0]

[3,8,5,7,6,2,4,1,0,9]

swap_helper // help us swap 2 positions

flag = true
# raise flag anytime we swap

l, r = 0, 1

while flag:
    compare if arr[l] > arr[r]:
        arr = swap(arr, l, r)
        flag = true

    if r <= len(arr) - 1:
        l, r = 0, 1
        
    l += 1
    r += 1

iterate backwards

Recursive

"""
