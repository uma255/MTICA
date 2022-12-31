fo=open(r"D:\PYTHON practise 63\DAY10\filehaandling.txt","a")
for i in range(5):
    inpstr=input("enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file")
