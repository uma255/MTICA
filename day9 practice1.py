def printseriesincreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
def printseriesdecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpch=input("enter a character:")
inpnum=int(input("enter a no"))
printseriesincreasing(inpch,inpnum)
print('-'*40)
printseriesdecreasing(inpch,inpnum)
