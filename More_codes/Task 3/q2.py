from math import pi
    
def AreaofCone(radius,height):
    area = pi * radius * height
    print("Area of the cone is ",area)
radius = float(input("Enter radius of cone: "))
height = float(input("Enter height of cone: "))

AreaofCone(radius,height)
