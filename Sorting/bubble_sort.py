###  .............Selection Sort ...................

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [2, 5, 3, 4, 8, 7]
selection_sort(arr)
print(arr)

#### ..................Bubble sort ...................

def bubble_sort(arr):
    n = len(arr)
    for i in range(1,n):     # from i (1-n) or j (0 - n-i-1)

        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [12,8,15,7,5,2,1,18]
bubble_sort(arr)
print(arr)

### ................Insertion Sort...............

def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        for j in range(n):
            if arr[j]< arr[j-1]:
                arr[j]=



