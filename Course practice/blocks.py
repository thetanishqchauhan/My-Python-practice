age = int(input("Please enter your age: "))

if age < 18:
    print("You're not eligible to vote.\nPlease come back in {0} years".format(18-age))
elif age == 900:
    print("Please go back to your grave, sir.\n")
else:
    print("Press the 'Lotus' button for BJP.\n")