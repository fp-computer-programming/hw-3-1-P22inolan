# Author: IBN (AMDG) 9/30/2021
card_total = input("What is the total of your cards? ")

if int(card_total) <= 21:
    print("You're safe!")
else:
    print("You bust!")
