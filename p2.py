def removespecialcharacter(s):
    ans=[]
    for i in s:
        if i in '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
            ans.append(i)
    return ''.join(ans)
inp=input()
print(removespecialcharacter(inp))
