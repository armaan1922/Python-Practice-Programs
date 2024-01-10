##            .... NO. of times a list is ROTATED ........

# def count_rotations(arr):
#     start = 0
#     end = len(arr)-1
#     mid = (start + end)//2
#
#     while start <= end:
#         if arr[mid]>0 and arr[mid]<arr[mid-1]:
#             return mid
#         elif arr[mid] < arr[end]:
#             end = mid-1
#         elif arr[mid] > arr[end]:
#             start = mid+1
#         mid = (start+end)//2
#     return 0
#
# my_list = [8, 9, 2, 3, 4, 7]
#
# print(count_rotations(my_list))

                                  # ... Peak elememnt in an array.....
# def peak_element(arr):
#     start = 0
#     end = len(arr)-1
#     mid = (start+end)//2
#
#     while start < end:
#         if arr[mid] < arr[mid+1]:
#             start = mid+1
#         else:
#             end = mid
#         mid = (start+end)//2
#     return arr[start]  # returns value of peak index .... if peak index is req then return 'start' only
#
# my_list=[ 3,4,5,6,4,1]
# print(peak_element(my_list))


#           .........................First AND Last OCCURENCE OF AN ELEMENT ............

#
# def firstOcc(arr, key):
#     start = 0
#     end = len(arr)-1
#     mid = (start+end)//2
#     ans = -1
#     while start <= end:
#         if arr[mid] == key:
#             ans = mid
#             end = mid-1
#         elif arr[mid] < key:
#             start = mid+1
#         else:
#             end = mid-1
#         mid = (start + end) // 2
#
#     return ans
#
# def lastOcc(arr, key):
#     start = 0
#     end = len(arr)-1
#     mid = (start+end)//2
#     ans = -1
#     while start <= end:
#         if arr[mid] == key:
#             ans = mid
#             start = mid+1
#         elif arr[mid] < key:
#             start = mid+1
#         else:
#             end = mid-1
#         mid = (start + end) // 2
#
#     return ans
#
# my_list= [1,2,3,4,4,4,4,4,5,5,6]
#
# print("First occurence of the number is at index : ",firstOcc(my_list, 4))
# print("Last occurence of the number is at index :",lastOcc(my_list,4))
#

