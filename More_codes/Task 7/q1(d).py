l=[] 
l2=[]
with open("names.txt","r") as n:
    for i in n:
        l.append(i.strip())
with open("names.txt",'w') as f:
    for i in l:
        f.write(i+"\n") 
with open("names.txt",'r') as f:
    lines = f.readlines()
    for i in lines:
            l2.append(i[:-1]) 
with open("names_roll.txt",'w') as f:
    for i in l2:
        roll= input("Enter your roll number.")
        f.write(i+" "+roll+"\n")
f=open("names_roll.txt","r")
print(f.read())