"Pratice question no 1"
# list1=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in list1:
#     sum+=i
# print("The sum of list1 are ",sum)

"Pratice question no 2"
# list2=[5,10,15,20,25,30,35,40,45,50]
# largest=list2[0]

# for i in list2:
#     if i>largest:
#         largest=i
# print("The largest element is:",largest)

# print("The largest element are",max(list2))

"Pratice question no 3"
# list3=[5,10,15,20,25,30,35,40,45,50]
# smallest=list3[0]

# for i in list3:
#     if i<smallest:
#         smallest=i
# print("The smallest number is list are",smallest)

# print("The smallest element in list3 are",min(list3))

"Pratice question no 4"
# list4 = [1,2,3,4,5,6,7,8,9,10]
# reverse = []

# for i in list1:
#     reverse.insert(0, i)

# print(reverse)

"Pratice question no 5"
# list5=[5,10,15,20,25,30,35,40,45,50]
# even_no=[]
# for i in list5:
#     if i%2==0:
#         even_no.append(i)

# print("Even number list is",even_no)

"Pratice question no 6"
# list6=[5,10,15,20,25,30,35,40,45,50]
# odd_count=0
# for i in list5:
#     if i%2!=0:
#         odd_count+=1
# print("The total number of odd numbers in list are ",odd_count)

"Pratice question no 7"
# list7=[5,10,15,15,15,15,15,20,25,30,35,40,45,50]

# unique_list = []

# for i in list7:
#     if i not in unique_list:
#         unique_list.append(i)

# print(unique_list)
"Pratice question no 8"
# list1=[1,2,3,4,5];list2=[6,7,8,9,10]
# merge_list=(*list1,*list2)
# print(merge_list)

"Pratice question no 9"
# list6=[50,10,15,20,25,30,35,40,45,5]
# n=len(list6)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if list6[j]>list6[j+1]:
#             #swap
#             list6[j],list6[j+1]=list6[j+1],list6[j]
# print("Sorted list:",list6)
"Pratice question no 10"
# list10=[10,20,30,40,50]
# target=30
# index=-1
# for i in range(len(list10)):
#     if list10[i]==target:
#         index=i
#         break
# print("Index is:",index)
"Pratice question no 11"
# def leftRotate(arr,d):
#     n=len(arr)
#     d=d%n
#     arr[:]=arr[d:] +arr[:d]
#     return arr
# print(leftRotate([1,2,3,4,5],2))

"Pratice question no 12"
# arr=[1,2,3,4,5]
# result=arr[-1:] + arr[:-1]
# print(result)

"Pratice question no 13"
# arr=[1,2,3,4,5]
# Square_list=[]
# for i in arr:
#     Square_list.append(i*i)

# print(Square_list)
"Pratice question no 14"
# arr=[50,45,40,35,30,25,20,15,10,5]
# unique_sorted_list=sorted(list(set(arr)))
# second_largest=unique_sorted_list[-2]
# print(f"The second largest distinct element is :{second_largest}")
# sorted_list=sorted(arr)
# second_largest_with_duplicates=sorted_list[-2]
# print(f"The second largest element (allowing duplicates ) is :{second_largest_with_duplicates}")
"Pratice question no 15"
# l1=[1,2,1]
# rev=l1
# if l1==rev[::-1]:
#     print("Its Palindrome")
# else:
#     print("Not a palindrome")

"Tuples questions"
"pratice question no 1"
# t1=(1,2,3,4,5)
# print("The lenght of tjhe tuple are",len(t1))
"pratice question no 2"
# t1=(1,2,3,4,5)
# sum=0
# for i in t1:
#     sum+=i
# print("The sum of the tuple are",sum)
"pratice question no 3"
t1=(888,237834,43723894,34787364,7984788,213683478,3478934879)
"Here it is direct method using max and min function"
# print("The maximum of tuple element is",max(t1))
# print("The minimum of tuple element is",min(t1))
"Here first we have sorted the list the we will return the -1 index and 0 index"
# sorted_tuple=sorted(t1)
# print(sorted_tuple)
# print("The maximum element is sorted tuple are ",sorted_tuple[-1])
# print("The minimum element of sorted tuple are",sorted_tuple[0])

"pratice question no 4"
# tu =(1,2,3,4,5)
# l1=list(tu)
# l1[1]=6
# tu=tuple(l1)
# print(l1)

"pratice question no 5"
# my_tuple=("apple","banana","cherry")
# element_to_check="apple"
# if element_to_check in my_tuple:
#     print(f"Yes,'{element_to_check}' is in the tuple.")
# else:
#     print(f"No,'{element_to_check}' is not in the tuple.")

# #You can also use it directly in an expression:
# is_present="banana" in my_tuple
# print(is_present)

# is_not_present="grape" in my_tuple
# print(is_not_present)
"pratice question no 6"
# t1=(1,2,3,4,5)
# t2=(6,7,8,9,10)
# merge=*t1,*t2
# print(merge)

"pratice question no 7"
# t1=(1,2,3,4,4,4,4,45,5,5,5,5)
# elements=[4,5]
# for e in elements:
#     count=0
#     for i in t1:
#         if i==e:
#             count+=1
      
    
#     print("Total element in tuples is",count)

"pratice question no 8"
# t1=(1,2,3,4,5)
# reversed=()
# for i in range(len(t1)-1,-1,-1):
#     reversed+=(t1[i],)
# print(reversed)
# print(t1[::-1])

"pratice question no 9"
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)
"Pratice question no 10"
# student_details={
#     'name':"aman gupta",
#     'age':20,
#     'marks':90
# }
# print(student_details)
"Pratice question no 11"
# student_details={
#     'name':"aman gupta",
#     'age':20,
#     'marks':90
# }
# new_student_details={
#     'name':'rohan das',
#     'age':21,
#     'marks':85
# }
# student_details.update(new_student_details)
# print(student_details)
# merged_dict=student_details|new_student_details
# print(merged_dict)
# merged_key={}

# for key in student_details:
#    merged_key[key]=[student_details[key],new_student_details[key]]
# print(merged_key)

"Pratice question no 12"
# new_student_details={
#     'name':'rohan das',
#     'age':21,
#     'marks':85
# }
# new_student_details.pop('age')
# print(new_student_details)

"Pratice question no 13"
# new_student_details={
#     'name':'rohan das',
#     'age':21,
#     'marks':85
# }
# key_view=new_student_details.keys()
# print(key_view)
"Pratice question no 14"
# new_student_details={
#     'name':'rohan das',
#     'age':21,
#     'marks':85
# }
# value_view=new_student_details.values()
# print(value_view)
"Pratice question no 15"
# fruits={'1':'apple','2':'banana','3':'orange','4':'mango'}
# print(fruits)
"Pratice question 16"
fruits={'1':'apple','2':'banana','3':'orange','4':'mango'}
# key=input("Enter a key")
# if key in fruits:
#     print("Key is present")
# else:
#     print("Key is not present")
"Pratice question 17"
# fruit1={'1':'apple','2':'banana','3':'orange','4':'mango'}
# fruit2={'5':'cherry','6':'grapes','7':'pineapple','8':'guava'}
# merge_dict=fruit1|fruit2
# print(merge_dict)
"Pratice question no 18"
# set1={1,2,3,4,5}
# print(set1)
"Pratice question no 19"
# numbers=set()
# numbers.add(10)
# numbers.add(20)
# numbers.add(30)
# numbers.add(40)
# print(numbers)
"Pratice question no 20"
# numbers={10,20,30}
# numbers.add(40)
# print(numbers)
"Pratice question no 21"
# numbers={10,20,30,40}
# numbers.remove(20)
# print(numbers)
"Pratice question no 22"
# numbers={10,20,30,40,50}
# num=int(input("Enter a number"))
# if num in numbers:
#     print("Number is present")
# else:
#     print("Number is not present")
"Pratice question no 23"

# number1={10,20,30,40,50}
# number2={50,70,80,90,100}
# union=number1|number2
# print(union)

"Pratice question no 24"
# number1={10,20,30,40,50}
# number2={50,70,80,40,100}
# intersection=number1&number2
# print(intersection)
"Pratice question no 25"
# fruits={"apple","oranges","barries","cherries"}
# to_eat={"apples","cereals","barries","bread"}
# result=fruits-to_eat
# print(result)

"Pratice question no 26"
# l1=[1,1,2,2,3,3,4,4,5,5,6,6,7,7]
# t1=set(l1)
# print(t1)

"Pratice question no 27"
# l1={1,2,3,4,5,6,7,8,9,10}
# for i in l1:
#     print(i)
"Pratice question no 28"
# l1={1,2,3,4,5,6,7,8,9,10}
# print(max(l1))
"Pratice question no 29"
# my_set={10,4,76,23,12}
# max_val=float('-inf')
# for num in my_set:
#     if num>max_val:
#         max_val=num
# print(max_val)

"Pratice question no 29"
# my_set={10,4,76,23,12}
# print(min(my_set))

"Pratice question no 29"
# my_set={10,4,76,23,12}
# min_val=float('inf')
# for num in my_set:
#     if num<min_val:
#         min_val=num
# print(min_val)
"Pratice question no 30"
# set1={1,2,3,4}
# set2={3,4,5,6}
# result_method=set1.symmetric_difference(set2)
# print(result_method)
"Pratice question no 31"
# set_a={"apple","banana","cherry"}
# list_b=['banana','grape','kiwi']
# result=set_a.symmetric_difference(list_b)
# print(result)
"pratice question no 32"
# from itertools import combinations
# def get_k_subsets(s,k):
#     return list(combinations(s,k))
# #Example Usage
# my_set={1,2,3,4}
# k=2
# print(get_k_subsets(my_set,k))
"Pratice question no 34"
# set1={1,2,3,4}
# set2={1,2,5,6}
# set3=set()
# for i in set1:
#    if i in  set2:
#       set3.add(i)
# print(set3)
"Pratice question no 35"
# set1={1,2,3,4}
# set2={3,4,5,6}
# merged_set=set1.union(set2)
# print(merged_set)
"Pratice question no 36"
# set1={1,2,3,4,5,6,7,8,9,10}
# even=set()
# for i in set1:
#     if i%2==0:
#         even.add(i)

# print(even)
"Pratice question no 37"

# set1={1,2,3,4,5,6,7,8,9,10}
# odd=set()
# for i in set1:
#     if i%2!=0:
#         odd.add(i)

# print(odd)
"pratice question no 38"
# set1={10,20,30,40,50,60,70,80,90,100}
# for i in set1:
#     if i>50:
#         print(i)

"pratice question no 39"
set1={10,20,30,40,50,60,70,80,90,100}
square_set1=set()
for i in set1:
    square_set1.add(i*i)
print(square_set1)






































 



































 












