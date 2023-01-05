def reversestring(s):
    ans=[i[::-1]for i in s]
    return ans
    
inp=input().split()
print(inp)
print(*reversestring(inp))
