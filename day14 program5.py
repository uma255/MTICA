class wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grr...")

class dog(wolf):
     def bark(self):
        print("woof")
   
pet1=dog("tomy","brown")
pet1.bark()
pet2=wolf("jimmy","grey")
pet2.bark()
dog("abc","xyz").bark()
