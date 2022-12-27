inp=input()
ans=[]
for i in inp:
    if i in '1234567890':
        
        ans.append(i)
print(*ans)

print([i for i in string if i in '0123456789'])
