from array import*
import numpy as np


arr=np.array([['A','B','C','D'],['E','F','G','H'],['T','J','K','L'],['M','N','O','P'],['Q','R','S','T']])
target=input("Give target")

start='A'
print(target)
result = np.where(arr == target)
iT= int(result[0])
jT= int(result[1])
print("target place",iT,jT)

result = np.where(arr == start)
iS= int(result[0])
jS= int(result[1])
print("start place",iS,jS)

dist=((((iS-iT)*3)**2)+(((jS-jT)*5)**2))**0.5
print(dist)




    
