import os
path = "Labs_pp2/Tsis_2"
print(os.listdir(path))
only_foilders = []
only_files = []
for x in os.listdir(path):
    if ".py" in x:
        only_files.append(x)
    else:
        only_foilders.append(x)
print(only_files)
print(only_foilders)