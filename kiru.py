#To check leap year
year=2024
if(year%4==0 and year%200!=0)or(year%400==0):
    print(f"{year}is a leap year.")
else:
    print(f"{year}is not a leap year.")
#uppercase
a='apple'
print(a.upper())
print(a.islower())
#lowercase
b='FRUIT'
print(b.lower())
print(b.islower())

