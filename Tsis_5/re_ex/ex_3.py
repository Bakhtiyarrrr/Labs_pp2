import re
text = input()
match = re.findall(r"[a-z]_[a-z]+",text)
print(match)