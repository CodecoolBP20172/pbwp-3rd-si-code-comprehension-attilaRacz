"""
This is a game where the player guesses a computer generated random number,
getting feedback about it's size related to the player guess,
and fails after five incorrect guesses.
"""
import random  # imports the random module

guessesTaken = 0  # counter: how many guesses the player took

print('Hello! What is your name?')  # prints this message
myName = input()  # takes the player's name as an input and assigns it to myName variable

number = random.randint(1, 20)  # generates a random number between 1 - 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints this message and the player's name

while guessesTaken < 6:  # creates a loop where the player has five guesses maximum
    print('Take a guess.')  # prints out the message
    guess = input()  # takes an input and assigns it to quess variable
    guess = int(guess)  # converts the input to an integer

    guessesTaken += 1  # if guess does not equal number, adds one to guessesTaken

    if guess < number:  # if guess is higher than number
        print('Your guess is too low.')  # prints this message

    if guess > number:  # if guess is lower than number
        print('Your guess is too high.')  # prints this message

    if guess == number:  # if guess equals number
        break  # breaks out of this loop

if guess == number:  # if guess equals number
    guessesTaken = str(guessesTaken)  # convert guessesTaken to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # prints this message including the player's name and the number of guesses taken

if guess != number:  # if guess does not equal number after five trys
    number = str(number)  # converts number to a string
    print('Nope. The number I was thinking of was ' + number)  # prints this message including number
