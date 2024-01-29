def convert_to_ounces(grams:int):
    ounces = grams * 28.3495231
    return ounces
n = int(input())
print(convert_to_ounces(n))
