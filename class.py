#To calculate sum of series:1^1/1+2^2/2+3^3/3+.....n^n/n   
n=int(input("Enter the value of n:"))
a=0
for i in range(1,n+1):
 s=(i**i)/i
 a=a+s
print("The sum of series:",a)
#To calculate sum of series of x/1!+x^2/2!+x^3/3!+....x^n/n!
n=(int(input("Enter the value of n:")))
x=(int(input("Enter the value of x:")))
F,sum=1,0
for i in range(1,n+1):
    sum=(x**i)/i
    F*=i
print("sum of series:",sum)    