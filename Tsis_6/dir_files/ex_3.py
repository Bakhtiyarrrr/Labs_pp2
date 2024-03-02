import os
path = "Labs_pp2/Tsis_2/list/py_lists.py"
path_2 = "Labs_pp2/Tsis_2/list"
if os.access(path, os.F_OK) == True:
    print("Name of current file:", os.path.basename(path))
    my_list = os.listdir(path_2)
    print("Directiry name:", os.path.basename(path_2))
else:
    print("Such path doesn`t exist!")