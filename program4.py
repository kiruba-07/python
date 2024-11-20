#Remove repeated characters from the string
'''s=input("Enter the string:")
new=""
for i in s:
    if i not in new:
        new=new+i
print(new)'''
#Remove vowels from the string
s=input("Enter the string:")
vowels="AaEaIiOoUu"
temp=""
for i in s:
    if i not in vowels:
        temp=temp+i
print(temp)        


