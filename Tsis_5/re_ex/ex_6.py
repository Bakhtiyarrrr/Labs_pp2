import re
text = input()
match = re.sub("\s|,|.^\w" , ":", text)

print(match)