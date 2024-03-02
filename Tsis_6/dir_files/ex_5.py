numbers = [x for x in input().split()]
stroka = " ".join(numbers)
path = "Labs_pp2/Tsis_6/dir_files/files/just_2.txt"
file = open(path, "w")
file.write(stroka)
file.close()
