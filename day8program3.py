def factorial(num):
    assert(num>=0),"factorial of neg no is not defined"
    assert(isinstance(num,int)),"factorial not defined for non integer"
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
try:
    print(factorial(-45))
except Exception as ab:
    print(ab)
try:
    print(factorial(4.3))
except Exception as ab:
    print(ab)
try:
    print(factorial(45))
except Exception as ab:
    print(ab)
try:
    print(factorial(2))
except Exception as ab:
    print(ab)
print("thankyou")
        
