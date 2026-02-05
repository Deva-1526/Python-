a=30
b=20

var=a
a=b
b=var
print("with using variable")
print("swapping:")
print("a=", a)
print("b=",b)

a=40
b=30
a,b = b,a
print("without using variable")
print("swapping:")
print("a=", a)
print("b=",b)

