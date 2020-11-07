#  Muhsin Wahi-Anwar
#  10-28-2020
#  Sorting Algorithms

def insertionSort(inputList):
    '''
        >>> x = [5, 3, 2, 4, 7, 8, 9, 3, 2]
        >>> insertionSort(x)
        [2, 2, 3, 3, 4, 5, 7, 8, 9]
    '''
    # insertion sort uses a sorted section at teh begginign
    # and a unsorted section after the beginning,
    # individually inserting new unsortedvalues in the sorted part
    for i in range(1, len(inputList)):
        # i is the section divider
        # and it will start at number two
        for p in range(i):
            if inputList[p] > inputList[i]:
                inputList.insert(p, inputList.pop(i))

    return inputList
