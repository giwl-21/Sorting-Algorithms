# Muhsin Wahi-Anwar
# Sorting Algorithms
# Merge Sort
# 11/6/2020

def merge(list1, list2):
    '''
    >>> x = [0, 4, 5, 6, 7, 20, 24, 40]
    >>> y = [2, 4, 4, 5, 15]
    >>> merge(x, y)
    [0, 2, 4, 4, 4, 5, 5, 6, 7, 15, 20, 24, 40]
    '''
    # takes two input lists that are already sorted ascending
    # and puts them together as a sorted list
    listOut = []
    a = 0
    b = 0
    
    while (a < len(list1) and b < len(list2)):
        # put smaller value in new list and travel up
        if list1[a] < list2[b]:
            listOut.append(list1[a])
            a += 1
        elif list1[a] >= list2[b]:
            listOut.append(list2[b])
            b += 1

    #now deal with remaining items
    if (a == len(list1)):
        # list2 has unread elements
        return listOut + list2[b:]
    elif (b == len(list2)):
        return listOut + list1[a:]

def mergeSort(listIn):
    '''
        >>> x = [5, 3, 2, 4, 7, 8, 9, 3, 2]
        >>> mergeSort(x)
        [2, 2, 3, 3, 4, 5, 7, 8, 9]
    '''
    if len(listIn) == 1:
        # Inherently Sorted 
        return listIn
    else:
        # Splitting and then putting together
        middle = len(listIn)//2
        return merge(mergeSort(listIn[:middle]), mergeSort(listIn[middle:]))
