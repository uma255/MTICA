def factorial(num):
    assert(num>=0),"factorial of neg no is not defined"
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
try:
    print(factorial(3))
except Exception as ab:
    print(ab)
    
        
