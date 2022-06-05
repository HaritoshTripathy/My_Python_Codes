class cake:
 def show(self,qty,price):
  total=qty*price
  return total
ob=cake()
qty=eval(input("enter the quantity"))
price=eval(input("enter the price"))
total=ob.show(qty,price)
print("total price is", total,"/-")