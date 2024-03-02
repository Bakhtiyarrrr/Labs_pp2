path = "Labs_pp2/Tsis_6/dir_files/files"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in alpha:
    y = x + ".txt"
    file = open(path + "/" + y, "w")
file.close()


    