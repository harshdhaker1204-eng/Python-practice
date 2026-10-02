"pratice question no 1"
# num=int(input("Enter a number"))
# temp=num
# rev=0
# while temp>0:

#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10
# if num==rev:
#     print("Its palindrome")
# else:
#     print("its not a palindrome")

"pratice question no 2"
# num=int(input("Enter a number"))
# for i in range(1,11):
#     print(f"{num}X{i} =",num*i)

"pratice question no 3"
# third=int(input("Enter a number"))
# first=0
# second=1
# for i in range(third):
#     print(first,end=" ")
#     third=first+second
#     first=second
#     second=third
    
"pratice question no 4"
# num=int(input("Enter a number"))
# l1=[]
# for i in range(num+1):
#     l1.append(i)
# print(max(l1))

"pratice question no 5"
# num=int(input("Enter a number"))
# l1=[]
# for i in range(num+1):
#     l1.append(i)
# print(l1)
# print(min(l1))

"pratice question no 6"
# num=int(input("Enter a number"))
# l1=[]
# for i in range(num+1):
#     l1.append(i)
# print(l1)
# print(sum(l1))

"pratice question no 7"
# l1=[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,7,7,7]
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)

"pratice question no 8"
# l1=[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,7,7,7]
# count_dict={}
# for i in l1:
#     if i in count_dict:
#         count_dict[i]+=1
#     else:
#         count_dict[i]=1
# print(count_dict)

"pratice question no 9"

# l1=[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,7,7,7]
# s=set(l1)
# l=list(s)
# l.sort()
# print(l[-2])

"pratice question no 10"
# l1=[1,2,3,4]
# l2=[5,6,7,8]
# print(l1+l2)

"pratice question no 11"
# t1=(1,2,2,3,4,5,6)
# print(len(t1))

"pratice question no 12"

# t1=(1,2,2,3,4,5,6)

# l1=list(t1)
# s1=set(l1)
# l2=list(s1)
# t1=tuple(t1)

# print(max(t1))
"pratice question no 13"
# t1=(1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,7,7,7)
# l1=list(t1)
# dict_count={}
# for i in l1:
#     if i in dict_count:
#         dict_count[i]+=1
#     else:
#         dict_count[i]=1
# print(dict_count)
"pratice question no 14"
# l1=(1,2,3,4,5)
# t1=list(l1)
# t1.append(6)
# print(t1)
"pratice question no 15"
# l1=(1,2,3,4,5)
# t1=list(l1)
# print(t1[0])
"pratice question no 16"
# s1={1,2,3,4,4,4,5,6,7}
# s2={8,9,2,3,1}
# s3=s2.union(s1)
# print(s3)

"pratice question no 16"
# s1={1,2,3,4,4,4,5,6,7}
# s2={8,9,2,3,1}
# s3=s2.intersection(s1)
# print(s3)

"pratice question no 17"
# s1={1,2,3,4,4,4,5,6,7}
# s2={8,9,2,3,1}
# s3=s2.difference(s1)
# print(s3)

"pratice question no 18"
# l1=[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,7,7,7]
# s1=set(l1)
# print(s1)

"pratice question no 19"
# set={1,2,3,4,5}
# n=1
# if n in set:
#     print("Exist")
# else:
#     print("Not Exist")

"pratice question no 20"
# student_dict={"Rohit":44,"rudra":77,"Naitik":70,"Ankit":70}
# for i in student_dict.keys():
#     print(i)

"pratice question no 21"
# student_dict={"Rohit":44,"rudra":77,"Naitik":70,"Ankit":70}
# for i in student_dict.values():
#     print(i)
"pratice question no 22"
# s="programming"
# freq={}
# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)
"pratice question no 23"

# dict1={"a":10,"b":20}
# dict2={"c":30,"d":40}
# dict3={}
# for key in dict1:
#     dict3[key]=dict1[key]
# for key in dict2:
#     dict3[key]=dict2[key]
# print(dict3)

"pratice question no 24"

student_dict={"Rohit":44,"rudra":77,"Naitik":70,"Ankit":70}
reverse={}
for key,values in student_dict.items():
    reverse[values]=key
print(reverse)




















