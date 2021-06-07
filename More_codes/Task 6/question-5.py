max_min = {"0":0, "1":1, "2":4, "3":1, "4":6, "5":7}

highest = max(max_min, key= max_min.get)
hnumber = max(max_min.values())
print("highest number is:",hnumber)

lowest = min(max_min, key=max_min.get)
lnumber = min(max_min.values())
print("lowest number is",lnumber)
