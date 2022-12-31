def fun( str1):
    print (str1)
    return
fun("i'm first call to user defined function!")
fun("again second call to the same function")

def printme(str1,n):
    n[0]='lokesh'
    print (str1,n)
    return
x=['ganguly','master']
printme("wakeup",x)
print('x:',x)

def changeme(lstn):
    lstn=('vikram','santanam','rolex')
    print(lstn)
    return
lst=[1,4,5,6,77]
print(changeme(lst))
print('lst:',lst)

def name(lstn):
    lstn=('uma','master','krack')
    print(lstn)
    return 0
print(name(lst))
