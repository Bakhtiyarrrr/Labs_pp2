import re
text = input()
match = re.findall(r"a{1}[A_Za-z0-9]+b{1}", text)
print(match)