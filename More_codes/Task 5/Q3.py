def sort(x):
    for i in range (len(l)):
        
        for j in range (i+1, len(l)):
            
            if l[i] < l[j]:
                l[i] , l[j] = l[j] , l[i]
    return l
l = [1,2,3,4]
sort(l)
