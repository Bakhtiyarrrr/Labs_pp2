import re
text = input()
match = re.findall(r"ab{0,}",text)
print(match)
