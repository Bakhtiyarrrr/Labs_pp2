import os
path = "Labs_pp2/Tsis_3/Classes/ex_1.py"
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.X_OK))
# file = open(path, "r")
# print(file.read())
