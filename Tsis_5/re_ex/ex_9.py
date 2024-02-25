import re

stroka = input()
x = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', stroka)

while(x != re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', x)):
    x = re.sub(r'(?<=[A-Z])(?=[A-Z][a-z])', ' ', x)

print(x)
