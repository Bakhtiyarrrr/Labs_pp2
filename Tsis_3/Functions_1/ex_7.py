def has_33(numbers):
    m = False
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            break
        if numbers[i] == 3 and numbers[i+1] == 3:
            m = True
            break
    return m  
numbers = [int(value) for value in input().split()]      
print(has_33(numbers))

