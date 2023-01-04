def printadd(a,b):
    return a+b
def printsub(a,b):
    return a-b
def printmul(a,b):
    return a*b
def printdiv (a,b):
    return a/b
def choice():
    print("+:addition");print("-:subtraction");
    print("*:multiplication")
    
    print("/:division");   print("q:quit")
    
    return
colorselect={"+":printadd,"-":printsub,"*":printmul,"/":printdiv}
while True:
    choice()
    selection=input("select an arthimetic operaton:")
    if selection=='q'or selection=='Q':break
    if((selection=='+')or (selection=='-')or
       
    (selection=='*')or (selection=='/')):
       n1=int(input("enter first no:"))
       n2=int(input("enter second no:"))
       z=colorselect[selection](n1,n2)
       print(n1,selection,n2,'=',z)
       
    
