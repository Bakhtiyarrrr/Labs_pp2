def unique_list(tiktak, length):
   # Помечаем дубликаты меткой true
    for i in range(2):
        for j in range(length):
           for k in range(2):
               r = j + 1
               while r < length:
                   if r == length:        
                       break
                   if tiktak[i][j] == tiktak[k][r]:
                       tiktak[k+1][r] = True
                   r += 1
               break 
        break
   # Добавляем элементы которые остались false, это и есть уникальные элементы
    new_tiktak = []
    for i in range(2):
        for j in range(length):
            if tiktak[i+1][j] == False:
                new_tiktak.append(tiktak[i][j])
        break
    return new_tiktak



tiktak = []
my_list = [x for x in input().split()]
tiktak.append(my_list)
my_list_bools = []
for i in range(len(my_list)):
    my_list_bools.append(False)
tiktak.append(my_list_bools)
print(unique_list(tiktak, len(my_list)))
