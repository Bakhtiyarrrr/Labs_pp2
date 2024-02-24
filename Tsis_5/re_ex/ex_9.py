import re
text = input()
match = re.findall(r"\W*[A-Z][a-z]*",text)
stroka =" ".join(match)
print(stroka)
#изначально вводится сплошная строка по типу HelloMyNameIsBakhtiyar, и между ими ставится пробел
