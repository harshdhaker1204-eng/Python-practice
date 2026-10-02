import re
"Pratice question no 1"

# txt="cafe hello naive"
# print(re.findall(r"\w+",txt,re.ASCII))

"Pratice question no 2"
# txt="cafe 34hello 11naive"
# print(re.findall(r"\d+",txt,re.ASCII))

"Pratice question no 3"
# txt="harshdhaker12@gmail.com"
# print(re.findall("harshdhaker12@gmail.com",txt,re.DEBUG))

"Pratice question no 4"
# txt="welcome to apna college"
# print(re.findall(r"ab+",txt,re.DEBUG))

"Pratice question no 5"
# txt = """<p>
# Hi
# my
# name
# is
# Sally
# </p>"""
# x=re.findall(r"<p>(.*?)</p>",txt,re.S)
# print(x)

"Pratice question no 6"
# txt="""
# Start
# Hello python 
# How are you
# End"""
# x=re.findall(r"Start(.*?)End",txt,re.S)
# print(x)

"Pratice question no 7"
# txt="Python PYTHON pYtHoN"
# x=re.findall(r"python",txt,re.IGNORECASE)
# print(x)

"Pratice question no 8"
# txt="Hello HELLO hElLO hELLO"
# x=re.findall(r"hello",txt,re.I)
# print(len(x))

"Pratice question no 9"
# txt="""
# #Python
# Hello
# #RegEx
# World
# #coding"""
# x=re.findall(r"^#.*",txt,re.MULTILINE)
# print(x)

"Pratice question no 10"
# text="""
# Hello.py$
# RegEx
# World.py$
# Python
# coding.py$"""
# x=re.findall(r".*\.py\$",text,re.M)
# print(x)

"Pratice question no 11"
# txt="My marks are 85 to 90"
# x=re.findall(r"\d",txt)
# print(x)

"Pratice question no 12"
# txt="Python PYTHON pYtHoN"
# x=re.findall(r"python",txt,re.I)
# y=re.findall(r"PYTHON",txt,re.NOFLAG)
# print("Ignorecase",x)
# print("No flag",y)

"Pratice question no 13"
# text = "Hello नमस्ते こんにちは Python"
# x=re.findall(r"\w+",text)
# print(text)

"Pratice question no 14"
# text = "123 ٤٥٦ ७८९"
# x=re.findall(r"\d+",text,re.UNICODE)
# print(x)

"Pratice question no 15"
# import re

# pattern = r"""
# ^               # Start of string
# \d{3}           # First 3 digits
# [- ]?           # Optional dash or space
# \d{3}           # Next 3 digits
# [- ]?           # Optional dash or space
# \d{4}           # Last 4 digits
# $               # End of string
# """

# text = "123-456-7890"

# x = re.findall(pattern, text, re.X)

# print(x)

"Pratice question no 16"
import re

pattern = r"""
^                   # Start of line
(0[1-9]|[12][0-9]|3[01])   # Day: 01-31
-                   # Dash separator
(0[1-9]|1[0-2])     # Month: 01-12
-                   # Dash separator
\d{4}               # Year: 4 digits
$                   # End of line
"""

text = """18-05-2026
31-12-2025
99-99-9999"""

x = re.findall(pattern, text, re.X | re.M)

print(x)

























