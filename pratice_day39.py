"pratice question no 1"
# num=[10,20,30,40,50]
# sum=0
# for i in num:
#     sum+=i
# print("list sum",sum)
"pratice question no 2"
# num=[10,20,30,40,50]
# print(max(num))
# print(min(num))
"pratice question no 3"
# num=[10,20,30,40,50]
# num.reverse()
# print(num)
"pratice question no 4"
# num=[10,20,30,40,50]
# even=0
# odd=0
# for i in num:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)
"pratice question no 5"

"Remove duplicate"
# num=[10,20,30,40,50,50]
# num=list(set(num))
# print(num)

"pratice question no 6"
# num1=[10,20,30,40,50,50]
# num2=[60,70,80,90,0,110]
# merged=[]
# for i in num1:
#     if i not in merged:
#         merged.append(i)
# for i in num2:
#     if i not in merged:
#         merged.append(i) 
# print("merged list without duplicates:",merged)   

"pratice question no 9"

# num1=[10,20,30,40,50,50,7]
# for num in num1:
#     if num>1:
#         is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(num,end="")


"pratice question no 10"
# numbers=[2,3,4,5,6,7,8,9,10]
# largest=second=float('-inf')
# for num in numbers:
#     if num>largest:
#         second=largest
#         largest=num
#     elif num>second and num!=largest:
#         second=num

# print("second largest element :",second)

"pratice question no 11"
# list1=[1,2,3,4,5]
# k=2
# k=k%len(list1)
# rotated=list1[k:]+list1[:k]
# print("Left Rotated list",rotated)

"pratice question no 12"
# list1=[1,2,3,4,5]
# Square=[]
# for i in list1:
#     Square.append(i*i)
# print("Squared list:",Square)
"pratice question no 13"
# list1=[1,2,3,4,5,-1,-2,-3,-4,-5]
# list=[]
# for i in list1:
#     if i>=0:
#         list.append(i)
# print("Positive number",list)
"pratice question no 14"
# list1=[1,2,3,4,5]
# product=1

# for i in list1:
#     product=i*product
# print(product)
"pratice question no 15"
# list1=[1,2,2,2,2,3,3,3,4]
# max_count=0
# most_frequent=None

# for i in list1:
#     count=list1.count(i)
#     if count>max_count:
#         max_count=count
#         most_frequent=i
# print("Most frequent Element ",most_frequent)

"pratice question no 16"
# list1=[1,2,3,4,5,6]
# mid=len(list1)//2

# first_half=list1[:mid]
# second_half=list1[mid:]

# print("First_Half",first_half)
# print("Second Hald",second_half)

"pratice question no 17"
# list1=[1,2,1]
# if list1==list1[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")
"pratice question no 18"
# list1=[1,2,3,4]
# comulative=[]
# total=0
# for i in list1:
#     total+=1
#     comulative.append(total)
# print(comulative)

"pratice question no 19"
# list1=[1,[2,3],[4,5]]
# flatten=[]
# for i in list1:
#     if type(i)==list:
#         for j in i:
#             flatten.append(j)
# print("flattened list",flatten)
"pratice question no 20"

list1=[1,2,3,4,5]
target=6
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]==target:
            print(list1[i],list1[j])
            


































