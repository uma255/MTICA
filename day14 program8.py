#indirect inheritance or multilevel inheritance
class a:
    def first_method(self):
        print("method of class a...")

class b:
    def first_method(self):
        print("method of class b...")
        
class c(a,b):
    def third_method(self):
        print("method of class c...")

if __name__=='__main__':
    ob=c()
    ob.first_method()
    ob.third_method()


        
    
