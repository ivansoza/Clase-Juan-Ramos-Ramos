L1 = [1,2,3.0,'a','b','c',True,['X','Y','Z']]
print (L1)
print("Recorrido de la lista:")
numero=len(L1)
print(numero)
for i in range(3,len(L1)): 
    print ("El recorrido del valor:" ,i,"  ",L1[i])
  
#SLICES- REBANADA#

print(L1[0:4])
print(L1[:4])
print(L1[3:4])
print(L1[4:])

L1.extend(["Nuevo Valor"])
print(L1)

