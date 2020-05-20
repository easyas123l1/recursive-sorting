# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    first = len(arrA)
    second = len(arrB)
    elements = first + second
    merged_arr = [0] * elements
    i = 0
    j = 0
    while i < first and j < second:
        # check if location on arrA is smaller then arrB
        if arrA[i] <= arrB[j]:
            # insert data into merged array we know what index to add by adding i+j
            merged_arr[i+j] = arrA[i]
            i += 1
            if i == first:
                # i believe this gives us best runtime
                while j < second:
                    merged_arr[i+j] = arrB[j]
                    j += 1
        # else case for checking smaller value
        else:
            # insert data into merged array we know what index to add by adding i+j
            merged_arr[i+j] = arrB[j]
            j += 1
            if j == second:
                # i believe this gives us best runtime
                while i < first:
                    merged_arr[i+j] = arrA[i]
                    i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
