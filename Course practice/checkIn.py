alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter = input("Enter a character: ")

if letter in alphabet.casefold():
    print("{} is in the English Alphabet".format(letter))
else:
    print("I don't recognize that letter.")