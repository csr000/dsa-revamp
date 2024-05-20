def selection_sort(arr):
    for i in range(len(arr) - 1):
        curr_val = {"idx": i, "val": arr[i]}
        min_val = curr_val
        for j in range(i + 1, len(arr)):
            if arr[j] < min_val["val"]:
                min_val = {"idx": j, "val": arr[j]}

        arr[curr_val["idx"]], arr[min_val["idx"]] = min_val["val"], curr_val["val"]

    return arr


arr = [9, 3, 8, 5, 7, 6, 2, 4, 1, 0]
result = selection_sort(arr)
print(result)

"""
[9,3,8,5,7,6,2,4,1,0]

for i in (arr excluding the first item):
    get the mininum of the array with it's index
    store the current item's value and index

    # these 2 steps can be achieved easily with the help of storing the indexes
    store the minimum val in the current item
    store the current item at where miniumn value was

let the loop complete


"""
