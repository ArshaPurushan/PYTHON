a=input("enter list of word: ")
n=int(input("Enter a number: "))
b=a.split(',')
c=list(b)
print("list, ")
for i in c:
    if len(i)>n:
        print(i)
