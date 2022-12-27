def extract_specialcharacters(s):
    temp_specialcharacters=0
    for i in s:
        if i not in 'aeioubcdfghjklmnpqrstvwxyzAZQXSWCDEVFRBGTNHYMJUKILOP1234567890':
            temp_specialcharacters+=i
    return temp_specialcharacters

str1=input()
a=extract_specialcharacters(str1)
print("no of specialcharacters in:",a)
