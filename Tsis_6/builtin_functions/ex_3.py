def palindrome(stroka):
    inverse_str = stroka[::-1]
    if inverse_str == stroka:
        print("it is a palindrome!")
    else:
        print("it is not palindrome!")

stroka = input()
palindrome(stroka)