class emp:
 ecount=0;
 def __init__(self,ename,eadd,eid,esal):
  self.ename=ename
  self.eadd=eadd
  self.eid=eid
  self.esal=esal
  b=20
  print(b)
 def display(self):
  print(self.ename,self.eadd,self.eid,self.esal)
  a=10
  print(a)
e1=emp("PK","bbsr",1,10000)
e1.display()
e2=emp("harry","jpr",2,20000)
e2.display()
e3=emp("tan","bbsr",3,30000)
e3.display()
e4=emp("sk","bbsr",4,50000)
e4.display()
print(emp.ecount)
print(e1.ecount)