def printmonth(dn):
    if(dn==1):
        return 'january'
    elif(dn==2):
        return 'febravary'
    elif(dn==3):
        return 'March'
    elif(dn==4):
        return 'April'
    elif(dn==5):
        return 'May'
    elif(dn==6):
        return 'June'
    elif(dn==7):
        return 'July'
    elif(dn==8):
        return 'August'
    elif(dn==9):
        return 'September'
    elif(dn==10):
        return 'October'
    elif(dn==11):
        return 'November'
    elif(dn==12):
        return 'December'
    else:
        return None
def printmonth(dn):
    if(dn==1):
        return 'january'
    if(dn==2):
        return 'febravary'
    if(dn==3):
        return 'March'
    if(dn==4):
        return 'April'
    if(dn==5):
        return 'May'
    if(dn==6):
        return 'June'
    if(dn==7):
        return 'July'
    if(dn==8):
        return 'August'
    if(dn==9):
        return 'September'
    if(dn==10):
        return 'October'
    if(dn==11):
        return 'November'
    if(dn==12):
        return 'December'
    else:
        return dn
import time
for i in range(7):
    inpnum=int(input())
    start=time.time()
    print(printmonth(inpnum))
    print((time.time()-start)*100)
    start=time.time()
    print(printmonth(inpnum))
    print((time.time()-start)*100)
            
        
          
    
    
    
      
