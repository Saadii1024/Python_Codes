import math
def cylinder (r,h):

    #circumfrance of a cylinder calculation
    c = 2*math.pi*r
    
    #volume of a cylinder calculation
    v = math.pi*r**2*h
    
    print("Circumfrance of cylinder is:",c)
    print("Volume of cylinder is:",v)


#taking value of radius from user
r = float(input("Enter radius: "))
    
#taking value of height from user
h = float(input("Enter height: "))

cylinder(r,h)

