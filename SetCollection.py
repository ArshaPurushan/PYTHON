a=input("Enter first collection of integer: ")
b=input("Enter second collection of integer: ")
a=set(map(int,a.split(',')))
b=set(map(int,b.split(',')))
print("List of same length: ",len(a)==len(b))
print("Sum of same value: ",sum(a)==sum(b))
print("Common Elements: ",bool(len(a&b)))

