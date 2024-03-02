import re
text = input()
match = re.findall(r"\W*[A-Z][a-z0-9]*",text)
print(match)
t = match[0]
my_list = [t,]
for x in range(1,len(match)):
    stroka_1 = ''
    for y in match[x]:
        if y != " ":
            stroka_1 += y
    my_list.append(stroka_1)        

print(my_list)
stroka =" ".join(my_list)
print(stroka)
