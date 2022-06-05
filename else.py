try:
 a=10/0
 print(a)
except ZeroDivisionError:
 print("error")
else:
 print("ok")
finally:
 print("thank you")