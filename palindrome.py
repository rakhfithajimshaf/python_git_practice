print("Palindrome")
n=input("Enter the string: ")
rev=""
for i in n:
    rev=i+rev
if n==rev:
    print("palindrome")
else:
    print("not palindrome")
 