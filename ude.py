class lesssalaryerror(Exception):
 def show (self):
  print("getting less salary")
class UDE:
 def main (self,sal):
  sal=eval(input("salary"))
  if (sal>10000):
   print("ok")
  else:
   try:
    raise lesssalaryException()
   except lesssalaryexceptionasob:
    ox=UDE()
   ox.main()