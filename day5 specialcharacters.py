def count_specialcharacters(s):
    n_specialcharacters=0
    for i in s:
        if i not in 'aeioubcdfghjklmnpqrstvwxyzAZQXSWCDEVFRBGTNHYMJUKILOP1234567890':
            n_specialcharacters+=1
    return n_specialcharacters

str1=input()
a=count_specialcharacters(str1)
print("no of specialcharacters in:'",str1,"'  is",a)
