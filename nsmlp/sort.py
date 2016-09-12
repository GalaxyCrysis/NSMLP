
#sorts the array with bubble sort algorithm
def bubbleSort(x):
    for i in range(0, len(x)):
        for j in range(0, len(x) - 1):
            if x[j] > x[j + 1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
    return x

#sorts the array or list with quicksort algorithm(in place)
class QuickSort():
    def sort(self,x):
        self.qsort(x)
        return list(reversed(x))

    def qsort(self, x, left=0, right=None):
        if right is None:
            right = len(x) - 1
        if left >= right:
            return
        pivot = self.partition(x, left, right)
        self.qsort(x, left, pivot - 1)
        self.qsort(x, pivot + 1, right)

    def partition(self, x, left, right):
        pivot = left
        for i in range(left + 1, right + 1):
            if x[i] >= x[left]:
                pivot += 1
                x[i], x[pivot] = x[pivot], x[i]
        x[pivot], x[left] = x[left], x[pivot]
        return pivot

#sorts the array or list by insertionsort
def insertionSort(x):
    for i in range(1,len(x)):
        j = i
        while j > 0 and x[j] < x[j - 1]:
            x[j], x[j - 1] = x[j - 1], x[j]
            j = j - 1
    return x
    
#sorts the array or list by gnome sort algorithm and returns the array/list
def gnomeSort(x):#
    i = 0
    while i < len(x):
        if i and x[i] < x[i-1]:
            x[i],x[i-1] = x[i-1],x[i]
            i = i-1
        else:
            i = i+1
    return x
#sorts the array or list by combsort algorithm and returns it
def combSort(x):
    n = len(x)
    gap = n
    swapped = True
    while swapped == 1:
        gap = int(gap/1.3)
        for i in range(0, n-gap):
            if x[i] > x[i+gap]:
                x[i],x[i+gap]=x[i+gap],x[i]
                swapped=True
        if gap <=1:
            break
    return x
    
#sorts the list or array with merge sort algorithm
def mergeSort(x):
    if len(x) <= 1:
        return
    mid = int(len(x)/2)
    left = x[:mid]
    right = x[mid:]
    #now split again both parts
    mergeSort(left)
    mergeSort(right)

    i,j,n = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            x[n] = left[i]
            i = i+1
        else:
            x[n] = right[j]
            j = j+1
        n = n+1
    while i < len(left):
        x[n] = left[i]
        i = i+1
        n = n+1
    while j < len(right):
        x[n] = right[j]
        j = j+1
        n = n+1

    return x












