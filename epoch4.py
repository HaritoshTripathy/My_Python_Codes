from datetime import*
td=date.today()
print(td)
print(type(td))
str=td.strftime('%d.%B.%y')
print(str)
str1=td.strftime('%j')
print('To is',str1,'th day of the current year')
str2=td.strftime('%A')
print('Its.....',str2)