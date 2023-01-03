class number:
    def __init__(self,n):
        self.n=n
    def calculatefactorial(self):
        if self.n==0:
            return 1
        res=1
        for i in range(1,self.n+1):
            res*=i
        return res
inp=int(input())
obj=number(inp)
print('factorial of ',inp,'is',obj.calculatefactorial())

