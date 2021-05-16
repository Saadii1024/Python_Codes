marks = int(input("Enter your marks: "))

if marks <= 80 and 100:
    print("grade A")
elif marks <= 60 and 80:
    print("grade B")
elif marks <= 50 and 60:
    print("grade C")
elif marks <= 45 and 50:
    print("grade D")
elif marks <= 25 and 45:
    print("grade E")
elif marks >= 25:
    print("grade F")
    