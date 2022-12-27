#string='''pratice problems for list comprehension in python.'''
#print(string.count(' '))
ans=[]
for i in string:
    if i == ' ':
        ans.append(i)
print(len(ans))
print(string.count(' '))
