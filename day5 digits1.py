def digits(s):
    n_digit=0
    for i in s:
        if i in '0123456789':
            n_digit+=1
    return n_digit

str1=input()
a=digits(str1)
print("digits'",str1,"' is",a )
