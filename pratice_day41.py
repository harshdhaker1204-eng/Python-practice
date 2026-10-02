# student_details={
#     "Ronak jain":83,
#     "aman gupta":76,
#     "aanshul lasod":99,
#     "Mega Soni":80,
#     "Vishal nagori":95

# }
# print(student_details)


# student_details={
#     "Ronak jain":83,
#     "aman gupta":76,
#     "aanshul lasod":99,
#     "Mega Soni":80,
#     "Vishal nagori":95

# }
# key =input("Enter a key:")

# if key in student_details:
#     print("Key is present")
# else:
#     print("Key is not present")

student_details1={
    "Ronak jain":83,
    "aman gupta":76,
    "aanshul lasod":99,
    "Mega Soni":80,
    "Vishal nagori":95

}

# for i in student_details.keys():
#     print(i)

# for i in student_details.values():
#     print(i)

# student_details["Anish sen"]=65
# print(student_details)

# del student_details['Vishal nagori']
# print(student_details)


# print(len(student_details))

# sum=0
# for i in student_details.values():
#     sum+=i
# print(sum)

# max_val=max(student_details.values())
# print(max_val)

# min_val=min(student_details.values())
# print(min_val)

# reversed_dict={}
# for key,value in student_details.items():
#     reversed_dict[value]=key

# print("Original:",student_details)
# print("Reversed:",reversed_dict)

# student_details2={
#     "ayushi tiwari":33,
#     "astitwa sharma":80,
#     "amir khan":45,
#     "kanishk rawal":80,
#     "harsh chadel":66


# }
# merge_dictionary=student_details1|student_details2
# print(merge_dictionary)

# text=input("Enter a string")

# #Empty dictionary
# freq={}

# #Loop through each character
# for ch in text:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print("Character Frequency:",freq)

"Sample list"
# nums=[1,2,2,3,1,4]
# freq={}

# for num in nums:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1
# print("Frequency:",freq)

"List Elements Frequency"
# nums=[1,2,2,3,1,4]
# freq={}

# for num in nums:
#     freq[nums] = freq.get(num,0)+1

# print(freq)


# 
# data={
#     "a":10,
#     "b":15,
#     "c":20,
#     "d":25
# }
# even_dict={}

# for key,value in data.items():
#     if value%2==0:
#         even_dict[key]=value
# print(even_dict)

# student={
#     "Rahul":{"marks":85,"age":20},
#     "Aman":{"marks":90,"age":21},
#     "Neha":{"marks":78},"age":19}
# print(student)

# name=input("Enter student name:")
# if name in student_details1:
#     print("marks:",student_details1[name]["marks"])
# else:
#     print("student not found")


# data={
#     "Rahul":85,
#     "Aman":90,
#     "Neha":78
# }
# sorted_dict=dict(sorted(data.items(),key=lambda x:x[1]))
# print(sorted_dict)

# data={
#     "a":10,
#     "b":20,
#     "c":10,
#     "d":30

# }
# unique_dict={}

# for key,value in data.items():
#     if value not in unique_dict.values():
#         unique_dict[key]=value
# print(unique_dict)

# import json
# data={
#     "name":"Rahul",
#     "age":20,
#     "marks":85
# }
# json_data=json.dumps(data)
# print(json_data)

# data={
#     "a":10,
#     "b":20,
#     "c":30
# }
# Values=list(data.values())
# if len(Values) ==len(set(Values)):
#     print("All values are unique")
# else:
#     print("Duplicate values found")










