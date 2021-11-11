a=input("Enter sequence")
b=input("Enter matching case")
#print(a[0])
Nol=0
ol=0
for i in range(len(a)-2):
    if a[i]==b[0] and a[i+1]==b[1] and a[i+2]==b[2]:
        ol+=1
i=0
while i < len(a)-2:
    if a[i]==b[0] and a[i+1]==b[1] and a[i+2]==b[2]:
        Nol+=1
        i+=3
    else :
        i+=1




print("__________________________________ Sequence Detecter __________________________")        
print()
print()
print("Overlapping %s in %d instances."%(b,ol))
print("Non Overlapping %s in %d instances."%(b,Nol))
print()

print()
print("________________________________________________________________________________")
       
