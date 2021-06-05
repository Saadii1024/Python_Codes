def multiple():
    for n in range(1,50):
        if n%5==0 or n%3==0:
            print("Multiple of 5 and 3.")
        else:
            if n%5==0:
                print("Multiple of 5")
            elif n%3==0:
                print("Multiple of 3")
            else:
                print("Not a multiple of 3 and 5")
multiple()
