def check(x,d):

    l = []
    for k in d:
        l.append(k)
    if x in l:
        return True
    else:
        return False
d= { "Name": "Saad" , "Age" : "21" , "Hobby" : "Gaming" }
x = input("Enter the word:")
check(x,d)
    
