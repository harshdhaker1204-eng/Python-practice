import re
"Pratice question no 1"
# txt="banana rain river"
# x=re.findall("[arn]",txt)
# print(x)

"Pratice question no 2"
# txt="banana rain river"
# x=re.findall("[i]",txt)
# print(x)
# print(len(x))

"Pratice question no 3"
# txt="python mango zebra"
# x=re.findall("[a-n]",txt)
# print(x)

"Pratice question no 4"
# txt="hello world notebook"
# x=re.findall(r"[a-n]",txt)
# print(x)

"Pratice question no 5"
# txt="983201723"
# x=re.findall(r"[0123]",txt)
# print(x)


"Pratice question no 6"
# txt="120349876321"
# x=re.findall(r"[0123]",txt)
# print(x)
# print(len(x))

"Pratice question no 7"
# txt="My roll number is 45 and age is 20"
# x=re.findall(r"[0-9]",txt)
# print(x)

"Pratice question no 8"
# txt="A1B2C3D4"
# x=re.findall(r"[0-9]",txt)
# print(x)

"Pratice question no 9"
# txt="banana"
# x=re.findall("[^arn]",txt)
# print(x)

"Pratice question no 10"
# txt="orange"
# x=re.findall("[^arn]",txt)
# print(x)

"Pratice question no 11"
# txt="Time 12:45,09:59,07:6`"
# x=re.findall("[0-9][0-9]",txt)
# print(x)

"Pratice question no 12"
# txt="11 24 54 68 03 99"
# x=re.findall("[0-5][0-5]",txt)
# print(x)

"Pratice question no 13"
# txt="PytHon123@Code"
# x=re.findall("[a-zA-Z]",txt)
# print(x)

"Pratice question no 14"
# txt="Hello@2026#World"
# x=re.findall("[a-zA-Z]",txt)
# print(x)

"Pratice question no 15"
# txt="a+b+c+d"
# x=re.findall("[+]",txt)
# print(x)

"Pratice question no 16"
# txt="10+20-5+30+40"
# x=re.findall("[+]",txt)
# print(x)
# print(len(x))


"Loops pratice question"
"pratice question no 1"
# n=5
# num=2

# for i in range(1,n+1):
#     for j in range(i):
#         while True:
#             prime=True
#             for k in range(2,int(num**0.5)+1):
#                 if num%k==0:
#                     prime=False
#                     break
#             if prime:
#                 print(num,end=" ")
#                 num+=1
#                 break
#             num+=1
#     print()

"pratice question no 2"

# arr=[1,2,3,5,6,7,8,10]
# longest=1
# current=1

# for i in range(1,len(arr)):
#     if arr[i]==arr[i-1]+1:
#         current+=1
#     else:
#         current = 1
#     if current>longest:
#         longest=current
# print("Longest sequence length",longest)

"pratice question no 3"
# n=2
# num=1
# rows=[]

# #store triangle rows
# for i in range(1,n+1):
#     temp=[]
#     for j in range(i):
#         temp.append(num)
#         num+=1
#     rows.append(temp)
# #Print  rotated triangle
# for row in rows[::-1]:
#     for value in row[::-1]:
#         print(value,end=" ")
#     print() 













