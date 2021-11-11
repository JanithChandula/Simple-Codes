print("__________________________________ Sequence Detecter ___________________________")        
print()
print("You can find repitetion of binary code in a binary sequence using this program")
print()
print("________________________________________________________________________________")
print(" *** ALL INPUTS MUST BE BINARY *** ")

print("________________________________________________________________________________")
a=input("Enter sequence : ")
b=input("Enter matching case : ")
#print(a[0])
Nol=0
ol=0
for i in range(1+len(a)-len(b)):
    
    if b==a[i:i+len(b)]:
        
        ol+=1
   

i=0    
while i< 1+len(a)-len(b):
    if b==a[i:i+len(b)]:
        
        Nol+=1
        i+=3
    else :
        i+=1
    
print()
print("________________________________________________________________________________")
print("                                        Results                                ")
print("________________________________________________________________________________")       

print()

print("Overlapping %s in %d instances."%(b,ol))
print("Non Overlapping %s in %d instances."%(b,Nol))
print()

print()
print("________________________________________________________________________________")
       
