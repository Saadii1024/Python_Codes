def sum_1(d):
    
    count = 0
    for k in d:
        v = d[k]
        print(k, "=", v)
        count += 1
    print("------------------------")
    if count % 2 == 0:
        print ("The sum is even")
    else:
        print ("The sum is odd")
d= { "Name": "Saad" , "Age" : "21" , "Hobby" : "Gaming" }
sum_1(d)
