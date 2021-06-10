with open("names.txt","r") as n: #opening the text file 
    for l in n:
        print(l.strip()[-4:])