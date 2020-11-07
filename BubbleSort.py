# Muhsin Wahi-Anwar
# 10-28-2020
# Sorting Algorithms

def bubbleSort(inputList):
    '''
        >>> x = [5, 3, 2, 4, 7, 8, 9, 3, 2]
        >>> bubbleSort(x)
        [2, 2, 3, 3, 4, 5, 7, 8, 9]
    '''
    # loops entirely, switches values until it can verify everything is sorted
    entirelySorted = False
    while entirelySorted == False:
        # entirelySorted is kept true only if we go through an entire iteration without swapping
        entirelySorted = True
        for i in range(len(inputList)-1):
            if inputList[i] > inputList [i+1]:
                inputList.insert(i, inputList.pop(i+1))
                entirelySorted = False

    return inputList
