"Pratice question no 1"
# with open("data.txt","r") as f:
#     data=f.read()
#     print(data)

"Pratice question no 2"
# with open("number.txt","w") as file:
#      for i in range(1,11):
#          file .write(str(i)+"\n")

"pratice question no 3"
# with open("info.txt","r") as file:
#     data=file.read()
#     print(data)

"pratice question no 4"
# with open("info.txt","a") as file:
#     data=file.write("This is the end of the story")
#     print(data)

"pratice question no 5"
# with open("info.txt","r") as file:
#      lines=file.readlines()
#      print("Total number of lines:",len(lines))

"pratice question no 6"
# total=0
# with open("marks.txt","r") as file:
#     for line in file:
#         total+=int(line.strip())
# print("Total sum:",total)

"pratice question no 7"
# sentence=input("Enter a sentence:")
# with open("info.txt","w") as file:
#     file.write(sentence)
"pratice question no 8"
# with open("info.txt","r") as file:
#     for line in file:
#         if "python " in line:
#             print(line.strip())

"Pratice question no 9"
# with open("info.txt","r") as file:
#     text=file.read()
# words=text.split()
# print("Total words:",len(words))
# print("Total characters:",len(text))

"Pratice question no 10"
# with open ("info.txt","r") as src:
#     with open("desination .txt","w") as dest:
#         dest.write(src.read())


"pratice question no 11"
# f=open("info.txt","r")
# data=f.read()
# print(data)

"pratice question no 12"
# with open("number","w") as file:
#     for i in range(2,21,2):
#        file.write(str(i)+"\n")

"pratice question no 13"
# with open("number.txt","a") as file:
#     data=file.write("Hello my name is harsh dhakad now i am learning python ")
#     print(data)

"pratice question no 14"
# file =open("info.txt","r")
# content=file.read()

# if "Python" in content:
#     print("Python word present in the content")
# else:
#     print("Python word not present in the content")

# file.close()

"pratice question no 15"
# info_file=open("info.txt","r")

# new_file=open("new.txt","w")

# data=info_file.read()
# new_file.write(data)

# info_file.close()
# new_file.close()

# print("Data successfully copied from info.txt to new.txt")

"pratice question no 16"
# with open("info.txt","r") as file:
#     text=file.read()
# words=text.split()
# print("total words:",len(words))
# print("TOtal characters:",len(text))

"pratice question no 17"
# file =open("info.txt","r")
# count=0
# for line in file:
#     count+=1
# file.close()
# print("Total lines:",count)

"pratice question no 18"
# file=open("log.txt","r")
# for line in file:
#     if "error" in line:
#         print(line.strip())
# file.close()

"pratice question no 19"
# sentence=input("Enter a sentence")

# file=open("info.txt","a")
# file.write(sentence + "\n")
# file.close()

# print("Sentence successfully added to file")

"pratice question no 20"
# file =open("student.txt","r")
# names=file.readlines()
# file.close()

# names=[name.strip() for name in names]
# names.sort

# file=open("student.txt","w")
# for name in names:
#     file.write(name+"\n")

# file.close()
# print("Names sorted and written back to file")

"Pratice question no 21"

# with open("info.txt","w") as file:
#     data=file.write("My name is boby fisher and age is 29")
#     print(data)
"Pratice question no 22"
# with open("info.txt","r") as file:
#     data=file.read()
#     print(data)
"pratice question no 23"
# with open("info.txt","r") as file:
#     count=0
#     for line in file:
#         count+=1
#     print(count)

"pratice question no 24"
# with open("info.txt", "r") as file:
#     total_words = 0
#     for line in file:
#         words = line.split()
#         total_words += len(words)

# print(total_words)

"pratice question no 25"
# with open("info.txt","a") as file:
#     data=file.write("\nHello bsdk teri maa ka bharosha")
#     print(data)
"pratice question no 26"


# search_word = input("Enter a word: ")

# with open("info.txt", "r") as file:
#     content = file.read()

#     if search_word in content:
#         print("Word is present in the file")
#     else:
#         print("Word is not present in the file")

"Pratice question no 7"
# with open("info.txt","r") as f1:
#     data=f1.read()

# with open("copy,txt","w") as f2:
#     f2.write(data)
# print("File copied successfull")

"Pratice question no 8"
# with open("info.txt","r") as f:
#     content=f.read()
#     count=len(content)
# print("Total characters:",count)

"Remove Blank Lines"
# with open("info.txt","r") as f:
#     lines=f.readlines()
# with open("output.txt","w") as f:
#     for line in lines:
#         if line.strip() !="":
#             f.write(line)
# print("Blank lines removed")

"pratice question  no 30"
# with open("number.txt","w") as f:
#     f.write("Rahul 80\n")
#     f.write("Aman 80\n")
#     f.write("Neha 80\n")
# total=0
# count=0
 
# with open("number.txt","r") as f:
#     for line in f:
#         name,marks=line.split()
#         total+=int(marks)
#         count+=1
# average=total/count
# print("Average marks:",average)

"Pratice question no 31"
# with open("info.txt","w") as file:
#     data=file.write("Hello python")
#     print(data)
"Pratice question no 32"
# with open("info.txt","r") as file:
#     data=file.read()
#     print(data)
"Pratice question no 33"
# with open("info.txt","r") as file:
#     data=file.read()
#     print(data)
"Pratice question no 34"
# with open("info.txt","r") as file:
#     content=file.read()
#     count=len(content)
#     print("Total character ",count)
"Pratice question no 35"
# with open("info.txt","r") as file:
#     total_words=0
#     for line in file:
#         words=line.split()
#         total_words+= len(words)
# print(total_words)
"Pratice question no 36"
# total=0
# with open("marks.txt","r") as file :
#     for line in file:
#         total+=int(line.strip())
# print("Total sum:",total)

"Pratice question 37"
# search_word=input("Enter a word:")
# with open("info.txt","r") as file:
#     content=file.read()
#     if search_word in content:
#         print("Word is present in the file")
#     else:
#         print("Word is not present in the file")

"Pratice question 38"
# with open("info.txt","a") as file:
#     data=file.write("Hello java script")
#     print(data)

"Pratice question no 39"
# with open("info.txt","r") as f1:
#     data=f1.read()

# with open("Copy1.txt","w") as f2:
#     f2.write(data)
# print("file copied successfull")

"Pratice questionn 40"
# with open("info.txt","r") as f:
#     lines=f.readlines()
# with open("output.txt","w") as f:
#     for line in lines:
#         if line .strip()!="":
#             f.write(line)
# print("Blank lines removed")

"Pratice question no 41"
# with open("info.txt","w") as file:
#     data=file.write("My name is james bobby fishe Age is 90")
#     print(data)
"Pratice question no 42"
# with open("info.txt","r") as file:
#     data=file.read()
#     print(data)

"Pratice question no 43"
# with open("info.txt","r") as file:
 
#     count=0
#     for line in file:
#         count+=1
#     print("Total lines in files",count)

"Pratice question no 44"
# with open("info.txt","r") as file:
#     total_words=0
#     for line in file:
#         words=line.split()
#         total_words+=len(words)
# print(total_words)

"Pratice question no 45"
# with open("info.txt","r") as file:
#     content=file.read()
#     count=len(content)
#     print("Total character ",count)
"Pratice question no 46"
# search_word=input("Enter a word:")
# with open("info.txt","r") as file:
#     content=file.read()
#     if search_word in content:
#         print("Word is present in the file")
#     else:
#         print("Word is not present in the file")

"Pratice question no 47"
# with open("info.txt","a") as file:
#     data=file.write("\nhello")
#     print(data)



    




