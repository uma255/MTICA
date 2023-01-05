class a:
    def first_method(self):
        print("method of class a....")

class b(a):
    def first_method(self):
        print("method of class b...")
        super().first_method()

ob=b()
ob.first_method()
