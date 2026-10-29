print("Armstrong")
num=int(input("Enter a num :"))
sum=0
temp=num
digit=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==num:
    print("arms")
else:
    print("not")
