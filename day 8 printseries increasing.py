def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None


inpch=input("enter a character:")
inpnum=int(input("enter a no:"))
printSeriesIncreasing(inpch,inpnum)
print('-'*40)
printSeriesDecreasing(inpch,inpnum)   
    
