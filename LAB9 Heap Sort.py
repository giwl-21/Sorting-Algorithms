#LAB 9
#Due Date: 04/11/2020, 11:59PM EST
########################################
#                                      
# Name: Muhsin Wahi-Anwar
# Collaboration Statement:             
# I worked alone and used classroom materials.
########################################
import math

class MaxPriorityQueue:
    def __init__(self):
        self.heap=[]

    def __str__(self):
        return f'{self.heap}'

    __repr__=__str__

    def __len__(self):
        # YOUR CODE STARTS HERE
        #the heap list length tells how many values are present
        return len(self.heap)


    def parent(self,index):
        # YOUR CODE STARTS HERE
        # inputted heap index is +1 of list index
        # uses floor division because the parent index is half of the child
        parentIndex = index//2
        if parentIndex == 0:
            return None
        
        return self.heap[parentIndex-1]
        

    def leftChild(self,index):
        # YOUR CODE STARTS HERE
        # multiplies given by two and reurns value at that index
        lcIndex = index * 2
        if lcIndex > len(self):
            return None
        return self.heap[lcIndex-1]

    def rightChild(self,index):
        # YOUR CODE STARTS HERE
        # multiplies given by two, adds one, and returns value at that index
        rcIndex = index * 2 + 1
        if rcIndex > len(self):
            return None
        return self.heap[rcIndex - 1]
 
        

    def insert(self,x):
        # YOUR CODE STARTS HERE
        # Node means heap index, index means list index
        self.heap.append(x)
        currentNode = len(self)
        while self.isNum(self.parent(currentNode)) and (x > self.parent(currentNode)):
            currentNode = self.replaceParent(currentNode)
            

    def deleteMax(self): 
        if len(self)==0:
            return None        
        elif len(self)==1:
            outMax=self.heap[0]
            self.heap=[]
            return outMax

        # YOUR CODE STARTS HERE
        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        #now the heap has moved the smallest value to the root node
        currentNode = 1
        while self.isNum(self.leftChild(currentNode)):
            largeChildNode = currentNode * 2
            if self.isNum(self.rightChild(currentNode)) and self.rightChild(currentNode) > self.leftChild(currentNode):
                #when the right child exists and is larger than left child
                largeChildNode = currentNode * 2 + 1
            else:
                #if the left child exists or is larger than right
                largeChildNode = currentNode * 2

            #now we have the largest child node, we can compare it to the current node
            if self.heap[largeChildNode - 1] > self.heap[currentNode - 1]:
                #if the child is larger than current node, we will switch them
                childValue=self.heap[largeChildNode - 1]
                self.heap[largeChildNode - 1]=self.heap[currentNode - 1]
                self.heap[currentNode - 1]=childValue
                currentNode = largeChildNode
            else:
                # we dont need to iterate anymore if they are equal
                break
        return maximum

    def replaceParent(self, node):
        #replaces the parent's value with the value of the given index
        # returns the parent's heap index (list index - 1)
        # if the parents node doesnt exist return none
        pNode = node // 2
        if pNode == 0:
            return None
        
        value = self.heap[node-1]
        self.heap[node-1] = self.heap[pNode-1]
        self.heap[pNode - 1] = value
        return pNode


    def isNum(self, value):
        try:
            float(value)
            return True
        except:
            return False



def isNum(value):
    try:
        float(value)
        return True
    except:
        return False

def heapSort(numList):
    '''
       >>> heapSort([9,7,4,1,2,4,8,7,0,-1])
       [-1, 0, 1, 2, 4, 4, 7, 7, 8, 9]
    '''
    sortHeap = MaxPriorityQueue()
    # -- YOUR CODE STARTS HERE
    #first we fill the heap
    #then we will remove maximums one by one until the heap is empty
    # and add those maximums to the beginning of a list to make the list ascending
    for i in numList:
        sortHeap.insert(i)
    descending = []
    
    while len(sortHeap) > 0:
        descending.append(sortHeap.deleteMax())

    descending.reverse()
    # it is now ascending
    return descending
        

    
        
