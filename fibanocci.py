num=int(input("Enter limit: ")) 
f1= 0 
f2= 1
f3=f1+f2 
print(f1) 
print(f2) 
while(f3<=num):
    f3=f1+f2 
    print(f3) 
    f1=f2 
    f2=f3 