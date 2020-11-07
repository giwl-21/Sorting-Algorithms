#  Muhsin Wahi-Anwar
#  10-28-2020
#  Sorting Algorithms

def quickSort(inputList):
    '''
        >>> x = [5, 3, 2, 4, 7, 8, 9, 3, 2]
        >>> quickSort(x)
        [2, 2, 3, 3, 4, 5, 7, 8, 9]
    '''
    # This quicksort will use the rightmost value as a pivot
    # It will have a left pointer and a right pointer
    # The left and right pointers will converge, switching values so the
    # left side will have numbers less than the pivot while the right side
    # will have numbers greater than the pivot.
    
    if len(inputList) <= 1:
        # BASE CASE
        return inputList
    
    pivot = len(inputList) - 1
    left = 0
    right = len(inputList) - 1 # same pos as pivot is fine
    while (right > left):
        # conditions for moving pointers and switching values
        if (inputList[left] <= inputList[pivot]):
            left += 1
        elif (inputList[right] >= inputList[pivot]):
            right -= 1
        else:
            inputList[right], inputList[left] = inputList[left], inputList[right]

    # now right == left so we switch then split and recurse
    inputList[left], inputList[pivot] = inputList[pivot], inputList[left]
    return quickSort(inputList[:left]) + quickSort(inputList[left:])
