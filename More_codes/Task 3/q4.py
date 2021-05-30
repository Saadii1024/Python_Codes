def convert(x):
    
    #converting pounds into grams
    grams = 453.59237*x
    
    #converting pounds into kilograms
    kilo = 0.454 *x
    
    print("Pounds in Gram =", grams)
    print("Pounds in kilogram =", kilo)
    
#taking quantity in pounds from user
x=int(input("Enter the quantity in pounds: "))
convert(x)
