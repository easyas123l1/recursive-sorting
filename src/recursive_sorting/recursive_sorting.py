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
    # $%$Start
    # based on C solution at: https://www.geeksforgeeks.org/in-place-merge-sort/
    start2 = mid + 1
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return arr
    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:
        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2
            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
    # $%$End
    return arr


def merge_sort_in_place(arr, l, r):
    # $%$Start
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) / 2
        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)
    # $%$End
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
