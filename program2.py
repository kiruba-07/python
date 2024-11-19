# Write a program to check the given number is palindrome or not.
n=int(input("Enter the number:"))
a=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if a==rev:
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")
            
