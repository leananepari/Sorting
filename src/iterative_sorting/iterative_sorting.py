# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
          if arr[j] < arr[smallest_index]:
            smallest_index = j   



        # TO-DO: swap
        saveSmallest = arr[smallest_index]
        arr[smallest_index] = arr[cur_index] 
        arr[cur_index] = saveSmallest
    
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
  swaps = 0
  repeat = True

  while repeat:
    for i in range(len(arr) -1):
      if arr[i + 1] < arr[i]:
        saveVal = arr[i]
        arr[i] = arr[i+1] 
        arr[i+1] = saveVal
        swaps = swaps + 1
    if swaps == 0:
      break
    else:
      swaps = 0

  return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr