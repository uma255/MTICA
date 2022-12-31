fo1=open(r"D:\PYTHON practise 63\DAY10\filehaandling.txt","r")
fo2=open(r"D:\PYTHON practise 63\DAY10\master.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("file copied")
