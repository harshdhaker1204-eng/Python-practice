"Lists in python"
"program 1"
"find a sum of list elements"
# numbers=[10,20,30,40,50]
# sum=0
# for num in numbers:
#     sum+=num
#     print("The sum of list elements is:",sum)

"Program 2"
"take 5 inputs from user and strore them in a list"
# user_inputs=int(input("Enter number of inputs you want to provide:"))
# input_list=[5]
# for i in range(user_inputs):
#     element=input("Enter element:")
#     input_list.append(element)
#     print("The list of user inputs is:",input_list)

"Program 3"
"remove duplicates from a list"
# original_List=[1,2,2,3,4,4,5,6,6]
# unique_List=[]
# for item in original_List:
#     if item not in unique_List:
#         unique_List.append(item)
#         print("The List after removing duplicates is:",unique_List)

"Program 4"
"add an two to list of elements"
# fruits=["apple","banana","cherry"]
# number=[1,2,3,4,5]
# print(fruits+number)

"Program 5 "
"Reverse a list without using reverse function"
# my_list=[1,2,3,4,5]
# reversed_list=[]
# for i in range(len(my_list)-1,-1,-1):
#     reversed_list.append(my_list[i])
#     print("The reversed list is:",reversed_list)

"program 6"
"sort the list in both ascending and decendingn order"
# my_list=[5,2,9,1,5,6]
# ascending_List=sorted(my_list)
# decending_list=sorted(my_list,reverse=True)
# print("The list in ascending order is:",ascending_List)
# print("The list in decending order is:",decending_list)


"program 7"
"count a specific frequency of an element in a list"
# my_list=[1,2,2,3,4,4,4,5]
# count=my_list.count(4)
# print("The count of 4 in the list is:",count)

"Tuples in python"
"Program 1"
"Tuple is given how many times 20 repeated in tuple (10,20,30,20,50)"
# my_tuple=(10,20,30,20,50)
# count=(my_tuple.count(20))
# print("The count of 20 in the tuples is:",count)

"Program 2"
"Convert tuple to list"
# my_tuple=(1,2,3,4,5)
# my_list=list(my_tuple)
# print("The converted list is:",my_list)

"PRogram 3"
"find the average of the tuples elements "
# my_tuple=(10,20,30,40,50)
# sum=0
# for num in my_tuple:
#     sum+=num
#     average=sum/len(my_tuple)
#     print("The average of tuple elements is:",average)

"Program 4"
"concatenate tow tuples"
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# concatenated_tuple=tuple1+tuple2
# print("The concatenated tuple is:",concatenated_tuple)

"program 5"
"find the maximum and minimum element in a tuple"
# my_tuple=(10,20,5,30,15)
# max_element=max(my_tuple)
# min_element=min(my_tuple)
# print("The maximum element in the tuple is:",max_element)
# print("The minimum element in the tuple is:",min_element)

"Program 6"
"Take input from user and store them in a tuple"
# user_inputs=int(input("Enter number of inputs you want to provide:"))
# input_list=[]
# for i in range(user_inputs):
#     element=input("Enter element:")
#     input_list.append(element)
#     input_tuple=tuple(input_list)
#     print("The tuple of user inputs is:",input_tuple)

"find 50 is greater than 20 or not using boolean operators"
a=50
b=20
print("Is 50 greater than 20:",a>b)
print("Is 50 less than 20:",a<b)
print("Is 50 equal to 20:",a==b)
print("Is 50 not equal to 20:",a!=b)
