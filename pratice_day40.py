# tup=(1,2,3,4,5,6)
# print(tup)

# tup=(1,2,3,4,5,6)
# print(tup[3])

# tup=(1,2,3,4,5,6)
# print(tup[-1])

# tup=(1,2,3,4,5,6)
# print(len(tup))

# tup1=(1,2,3,4,5,6)
# tup2=(7,8,9,10,11,12)
# print(tup1+tup2)

# tup1=(1,2,3,4,5,6)
# print(tup1[::-1])

# tup1=(1,2,3,4,5,6)
# print("The maximum of tuple",max(tup1))


# tup1=(1,2,3,4,5,6)
# print("The minimum of tuple",min(tup1))

# tup1=(1,2,3,2,4,2,5)
# count=0

# for i in tup1:
#     if i==2:
#         count+=1
# print("Total counts",count)


# tuple=(10,20,30,40,50)
# print(tuple[1:4])

# X=(10,20,30,40,50)

# Y=list(X)
# Y[4]=100
# X=tuple(Y)
# print(X)

# N_tuple=((1,2),(3,4),(5,6))
# print(N_tuple[1][1])


# X=(10,20,30,40,50)
# sum=0
# for i in X:
#     sum+=i
# print("The total sum of list this is",sum)

# X=("Apple","banana","Mango","Orange","pineapple")
# (A,*B,C)=X
# print(A)
# print(B)
# print(C)

# tup1=(1,2,3,2,4,2,5)
# new_tup=tuple(set(tup1))
# print(new_tup)

# tup1=(5,10,15,20,25,30)
# even_tup=()
# for i in tup1:
#     if i%2==0:
#         even_tup+=(i,)
# print(even_tup)

# t1 = (1,2,3,4)
# t2 = (1,2,3)

# if t1 == t2:
#     print("Equal")
# else:
#     print("Not Equal")

# my_tuple=(10,5,8,20,15,20)
# sorted_list=sorted(list(my_tuple))
# second_largest=sorted_list[-2]

# print(f"The second largest num,ber is:",{second_largest})

# T1=("apple","banana","orange")
# T2=tuple([i.upper() for i in T1])

# print(T2)



# T1=('APPLE', 'BANANA', 'ORANGE')
# T2=tuple([i.lower() for i in T1])

# print(T2)

tup=(40,10,30,20,50)
sorted_tup=tuple(sorted(tup))

print("Original Tuple:",tup)
print("Sorted tuples",sorted_tup)























