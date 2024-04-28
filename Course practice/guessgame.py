answer = 5

print("There's an answer stored in the code.")
print("You have to guess this number between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print("Please guess higher...")
#     guess = int(input())
#     if guess == answer:
#         print("You got it right.")
#     else:
#         print("You Lost!")

# elif guess > answer:
#     print("Please guess lower...")
#     guess = int(input())
#     if guess == answer:
#         print("You got it right.")
#     else:
#         print("You Lost!")

# else:
#     print("You got it the first time.")


# ------------------ same same but different ------------------- #

if guess != answer:
    if guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
    
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it right.")
    else:
        print("Sorry, you did not guess it right.")
else:
    print("Congrats! You got it the first time.")