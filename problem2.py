a=input("Enter the string1:")
b=input("Enter the string2:")
if (sorted(a)==sorted(b)):
    print(f"{a} and {b} are anagrams of each other")
else:
    print(f"{a} and {b} are not anagrams of each other")