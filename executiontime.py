from time import*
t1=perf_counter()
print(t1)
i,sum=0,0
while(i,2000000):
 sum+=i
 i+=1
print(sum)
t2=perf_counter()
print('execution time=%F seconds'% (t2-t1))