def printblue():
    print('you choose blue!\n')
    return
def printred():
    print('you choose red!\n')
def printorange():
    print('you choose orange!\n')
def printyellow():
    print('you choose yellow!\n')
def choice():
    print("0:blue")
    print("1:red")
    print("2:orange")
    print("3:yellow")
    print("4:quit")
    return
colorselect={0:printblue,1:printred,2:printorange,3:printyellow}
selection=0
while True:
    if selection==4:break
    choice()
    selection=int(input("selection a color option"))
    if (selection>=0)and(selection<4):
        colorselect[selection]()
                  
    




