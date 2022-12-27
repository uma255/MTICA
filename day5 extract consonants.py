def extract_consonants(s):
    temp_consonants=0
    for i in s:
        if i in 'qzwsxdcfvrbgtnhymjklp':
            temp_consonants+=1
    return temp_consonants

str1=input()
a=extract_consonants(str1)
print("consonents:",a)

