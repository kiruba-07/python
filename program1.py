n=list(range(1,11))
print("numbers from 1 to 10...\n",n)
for i in n:
    if(i%2==1):
        n.remove(i)
print("The values after removing odd numbers...\n",n)
