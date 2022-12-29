def checkevenodd(num1):
    assert(num1>0),"negative numbers"
    if num1%2==0:
        return "even"
    else:
        return "odd"

for i in range(3):
    num=int(input("enter a number"))
    try:
        print(num,"is",checkevenodd(num))
    except AssertionError as ob:
        print(ob)
