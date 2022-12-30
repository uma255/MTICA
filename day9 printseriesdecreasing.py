def printseriesdecreasing(ch,n):
    assert isinstance(ch,str),'second case should be in str'
    assert isinstance(n,int),'second case should be in int'
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpch=input("enter a character:")
inpnum=int(input("enter a no"))
#printseriesincreasing(inpch,inpnum)
print('-'*40)
try:
    printseriesdecreasing(inpch,inpnum)
except AssertionError as ob:
    print(ob)
    

