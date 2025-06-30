import random


def game():
    score = random.randint(1, 101)
    
    with open("hi-Score.txt") as f:
        highscore = f.read()
        if(highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    if(score > highscore):
        with open("Hi-Score.txt" , "w") as f:
            f.write(str(score))
    print(f"Your Score is {score}")
    print(f"Your High Score is {highscore}")
    
    return score


game()
