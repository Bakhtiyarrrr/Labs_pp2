def re_sentence(sentence:str):
    sentence = sentence.split()
    sentence = list(reversed(sentence))
    print(sentence)


sentence = input()
re_sentence(sentence)