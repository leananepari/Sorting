# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    index = 0
    while index < len(arrA):
      if len(arrB) > 0:
        if arrA[index] < arrB[0]:
          merged_arr.append(arrA[index])
        else:
          merged_arr.append(arrB[0])
          del arrB[0]
          index = index - 1
      else:
        merged_arr.append(arrA[index])
        
      index = index + 1
    
    if len(arrB) > 0:
      merged_arr = merged_arr + arrB

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
      mid = len(arr)//2 
      left = arr[:mid] 
      right = arr[mid:] 

      merge_sort(left) 
      merge_sort(right) 

      sortedSub = merge(left, right)

      for i in range(len(sortedSub)):
        arr[i] = sortedSub[i]

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr



print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))