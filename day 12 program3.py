class student:
    college="mtica"
    course='mca'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def displaystudent(self):
        print('name :'+self.name.title()+'\nroll.no:'+str(self.rollno))
        print('college :'+self.college+'\ncourse:'+self.course)
lstobj=[]
for i in range(2):
    n=input()
    r=int(input())
    temp='obj'+str(i)
    temp=student(n,r)
    lstobj.append(temp)
for i in lstobj:
    i.displaystudent()
