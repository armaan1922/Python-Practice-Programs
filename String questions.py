# # ........... String palindrome check........
#
# a = input("Enter any word")
# start = 0
# last = len(a)-1
# flag = 0
# while(start < last):
#     if a[start] == a[last]:
#         start += 1
#         last -= 1
#     else:
#         flag = 1
#         break
# if flag == 0:
#     print("The string is palindrome")
# else:
#     print("NOT Palindrome")

#
# nums = [1,-2,-3,4,5,-6,-7]
#
# i = 0
# j = 1
# while j < len(nums):
#     if nums[i] > 0 and nums[j] < 0:
#         i += 1
#         j += 1
#
#     elif nums[i] < 0 and nums[j] > 0:
#         nums[i], nums[j] = nums[j], nums[i]
#         i += 1
#         j += 1
#     elif nums[i] < 0 and nums[j] < 0:
#         k = i
#         while k < len(nums):
#             if nums[k] > 0:
#                 nums[i], nums[k] = nums[k], nums[i]
#                 break
#         i += 1
#         j += 1
#     else:
#
#         k = j
#         while k < len(nums):
#             if nums[k] < 0:
#                 nums[j], nums[k] = nums[k], nums[j]
#                 break
#         i += 1
#         j += 1
# print()
# count1 = 0
# count2 = 0
# el1 = -1
# el2 = -1
# for i in range(len(arr)):
#     if count1 == 0 and arr[i] != el2:
#         count1 = 1
#         el1 = arr[i]
#
#     elif count2 == 0 and arr[i] != el1:
#         count2 = 1
#         el2 = arr[i]
#
#     elif arr[i] == el1:
#         count1 += 1
#     elif arr[i] == el2:
#         count2 += 1
#     else:
#         count1 -= 1
#         count2 -= 1
#
# result = []
# count1 = 0
# count2 = 0
# target = len(arr) // 3
# for i in range(len(arr)):
#     if arr[i] == el1:
#         count1 += 1
#     elif arr[i] == el2:
#         count2 += 1
# if count1 > target:
#     result.append(count1)
# if count2 > target:
#     result.append(count2)
# return result
# import math
#
#
# def calculate_distance(point1, point2):
#     return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
#
#
# def assign_vehicles(passengers, vehicles):
#     allocated_vehicles = {}
#     total_distance = 0
#
#     for passenger in sorted(passengers):
#         min_distance = math.inf
#         closest_vehicle = ""
#         passenger_coordinates = passenger[passenger]
#
#
#     for vehicle in vehicles:
#         if vehicle[vehicle] == "":
#             vehicle_coordinates = vehicles[vehicle + "_coordinates"]
#             distance = calculate_distance(passenger_coordinates, vehicle_coordinates)
#             if distance < min_distance or (distance == min_distance and vehicle < closest_vehicle):
#                 min_distance = distance
#                 closest_vehicle = vehicle
#
#     allocated_vehicles[passenger] = closest_vehicle
#     vehicles[closest_vehicle] = passenger
#     total_distance += min_distance
#
#     return total_distance
#
# N, M = map(int, input().split())
# passengers = {}
# vehicles = {}
#
# for _ in range(N):
#     name, x, y = input().split()
#     passengers[name] = (int(x), int(y))
#
# for _ in range(M):
#     vehicle, x, y = input().split()
#     vehicles[vehicle] = ""
#     vehicles[vehicle + "_coordinates"] = (int(x), int(y))
#
# minimum_distance = assign_vehicles(passengers, vehicles)
#
# print(minimum_distance)















