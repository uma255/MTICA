def printseries(n):
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(i,end=' ')
            num+=1
    return None
inpnum=int(input())
printseries(inpnum)
