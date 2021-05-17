characters = ['a','e','i','o','u']
B = input("Enter an alphabet: ")
for i in characters:
    if i == B:
        print("It is a vowel!")
        break
    else:
        print("It is not a vowel!")