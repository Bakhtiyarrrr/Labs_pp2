import re
text = input()
match = re.findall(r"\W*[A-Z][a-z]*",text)
stroka =" ".join(match)
print(stroka)

