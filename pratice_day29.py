"Special Sequences in Regular Expression"

import re
 #\A
# a="harry potter"
# match=re.search(r"\Ahar",a)
# print(match)

#\b
# a="harry potter"
# match=re.search(r"\bpo",a)
# print(match)

#\B
# a="harry potter"
# match=re.search(r"\B",a)
# print(match)

#\d
# a="harry1 potter2345"
# match=re.findall(r"\d",a)
# print(match)


#\D
# a="harry1 potter234@5"
# match=re.findall(r"\D",a)
# print(match)

#\s
# a="harry1 po tter2345"
# match=re.findall(r"\s",a)
# print(match)

#\S
# a="harry1 po tter2345"
# match=re.findall(r"\S",a)
# print(match)

#\w
# a="harry1 po tter2345"
# match=re.findall(r"\w",a)
# print(match)

#\W
# a="harry1 po tter2345"
# match=re.findall(r"\W",a)
# print(match)

#\Z
# a="harry1 po tter2345"
# match=re.findall(r"S\Z",a)
# print(match)

"Regural Expression sets"
a="Charlie and chocolate factory"
b="123john#@^6+-+-773"

#[atx]
# match=re.findall("[atx]",a)
# print(match)

#[^atx]
# match=re.findall("[^atx]",a)
# print(match)

#[c-y]
# match=re.findall("[a-b]",a)
# print(match)

#[0123]
# match=re.findall("[0123]",b)
# print(match)

#[0-9]
# match=re.findall("[0-9]",b)
# print(match)


#[0-7][0-9]
# match=re.findall("[0-7][0-9]",b)
# print(match)

#[a-zA-Z]
# match=re.findall("[a-zA-Z]",a)
# print(match)

#[+]
match=re.findall("[+-]",b)
print(match)