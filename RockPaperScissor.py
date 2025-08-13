print("Hii dude! Feeling bored? Let's play Rock Paper Scissors!")
import random
print("-----------------------------------------------------------")
print("Welcome to the Rock Paper Scissors game!")
print("Ok dude! let me tell you the rules:")
print("1.Rock beats Scissors")
print("2.Scissor beats Paper")
print("3.Paper beats Rock")
print("------------------------------------------------------------")
print("0 for Rock")
print("1 for Paper")
print("2 for Scissors")
print("Want to play with your friend or with the computer?")
choice = input("Type 'friend' to play with a friend or 'computer' to play with the computer: ").strip().lower()
if choice == 'friend':
    you=int(input("Enter your choice: "))
    if you < 0 or you > 2:
        print("Dude! I think you have not read the rules properly ok let me tell you again enter a number between 0 and 2")
        exit()
    friend=int(input("let your friend enter their choice: "))
    if friend < 0 or friend > 2:
        print("Dude! I think you have not told your friend the rules properly ok let me tell you again enter a number between 0 and 2")
        exit()
    if you == friend:
        print("It's a tie! You guys are thinking same!")
    elif(you == 0 and friend == 2):
        print("You Win! That's a great move!")
    elif(you == 2 and friend == 0):
        print("Your friend wins! Sometimes it happens! letting someone else win is also a good thing!")
    elif(you > friend):
        print("You Win! That's a great move!")
    elif(you < friend):
        print("Your friend wins! Sometimes it happens! letting someone else win is also a good thing!")
    else:
        print("You have entered an invalid choice dude!")
elif choice == 'computer':
    you=int(input("Enter your choice: "))
    if you < 0 or you > 2:
        print("Dude! I think you have not read the rules properly ok let me tell you again enter a number between 0 and 2")
        exit()
    computer=random.randint(0,2)
    print("You chose: ",you)
    print("Computer chose: ",computer)
    if you == computer:
        print("It's a tie! You guys are thinking same!")
    elif(you == 0 and computer == 2) :
        print("You Win! That's a great move! Beating a machine is not easy but you did it!")
    elif(you == 2 and computer == 0):
        print("Computer wins! Sometimes it happens! letting someone else win is also a good thing!")
    elif(you > computer):
        print("You Win! That's a great move! Beating a machine is not easy but you did it!")
    elif(you < computer):
        print("Computer wins! Sometimes it happens! letting someone else win is also a good thing!")
    else:
        print("You have entered an invalid choice dude!")
else:
    print("Then whom do you want to play with? Uff go dude go and select either friend or computer")
