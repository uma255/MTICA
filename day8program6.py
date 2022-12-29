num1=input("enter a number:")
num2= input("enter a number:")
try:
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print("exception handled by lokesh kanagaraj")
except ValueError:
    print("exception handled by vikram ")
except Exception as ob:
    print(ob)
else:
    print(num1, '/' ,num2, '=', res)
finally:
    print("thanks")
print("visit again at python class at mtica")
