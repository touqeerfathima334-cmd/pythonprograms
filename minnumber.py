a=int(input("enter first number:"))
b=int(input("enter sec number:"))
c=int(input("enter third number:"))
min=a if a<b and a<c else b if b<c else c
print("minimum value:", min)
