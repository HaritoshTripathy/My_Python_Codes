class X:
 def m1 (self):
  print("no paramter")
 def m1 (self,a):
  print("1 parametre")
 def m1 (self,a,b):
  print("two parametre")
x1=X()
x1.m1(100,1000)
x1.m1(100,200)