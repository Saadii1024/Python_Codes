def search(x): 
    l2=[]
    l3=[]
    with open("names.txt","r") as n:
        for i in n:
            l2.append(i.strip())
        for l in l2:
            if x == l:
                l3.append(x)
                break
        if x in l3:
            return True
        else:
            return False
x=input("Enter the name:")
search(x)