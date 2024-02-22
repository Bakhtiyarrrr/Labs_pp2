import re
text = input()
match = re.findall(r"[A-Z]{1}[[a-z]+",text)
print(match)

