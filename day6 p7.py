import time
import sys
inpNo =int(input("enetr a no:  "))
start=time.time()
for i in range(inpNo):
    print("i=",1,"i^2=",1*i)
print("time taken byloop:",
      (time.time()-start)*100000)
