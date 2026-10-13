"Pratice question no 1"
# sorting in ascending order

# def merge_sort(nums):
#     if len(nums)<=1:
#         return nums
#     mid =len(nums)//2
#     left=merge_sort(nums[:mid])
#     right=merge_sort(nums[mid:])
#     return merge(left,right)
# def merge(left,right):
#     result=[]
#     i=0
#     j=0
#     while i<len(left) and j <len(right):
#         if left[i]<=right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# # nums=[8,3,6,2,7,1]
# nums=[4,-2,7,4,0,-2,5]
# print(merge_sort(nums))


"Pratice question no 2"
#Sorting in decending order
# def merge_sort(nums):
#     if len(nums)<=1:
#         return nums
#     mid=len(nums)//2
#     left=merge_sort(nums[:mid])
#     right=merge_sort(nums[mid:])
#     return merge(left,right)
# def merge(left,right):
#     result=[]
#     i=0
#     j=0
#     while i<len(left) and j<len(right):
#         if left[i]>=right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# nums=[1,2,3,4,5,6,7,8,9]
# print(merge_sort(nums))
