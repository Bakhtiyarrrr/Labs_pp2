import re
text = input()
match = re.split("_",text)
my_list = []
for x in match:
    my_list.append(x.capitalize())
print(my_list)


new_text = ""
new_text = ''.join(my_list)
print(new_text)
