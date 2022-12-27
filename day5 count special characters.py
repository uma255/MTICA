def special_characters(s):
    n_special_characters=0
    for i in s:
        if i not in '01234567890aqzxswcderfvbgtnhymjukliopAZQXSWCDEVFRBGTNHYMJUKILOP':
            n_special_characters+=1
    return n_special_characters

str1=input()
a=special_characters(str1)
print("no of special characters in:'",str1,"' is",a)
