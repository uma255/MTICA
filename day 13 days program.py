def printsunday():
    print("sunday")
def printmonday():
    print("monday")
def printtuesday():
    print("tuesday")
def printwednesday():
    print("wednesday")
def printthursday():
    print("thursday")
def printfriday():
    print("friday")
def printsaturday():
    print("saturday")
def choose():
    print("enter any number between 1-7")
daydict={ 1:printsunday,2:printmonday,3:printtuesday,4:printwednesday,5:printthursday,6:printfriday,7:printsaturday }
choose()
dayno=int(input())
if dayno>1 and(dayno<=7):
    daydict[dayno]()
else:
    print("invalid")
        
    
  
