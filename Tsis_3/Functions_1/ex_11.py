def palindrome(stroka):
    stroka2 = list(reversed(stroka))
    stroka2 = "".join(stroka2)
    if stroka == stroka2:
        print("Yes, it is palindrome!")
    else:
        print("No, it is not palindrome!")    

stroka = input()
palindrome(stroka)    
