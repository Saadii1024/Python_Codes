A = int(input("Enter classes held"))
B = int(input("Enter classes taken"))
percentage =  B/A * 100
if percentage <= 75:
    print("You are not allowed")
else:
    print('You are allowed to give exams')
