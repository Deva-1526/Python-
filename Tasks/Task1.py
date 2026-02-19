#Hello world
a="Hello World !"
print(a)

#Add,Sub,Multiply,Divide,Modules of Two Numbers.
a=10
b=20
print("The addition of a & b:", a+b)
print("The subtraction of a&b:", a-b)
print("The multiplication of a&b:", a*b)
print("The division of a&b:", a/b)
print("The modulus of a&b:", a%b)

#Square Root 
num=int(input("Enter the number:"))
sqrt = num**0.5
print("Square root:", sqrt)

#Area of a Triangle 
base=30
height=50
area=0.5*base*height
print("Area of triangle:", area)

#Quadratic function
a=60
b=90
print("(a+b)^2=", a+b**2)
print("(a-b)^2=", a-b**2)
print("a^2-b^2=", (a**2)-(b**2))

#swap two variables with & without variable
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

#last digit of the number
num=38950
last_digit = num%10
print("Last digit:", last_digit)
#last two digit of the number
num=2346528
last_two_digit= num%100
print("Last two digit:",last_two_digit)

#Buzz number
n=int(input("Enter the number:"))
if n%7==0:
    print("Buzz number")
else:
    print("not buzz")
