# Project Name:: Guess the number game

i=0
while(1):
    print("\nYou have", 3 - i, "guesses left")
    i=i+1
    if (i > 3):
        print("Game Over!!!")
        break
    print("Enter your Guess::", end="")
    num = int(input())
    if(num==18):
        print("Congrats! You guessed it right in guess no. ",i)
        break
    elif(num>18):
        print("Guess a Smaller Number.")
    elif(num<18):
        print("Guess a Bigger Number.")
