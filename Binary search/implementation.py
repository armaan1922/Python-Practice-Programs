def binary_search(arr, key):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2

    while start <= end:
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            end = mid - 1
        mid = (start+end)//2
    return -1

my_list = [1,3,4,5,7,8,9,12,14,22]

print(binary_search(my_list, 12))

