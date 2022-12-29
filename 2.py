def factorial(num):
    assert(num>=0),"neg no are not "
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
    
try:
    print(num(50))
except Exception as ab:
    print(ab)
    
        
