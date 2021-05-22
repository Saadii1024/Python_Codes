x = int(input("Enter x coordinate point: "))
y = int(input("Enter y coordinate point: "))
if x>0 and y>0:
    print("I Quadrant")
elif x<0 and y>0:
    print("II Quadrant")
elif x<0 and y<0:
    print("III Quadrant")
elif x>0 and y<0:
    print("IV Quadrant")
