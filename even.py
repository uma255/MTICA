def checkeven(num1):
    if num1%2==0:
        return"even"
    return None
def checkodd(num1):
    if num1%2==1:
        return"odd"
    return None
num=int(input("enter a number:"))
x=checkeven(num)
y=checkodd(num)

print("x=",x)
print("y=",y)
print(checkeven(num))
print(checkodd(num))
        
