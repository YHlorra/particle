letter =['','abc','def','ghi','jki','mno','pqrs','tuv','wyxz']
number =['1','2','3','4','5','6','7','8']

def use_numbers_to_repersent_words(words):
    reult = ''
    for i in range(len(words)):
        for w in range(len(letter)):
            if words[i] in letter[w]:
                reult +=number[w]
                break
    return reult

words =input("please input the string").lower()
print(use_numbers_to_repersent_words(words))