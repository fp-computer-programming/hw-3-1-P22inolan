x = input("Give me a number. ")

if int(x) % 2 == 0:
    print("Your number is a multiple of 2.")
if int(x) % 3 == 0:
    print("Your number is a multiple of 3.")
if int(x) % 5 == 0:
    print("Your number is a multiple of 5.")
else:
    print("Your number is not a mulitple of 2, 3, or 5.")
