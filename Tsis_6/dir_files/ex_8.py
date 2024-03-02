import os
path = "Labs_pp2/Tsis_6/dir_files/files/B.txt"
if os.access(path, os.F_OK) == True:
    os.remove(path)
else:
    print("This path doesn`t exist!")