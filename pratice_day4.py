"Python setd"
"Program 1"
"Remove the duplicates from the sets"
# fruits=['apple','banana','mango','cherry','orange','apple']
# fruits.remove('apple')
# print(fruits)
# my_fruits=set(fruits)
# print(my_fruits)

"Program 2"
"Find union,intersection,difference of two sets"
# set1={1,2,3}
# set2={2,3,4}
# union=set1|set2
# set3=set1.intersection(set2)
# set3=set1.difference(set2)
# print(union)
# print(set3)
# print(set3)

"Program3"
"Perform remove and add operation in sets"

# set1={1,2,3,4,5,6,7,8,9,10}
# set1.remove(4)
# a=set1.add(11)
# print(set1)
# print(a)

"Program 4"
"Check the set is disjoint or not"
# Set_A={1,2,3,4}
# set_B={5,6,7}
# set_C={4,5,8}
# print(f"Are set_A and Set_B disjoint?{Set_A.isdisjoint(set_B)}")
# print(f"Are Set_A and Set_C disjoint{Set_A.isdisjoint(set_C)}")

"Program 5"
"Filter the even numbers"
# my_sets=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in range(2,20,2):
#     print(i)


"program 6"
"1 to 20 squares numbers"
# square_set={x*x for  x in range(1,21)}
# print(square_set)

"program 7"
"Make frozenset "
# x=frozenset({"apple","banana","mango","Cherry","mango"})
# print(x)
# print(type(x))

"Python dictionary"
"Program 1"
# Marks_dictionary={'subject1':99,'subject2':89,'subject3':95,'subject4':85,'subject5':94}
# maximum_key=max(Marks_dictionary,key=Marks_dictionary.get)
# maximum_value=Marks_dictionary[maximum_key]
# print(f"key with the maximum value:{maximum_key}")
# print(f"The maximum value is:{maximum_value}")

"Program 2"
# data={"a":10,"b":20,"c":30}
# key_list=list(data.keys())
# values_list=list(data.values())
# print(key_list)
# print(values_list)

"program 3"
# text="apple banana apple mango banana apple"
# freq={}
# for word in text.split():
#     freq[word]=freq.get(word,0)+1
# print(freq)

"program 4"
# d1={"a":1,"b":2}
# d2={"c":3,"d":4}
# merged={**d1 ,**d2}
# print(merged)

"Program 5"
data={"name":"payal","age":23}
key="age"
if key in data:
    print("Key exists")
else:
    print("Key not found")