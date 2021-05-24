def bill(x,y,z):
    if z <= 199:
        ebill = z*1.20
    elif z>= 200 and z<400:
        ebill = z*1.50
    elif z>= 400 and z<600:
        ebill = z*1.80
    elif z>=600:
        ebill = z*0.15
    print("Your total bill is:",ebill)
    
a = input("Enter your name")
b = input("Enter your id")
c = int(input("Enter unit consumed"))
bill(a,b,c)
