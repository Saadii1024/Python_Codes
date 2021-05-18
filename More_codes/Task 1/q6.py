
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))

if x == y == z:
    print("It is an Equalateral triangle!")
elif x != y != z:
    print("It is a Scalene traingle!")
elif x == y != z:
    print("It is an Isoceles triangle!")