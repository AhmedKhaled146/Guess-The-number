from random import randint

number_guessing = randint(1, 10)
print("##### Guess The Number You Have 3 Chance To Find The Right Number From 1 To 10. #####")
# print(number_guessing) ===> print the guessing number for test
person_expectation = int(input("Guess the number: "))

tries = 3

while person_expectation != number_guessing :
    tries -= 1
    print(f" ---> wrong guess, you have {tries} chance.")
    person_expectation = int(input("Guess the number: "))
    if tries == 1 and person_expectation != number_guessing:
        print("You have had 3 attempts to guess the number Sorry you lost. ")
        print(f"The Right Number is {number_guessing}")
        break
    else:
        continue
else:
    print(" ---> Wonderful Correct Guess, You Won", end=" ")
    print(f"The Right Number is Exactly {number_guessing}")