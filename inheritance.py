class A:
 def x1 (self):
  print("1")
class B(A):
 def x2 (self):
  print("2")
class D(A):
 def x3(self):
  print("3")
class C(B):
 def x4(self):
  print("4")
class E(B,D):
 def x5(self):
  print("5")
ob=D()
ob1=C()
ob2=E()
ob.x1()
ob2.x2()
ob2.x3()
ob1.x4()
ob2.x5()