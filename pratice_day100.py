# arrs=[3,4,-5,8,-12,7,6,2]
# max_sub=float('-inf')
# for i in range(len(arrs)):
#     total=0
#     for j in range(i,len(arrs)):
        
#         total+=arrs[j]
#         max_sub=max(total,max_sub)
# print(max_sub)

"kadenes algorithm"
# def max_subarray(nums):
#     current_sum=nums[0]
#     max_sum=nums[0]
#     for i in range(1,len(nums)):
#         current_sum=max(nums[i],current_sum+nums[i])
#         max_sum=max(max_sum,current_sum)
#     return max_sum
# print(max_subarray(nums=[5,6,-2,3,4]))

"maximum of two sum"
# arr=[1,-1,2,3,3,4,5,6]

# max_two_sum=float('-inf')
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         max_two_sum=max(max_two_sum,arr[i]+arr[j])
# print("maximum of two sum array",max_two_sum)