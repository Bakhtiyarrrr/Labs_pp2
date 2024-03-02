path = "Labs_pp2/Tsis_6/dir_files/files/just_1.txt"
file = open(path, "r")
count = 0
for x in file.read():
    if x == "\n":
        count += 1
print(count + 1) # добавил 1 потому что у последней строки нет \n
file.close()