i =0
while i<=10:
    print(i)
    i+=1


guess_count=3 
guess_time=0 
value =9
while True:
    guess=int(input("Guess a number:"))

    if(guess==value):
        print("you won the game")

        break
    elif guess_time==guess_count:
        print("you failed the game")
        break 
    else:
        guess_time+=1
