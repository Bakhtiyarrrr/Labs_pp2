text = input()
text = list(text)
for i in range(1,len(text)):
    if text[i].isupper() == True:
        text[i-1] = text[i-1] + "_"

stroka = "".join(text)
print(stroka.lower())



        
