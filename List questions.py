
#                  ..... prime number ......

# n = int(input("Enter the number ->"))
#
# if n%2 != 0:
#     print("Prime number!!")
# else:
#     print("Not prime!!")


#     ............... Interchange first nd last element in list...........
#
# arr = list()
# n = int(input("Enter the total number of elements"))
#
# for i in range(n):
#     a = int(input("enter no."))
#     arr.append(a)
# print("Array before swapping",arr)
#
#
# temp = arr[0]
# arr[0]= arr[n-1]
# arr[n-1] = temp
#
# print("Array after swapping",arr)


# ........... interchange any two number.......

# arr = []
# n = int(input("Enter the total number of elements->"))
# for i in range(n):
#     a = int(input("enter no."))
#     arr.append(a)
# print("your array -->",arr)
# n1 = int(input("Enter 1st ele. you want to interchange"))
# n2 = int(input("Enter the 2nd ele. you wana interchange"))
#
# temp = arr[n1-1]
# arr[n1-1] = arr[n2-1]
# arr[n2-1]= temp
# print("Array after swapping is",arr)


#   ......... reverse a array ..........

# arr =[]
#
# n = int(input("Enter the total number of elements->"))
# for i in range(n):
#     a = int(input("enter no."))
#     arr.append(a)
# print("Your array-> ", arr)
#
# print("Reversed array is -> ", arr[:: -1])


#     .......... Sum of numbers ........

# arr = list()
# n = int(input("Enter the total number of elements->"))
# for i in range(n):
#     a = int(input("enter no."))
#     arr.append(a)
# print("Your array-> ", arr)
#
# sum = 0
# for j in arr:
#     sum += j
#
# print("Sum is -> ", sum)
#

# ............... Count Occurrences of element ..........

# arr = list()
# n = int(input("Enter the total number of elements->"))
# for i in range(n):
#     a = int(input("enter no."))
#     arr.append(a)
# print("Your array-> ", arr)
#
# num = int(input("Enter the number you want to count"))
# count = 0
# for j in arr:
#     if num == j:
#         count += 1
# print(count)

# ............. Largest number in list ..........

#
# arr = list()
# n = int(input("Enter the total number of elements->"))
# for i in range(n):
#     a = int(input("enter no."))
#     arr.append(a)
# print("Your array-> ", arr)
#
# min = -1
# for j in arr:
#     if j>min:
#         min = j
#
# print("Largest number is -> ", min)


# ............... Second largest number ...............
# arr = list()
# n = int(input("Enter the total number of elements"))
#
# for i in range(n):
#     a = int(input("Enter no."))
#     arr.append(a)
# print("your array ->", arr)
#
# arr.sort()
# print("The second largest element is ->", arr[-2])


#                     ..... Sort array of only o,1,2 .......
# def sort_trio(s):
#     lo = 0
#     mid = 0
#     hi = len(s)-1
#
#     while mid <= hi:
#         if s[mid] == 0:
#             s[lo], s[mid] = s[mid], s[lo]
#             lo += 1
#             mid += 1
#
#         elif s[mid] == 1:
#             mid += 1
#         else:
#             s[mid], s[hi] = s[hi], s[mid]
#             hi -= 1
#     return s
#
# arr = [0, 1, 0, 1, 2, 1, 2]
# print(sort_trio(arr))

#                                     ...... Max Min in array ......
# def max_min(arr):
#     maxi = 0
#     mini = 1000000
#     n = len(arr)
#
#     for i in range(n):
#         if arr[i] > maxi:
#             maxi = arr[i]
#
#     for i in range(n):
#         if arr[i] < mini:
#             mini = arr[i]
#
#     print(maxi, mini)
#
# arr = [2,4,6,5,3,7,9,1]
# max_min(arr)

#                        ....... Move all negatives to left side ......
#
# def move_negatives(arr):
#     left = 0
#     right = len(arr)-1
#
#     while left <= right:
#         if arr[left] < 0 and arr[right] > 0:
#             left += 1
#             right -= 1
#         elif arr[left] > 0 and arr[right] < 0:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
#         elif arr[left] < 0 and arr[right] < 0:
#             left += 1
#         else:
#             right -= 1
#     return arr
#
#
# arr = [-1,-2,3,5,-6,2,-5,4]
# print(move_negatives(arr))





#######################################################################################################

                         # ....... cylinderically rotate array.......


# def cylindrically_rotate(arr, n):
#     temp = arr[n-1]
#     for i in range(n-1, 0, -1):
#         arr[i] = arr[i-1]
#     arr[0] = temp
#     return arr
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# n = len(arr)
#
# print(cylindrically_rotate(arr, n))

########################################################################################################################

#                   -------------------Second Largest Element In array------------------------

# def second_largest(arr, n):
#     largest = arr[0]
#     for i in range(n):
#         if arr[i] > largest:
#             largest = arr[i]
#     seclargest = -1
#     for i in range(n):
#         if arr[i] > seclargest and arr[i] != largest:
#             seclargest = arr[i]
#
#     return seclargest
#
#
# arr = [ 1,2,3,4,5,6,7,7]
# n = len(arr)
# print(second_largest(arr, n))    # complexity of this approach is O(2n) and O(1)


# def second_largest(arr):
#      largest = arr[0]
#      seclargest = -1
#      for i in range(len(arr)):
#          if arr[i] > largest:
#              seclargest = largest
#              largest = arr[i]
#
#          if arr[i]< largest and arr[i]> seclargest:
#              seclargest = arr[i]
#
#      return seclargest
#
# arr = [1,2,3,4,5,6,7,7,8]
# print(second_largest(arr))    # best optimal approach O(n) and O(n)

#######################################################################################################################
                 # ---- Left Rotate An Array by 1 Place-----
# def left_rotate(arr, n):
#
#     temp = arr[0]
#     for i in range(0, n-1):
#         arr[i] = arr[i+1]
#
#     arr[n-1] = temp
#     return arr
#
# arr = [1,2,3,4,5,6,7]
# n = len(arr)
# print(left_rotate(arr, n))    # Best Optimal Solution to rotate an array

#########################################################################################################

                   # ....... Left rotate array by D places .......
# def left_rotate(arr, n , d):
#     temp = []
#     for i in range(d,n):
#         temp.insert(arr[i])
#




#
# arr1 = [1,2,3,4,5,6,7]
# n = len(arr1)
# d = 2
# print(left_rotate(arr1, n, d))    # complexity of this approach O(n) and O(n)

#
# def left_rotate(arr,n,d):
#     for i in range(0, d):
#         arr.reverse()
#     for i in range(d, n):
#         arr.reverse()
#     for i in range(0, n):
#         arr.reverse()
#     return arr
#
#
# arr = [ 1,2,3,4,5,6,7]
# n = len(arr)
# d = 3
# print(left_rotate(arr, n, d))
####################################################################################################

#                 .............. (2D ARRAYS ) ...............
#
# def SearchElement(arr,element):
#
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j] == element:
#                 return "Present"
#
#     return "Not Present"
#
# def RowSum(arr):
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(len(arr[i])):
#             sum += arr[i][j]
#         print("Row", i, "sum is ", sum)
#
# def largestRowSum(arr):
#     presum = 0
#     for i in range(len(arr)):
#         sum = 0
#         for j in range(len(arr[i])):
#             sum += arr[i][j]
#         if sum > presum:
#             presum = sum
#     return presum
#
# def WavePrint(arr):
#
#     cols = len(arr[0])
#     rows = len(arr)-1
#     for c in range(cols):
#         if c % 2 != 0:
#             for r in range(rows, -1, -1):
#                 print(arr[r][c], end=" ")
#         else:
#             for k in range(rows+1):
#                 print(arr[k][c], end=" ")
#
# def spiralPrint(arr):
#     ans = []
#     rows = len(arr)
#     cols = len(arr[0])
#
#     top = 0
#     left = 0
#     right = cols-1
#     bottom = rows-1
#
#     while top <= bottom and left <= right:
#
#         for i in range(left,right+1):
#             ans.append(arr[top][i])
#         top += 1
#
#         for i in range(top,bottom+1):
#             ans.append(arr[i][right])
#         right -= 1
#
#         for i in range(right,left-1,-1):
#             ans.append(arr[bottom][i])
#         bottom -= 1
#
#         for i in range(bottom, top,-1):
#             ans.append(arr[left][i])
#         left += 1
#     return ans




















# r = int(input("Enter number of rows"))
# c = int(input("Enter number of columns"))

# myList = [[1, 2, 3,], [5, 6,7], [7, 8, 9,]]
# for i in range(r):
#     arr = []
#     for j in range(c):
#         val = int(input("Enter element"))
#         arr.append(val)
#     myList.append(arr)

# print(myList)
# for i in range(len(myList)):
#     for j in range(len(myList[i])):
#         print(myList[i][j], end=" ")
#     print()

# el = int(input("Enter the Element you want to search"))
# print(SearchElement(myList, el))
#
#
# RowSum(myList)
#
# print("Largest row sum is ", largestRowSum(myList))
#
#
# WavePrint(myList)

# print(spiralPrint(myList))
#######################################################################
#######################################################################
# def isvalid(arr,x):
#     for i in range(len(arr)):
#         if x % arr[i] == 0:
#             return False
#
#     return True
#
# arr = [2, 3, 4, 5, 6]
# k = 4
# x = 1
# count = 0
# sum = 0
# while count != k:
#     if isvalid(arr, x):
#         sum += x
#         count += 1
#     x += 1
# print(sum)

######################################################################
######################################################################

# def secLargest(arr):
#     largest = arr[0]
#     secondlar = -1
#     for i in range(len(arr)):
#         if arr[i] > largest:
#             secondlar = largest
#             largest = arr[i]
#         if arr[i]< largest and arr[i]>secondlar:
#             secondlar= arr[i]
#     return secondlar
# evenArr = []
# oddArr = []
# arr = []
# n = int(input("Enter the size of array"))
# for i in range(n):
#     num = int(input("Enter element at index :"))
#     arr.append(num)
#
# for i in range(len(arr)):
#     if i % 2 == 0:
#         evenArr.append(arr[i])
#     else:
#         oddArr.append(arr[i])
# print(arr)
# print(evenArr)
# print(oddArr)
# print(secLargest(evenArr)+secLargest(oddArr))

###################################################################
# ###################################################################
# def validPass(s):
#     cap = 0
#     num = 0
#     if len(s) < 4:
#         return 0
#     if s[0].isdigit():
#         return 0
#     for i in range(len(s)):
#         if s[i] == " " or s[i] == "/":
#             return 0
#         elif s[i] >= "A" and s[i] <= "Z":
#             cap += 1
#         elif s[i] >="1" and s[i] <="9":
#             num += 1
#
#     if cap > 0 and num > 0:
#         return 1
#     else:
#         return 0
#
# s = input("Enter the String")
# print(validPass(s))
# ############################################################################
# ############################################################################

# arr = [2,2,1,4,2,1,3,4,1,3,5,4]
#
# mp = {}
#
# for i in range(len(arr)):
#     if arr[i] in mp.keys():
#         mp[arr[i]] += 1
#     else:
#         mp[arr[i]] = 1
#
# for i in range(1,len(mp)):
#     print(i , mp[i])

#################################################################################
#################################################################################

# arr = [12, 3, 14, 56, 77, 13]
# num = 13
# diff = 2
# anss = 0
# for i in range(len(arr)):
#     res = arr[i]-num
#     if res <= diff:
#         anss += 1
# print(anss)

########################################################################
########################################################################

# s = "1C0C1C1A0B1"
#
# temp = s[0]
#
# for i in range(len(s)):
#     if s[i] == "A":
#         res = temp and s[i+1]
#     elif s[i] == "B":
#         res = temp or s[i+1]
#     elif s[i] == "C":
#         res = temp ^ s[i+1]
#

########################################################
########################################################

# n = 4
# m = 20
# divsum = 0
# nodivsum = 0
# for i in range(1, m+1):
#     if i % 4 == 0:
#         divsum += i
#     else:
#         nodivsum += i
#
# print(nodivsum - divsum)
##########################################################
##########################################################

# arr = [9,8,3,-7,3,9]
# sum = 4
#
# arr.sort()
# ans = arr[0]*arr[1]
# if ans < sum:
# #     print(ans)
#
# i = 0
# j = 1
# s = ["h","e","l","l","o","-","m","o","t","u","-","p","a","t","l","u"]
#
# while j <= len(s):
#     if s[i] == "-":
#         i += 1
#     elif s[j] == "-":
#         s[i], s[j] = s[j], s[i]
#         j += 1
#         i += 1
#     else:
#         j += 1
# print()

# s = "Test@123#"
# checks = 0
# upcount = 0
# locount = 0
# specount = 0
# digcount = 0
# consec = 0
#
# if len(s) < 6 or len(s) > 22:
#     checks += 1
#
# for i in range(len(s)):
#     if s[i]>="A" and s[i]<="Z":
#         upcount += 1
#     elif s[i]>="a" and s[i]<="z":
#         locount +=1
#     elif s[i] == "@" or s[i] == "!" or s[i] == "&" or s[i] == "^" or s[i] == "%" or s[i] == "*" or s[i] == "#":
#         specount += 1
#     elif s[i]>= "1" and s[i] <= "9":
#         digcount += 1
#     if i > 0 and s[i] == s[i-1]:
#         consec += 1
#     else:
#         continue
#
# if upcount < 1:
#     checks += 1
# if locount < 1:
#     checks += 1
# if specount < 2:
#     checks += 1
# if digcount < 1:
#     checks += 1
# if consec > 0:
#     checks += 1
#
# print(checks)
# arr = [1, 2, 3, 4, 3]
# largest = arr[0]
# secondlar = -1
# countl = 0
# counts = 0
# for i in range(1,len(arr)):
#     if arr[i] > largest:
#         secondlar = largest
#         largest = arr[i]
#     elif arr[i] < largest and arr[i]> secondlar:
#         secondlar = arr[i]
#
# for i in range(len(arr)):
#     if arr[i] == largest:
#         countl += 1
#     elif arr[i] == secondlar:
#         counts += 1
#
# lresult = countl - 1
# sresult = counts - 1
# print(lresult+sresult)

