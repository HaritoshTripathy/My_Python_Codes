a=10
b=input("Enter any No")
c=int(b)
total=a/c
print("total")
except ZeroDivisionError:
print("hi")
except ValueError:
print("Plz don't leave blank input/if string don't pass a string")
