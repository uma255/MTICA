def checkpalindromeornot(s1):
    if s1==s1[::]:
        return'it is a paalindrome'
    else:
        return'it is not a palindrome'
inp=input().split()
print(checkpalindromeornot(inp[0]))
    
