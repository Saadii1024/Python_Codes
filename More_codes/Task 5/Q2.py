def unique(x):
    l = []
    
    for i in x:
        if not i in l:
            l.append (i)
    return l

l = [10,20,30,40,20,50,60,40]
unique(l)
