"pratice question no 1"
# l1=[1,2,3,4,5]
# print(l1)

"pratice question no 2"
# numbers=[]
# for i in range(5):
#     num=int(input("Enter a number"))
#     numbers.append(num)
# print("List of numbers",numbers)

"pratice question no 3"
# l1=[1,2,3,4,5]
# length=0
# for _ in l1:
#     length+=1
# print("The length of the list are",length)

"pratice question no 4"
# l1=[100,101,99,55,22,44,55,66,211]
# l1.sort()
# max_element=l1[0]
# for i in l1:
#     if i>max_element:
#         max_element=i
# print("maximum element",max_element)

"pratice question no 5"
# l1=[100,101,99,55,22,44,55,66,211]
# l1.sort()
# print("minimum element",l1[0])

"pratice question no 6"
# l1=[100,101,99,55,22,44,55,66,211]
# sum=0
# for i in l1:
#     sum+=i
# print("Sum of list is",sum)

"pratice question no 7"
# l1=[100,101,99,55,22,44,55,66,211]
# even_count=0
# odd_count=0
# for i in l1:
#     if i%2==0:
#         even_count+=1
#     else:
#         odd_count+=1

# print("even count",even_count)
# print("odd count",odd_count)

"pratice question no 8"
# l1=[100,101,99,55,22,44,55,66,211]
# rev=[]
# for i in range(len(l1)-1,-1,-1):
#     rev.append(l1[i])
# print(rev)

"pratice question no 9"

# l1=[100,101,99,55,22,44,55,66,211]
# l1.sort(reverse=True)
# print(l1)

"pratice question no 10"
# l1=[100,101,99,55,22,44,55,66,211]
# target=211

# if target in l1:
#     print("Present")
# else:
#     print("Not present ")

"pratice question no 11"
# l1=[1,1,2,2,3,3,4,4,5,5]
# l2=set(l1)
# l3=list(l2)
# print(l3)

# remove_duplicate=[]
# for i in l1:
#     if i not in remove_duplicate:
#         remove_duplicate.append(i)
# print(remove_duplicate)

"pratice question no 12"
# l1=[1,2,3]
# l2=["apple","banana","cherry"]
# for x in l1:
#     l2.append(x)
# print(l2)

"pratice question no 13"
# l1=[100,101,99,55,22,44,55,66,211]
# # l1.sort()
# # print(l1[-2])
# largest=second_largest=float('-inf')
# for num in l1:
#     if num>largest:
#         second_largest=largest
#         largest=num
#     elif num>second_largest and num!=largest:
#         second_largest=num
# print("Second largest element ",second_largest)

"pratice question no 14"
# l1=[1,2,3,4]
# last=l1[-1]
# l1.pop()
# l1.insert(0,last)
# print(l1)

"pratice question no 15"
# l1=[1,2,3,4,5]
# k=2
# l1=l1[k:] + l1[:k]
# print(l1)
"pratice question no 16"
# l1=[1,-1,2,-2,3,-3,4,-4,5,-5,]
# positive_list=[]
# negative_list=[]
# for i in l1:
#     if i>0:
#         positive_list.append(i)
#     else:
#         negative_list.append(i)

# print("positive list",positive_list)
# print("Negatice list",negative_list)

"pratice question no 17"
# l1=[1,-1,2,-2,3,-3,4,-4,5,-5,]
# l1.sort()
# print("Second smallest number",l1[1])

"pratice question no 18"
# l1=[1,1,1,2,2,3,3,3,3,3,]
# freq={}
# for i in l1:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for key,value in freq.items():
#     print(key,"-",value,"items")

"pratice question no 19"
# l1=[1,2,3,4]
# l2=[1,2,3,4]
# if l1==l2:
#     print("Both list are equal")
# else:
#     print("good night and please you must take rest ")

"pratice question no 20"
# l1=[2,4,3,5,6]
# pair=[]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i] + l1[j]==7:
#             pair.append((l1[i],l1[j]))
        
# print(pair)

"pratice question no 21"
# nums=[100,4,200,1,3,2]
# nums.sort()
# print("Sorted list:",nums)
# length=1
# max_length=1

# for i in range(len(nums)-1):
#     if nums[i]+1==nums[i+1]:
#         length+=1
#     elif nums[i]==nums[i+1]:
#         continue
#     else:
#         length=1
# max_length=max(max_length,length)
# print("Longest Consecutive length",max_length)


















































