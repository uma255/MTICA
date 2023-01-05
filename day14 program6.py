#indirect inheritance or multilevel inheritance
class a:
    def first_method(self):
        print("method of class a...")

class b(a):
    def second_method(self):
        print("method of class b...")
        
class c(b):
    def third_method(self):
        print("method of class c...")

if __name__=='__main__':
    ob=c()
    ob.first_method()
    ob.second_method()
    ob.third_method()


        
    
