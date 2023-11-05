a=input("Enter a list: ")
b=a.split()
c=list(b)
l=[]
[l.append(i) for i in c if i not in l]
print("final result ",l)
