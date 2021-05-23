x = input("Enter a character: ")
if x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or x=='8' or x=='9':
    print("It is a digit")
elif x=='' or x=='!' or x=='@' or x=='#' or x=='$' or x=='%' or x=='^' or x=='&' or x=='*' or x=='?' or x=='/'or x=='=':
    print ("It is a special character")
else:
    print("It is an alphabet")
    
