import random
print("The Number Guessing Game!")
name = input("what is your name?: ")  # this takes the user's name
print(("Welcome ") + (name))
play = input(("Do you want to play my high low number guessing game? ") + (name) + (" (yes or no): "))    # this asks the user if they want to play
repeats1 = 0

while (repeats1 == 0 ):
    repeats = 0
    guesses = 0
    while (repeats == 0):
        if (play == "yes") or (play == "y") or (play == "Y") or (play == "ya") or (play == "ok") or (play == "of course") or (play == "yah"):  # this decides what happens when the user chooses yes
            mode = input(("Well, ") + (name) + (". What difficulty would you like ? easy, medium or hard?: "))

            if (mode == "easy") or (mode == "e") or (mode == "E"):  # this decides whats the number if the user chooses easy
                number = random.randint(1,20)
                compnum = number
                print((name) + (", I am thinking of a number between 1 and 20, can you guess it?"))
                while guesses < 10:  # this is how many times this program will loop
                    guess = int(input("Take a guess: "))  # this is where the user inputs their guess
                    guesses = guesses + 1

                    if guess == compnum + 6:  # this portion tells the user if they are getting closer
                        print ("your close")
                    elif guess == compnum + 5:
                        print ("your close")
                    elif guess == compnum + 4:
                        print ("your close")
                    elif guess == compnum + 3:
                        print ("your very close")
                    elif guess == compnum + 2:
                        print ("your very close")
                    elif guess == compnum + 1:
                        print ("your very close")

                    elif guess == compnum - 6:  # this portion tells the user if they are getting closer
                        print ("your close")
                    elif guess == compnum - 5:
                        print ("your close")
                    elif guess == compnum - 4:
                        print ("your close")
                    elif guess == compnum - 3:
                        print ("your very close")
                    elif guess == compnum - 2:
                        print ("your very close")
                    elif guess == compnum - 1:
                        print ("your very close")

                    elif guess == compnum:
                        print (" ")
                    else:
                        print("not even close")

                    if guess < number:  # this tells you whether your guess is too high
                        print('Your guess is too low.')
                    elif guess > number:  # this tells you whether your guess is too low
                        print('Your guess is too high.')
                    elif guess == number:  # this is what happens if the user's guess matches the number
                        guessesTaken = str(guesses)
                        print('Good job, ' + name + '! You guessed my number in ', guesses, ' guesses!')
                        repeats = repeats + 1
                        break
                    elif guesses == 10:  # this is what happens when you run out of tries
                        if guess != number:
                            number = str(number)
                            print(("that wasn’t the number I was thinking of was,") + (number))

            elif (mode == "medium") or (mode == "m") or (mode == "M"):  # this statement decides what the number is if the user chooses medium
                number = random.randint(1,50)
                compnum = number
                print((name) + (", I am thinking of a number between 1 and 50, can you guess it?"))
                while guesses < 10:  # this is how many times this program will loop
                    guess = int(input("Take a guess: "))  # this is where the user inputs their guess
                    guesses = guesses + 1

                    if guess == compnum + 10:  # this portion tells the user if they are getting closer
                        print ("your close")
                    elif guess == compnum + 9:
                        print ("your close")
                    elif guess == compnum + 8:
                        print ("your close")
                    elif guess == compnum + 7:
                        print ("your close")
                    elif guess == compnum + 6:
                        print ("your getting closer")
                    elif guess == compnum + 5:
                        print ("your getting closer")
                    elif guess == compnum + 4:
                        print ("your getting closer")
                    elif guess == compnum + 3:
                        print ("your very close")
                    elif guess == compnum + 2:
                        print ("your very close")
                    elif guess == compnum + 1:
                        print ("your very close")

                    elif guess == compnum - 10:  # this portion tells the user if they are getting closer
                        print ("your close")
                    elif guess == compnum - 9:
                        print ("your close")
                    elif guess == compnum - 8:
                        print ("your close")
                    elif guess == compnum - 7:
                        print ("your close")
                    elif guess == compnum - 6:
                        print ("your getting closer")
                    elif guess == compnum - 5:
                        print ("your getting closer")
                    elif guess == compnum - 4:
                        print ("your getting closer")
                    elif guess == compnum - 3:
                        print ("your very close")
                    elif guess == compnum - 2:
                        print ("your very close")
                    elif guess == compnum - 1:
                        print ("your very close")

                    elif guess == compnum:
                        print (" ")
                    else:
                        print("not even close")

                    if guess < number:  # this tells you whether your guess is too high
                        print('Your guess is too low.')
                    if guess > number:  # this tells you whether your guess is too low
                        print('Your guess is too high.')
                    if guess == number:  # this is what happens if the user's guess matches the number
                        guessesTaken = str(guesses)
                        print('Good job, ' + name + '! You guessed my number in ', guesses, ' guesses!')
                        repeats = repeats + 1
                        break
                    if guesses == 10:
                        if guess != number:  # this is what happens when you run out of tries
                            number = str(number)
                            print(("that wasn’t the number I was thinking of was,") + (number))

            elif (mode == "hard") or (mode == "h") or (mode == "H"):  # this chooses what the number is if the user chooses hard
                number = random.randint(1,100)
                compnum = number
                print((name) + (", I am thinking of a number between 1 and 100, can you guess it?"))
                while guesses < 10:  # this is how many times this program will loop
                    guess = int(input("Take a guess: "))  # this is where the user inputs their guess
                    guesses = guesses + 1

                    if guess == compnum + 10:  # this portion tells the user if they are getting closer
                        print ("your close")
                    elif guess == compnum + 9:
                        print ("your close")
                    elif guess == compnum + 8:
                        print ("your close")
                    elif guess == compnum + 7:
                        print ("your close")
                    elif guess == compnum + 6:
                        print ("your getting closer")
                    elif guess == compnum + 5:
                        print ("your getting closer")
                    elif guess == compnum + 4:
                        print ("your getting closer")
                    elif guess == compnum + 3:
                        print ("your very close")
                    elif guess == compnum + 2:
                        print ("your very close")
                    elif guess == compnum + 1:
                        print ("your very close")

                    elif guess == compnum - 10:  # this portion tells the user if they are getting closer
                        print ("your close")
                    elif guess == compnum - 9:
                        print ("your close")
                    elif guess == compnum - 8:
                        print ("your close")
                    elif guess == compnum - 7:
                        print ("your close")
                    elif guess == compnum - 6:
                        print ("your getting closer")
                    elif guess == compnum - 5:
                        print ("your getting closer")
                    elif guess == compnum - 4:
                        print ("your getting closer")
                    elif guess == compnum - 3:
                        print ("your very close")
                    elif guess == compnum - 2:
                        print ("your very close")
                    elif guess == compnum - 1:
                        print ("your very close")

                    elif guess == compnum:
                        print (" ")
                    else:
                        print("not even close")

                    if guess < number:  # this tells you whether your guess is too high
                        print('Your guess is too low.')
                    if guess > number:  # this tells you whether your guess is too low
                        print('Your guess is too high.')
                    if guess == number:  # this is what happens if the user's guess matches the number
                        guessesTaken = str(guesses)
                        print('Good job, ' + name + '! You guessed my number in ', guesses, ' guesses!')
                        repeats = repeats + 1
                        break
                    if guesses == 10:
                        if guess != number:  # this is what happens when you run out of tries
                            number = str(number)
                            print(("that wasn’t the number I was thinking of was,") + (number))

            else:
                print(" I didn't understand what you said")
                repeats = repeats + 1

        elif (play == "no") or (play == "n") or (play == "N") or (play == "na") or (play == "nope") or (play == "na"):
            print(("Ok ") + name + (", bye"))
            repeats = repeats + 1
            break

        else:
            print (("I didn't understand what you said ") + (name))
            repeats = repeats + 1
            break

    playagian = (input("Do you want to play again?: "))
    if (playagian == "yes") or (playagian == "y") or (playagian == "Y") or (playagian == "ya") or (play == "ok"):
        repeats = repeats - 1
    else:
        repeats1 = repeats1 + 1
print (" ")
print(("Thank you so much for playing my game ") + (name) + ("!"))






