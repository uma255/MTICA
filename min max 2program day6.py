lstEven=[]
lstodd=[]
while(True):
    inpnum=int(input("enter a value(-1 to end):"))
    if inpnum==-1:
        break
    elif inpnum%2==0:
        lstEven.append(inpnum)
    elif inpnum%2==1:
        lstodd.append(inpnum)
print("even:",*lstEven)
print("min:",(lstEven))
print("max:",(lstEven))
print("avg:",round(sum(lstEven)/len(lstEven),1))
      
print("odd:",*lstodd)
print("min:",(lstodd))
print("max:",(lstodd))
print("avg:",round(sum(lstodd)/len(lstodd),1))
      
    
