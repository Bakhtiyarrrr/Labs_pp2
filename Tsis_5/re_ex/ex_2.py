import re
text = input()
match = re.findall(r"ab{2,3}",text)
print(match)