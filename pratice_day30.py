import re
"re.findall"
# a="""John has scored 89 marks,
#     Lisa has scored 90 marks
#     David has scored 70 marks"""

# print(re.findall("\d+",a))
# print(re.findall(r'[A-Z][a-z]',a))

"re.compile"
# p=re.compile("[a-d]")
# print(re.findall(p,a))

"re.split()"
# print(re.split("\d+",a))

"re.escape()"
# print(re.escape(a))

"re.search()"
# print(re.search("\d+",a))

"Match object"
# a="John has scored 98 marks"
# match=re.search("\d+",a)
# print(match)
# print(match.re)
# print(match.string)
# print(match.start())
# print(match.end())
# print(match.span())
# print(match.group())

