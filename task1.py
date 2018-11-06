""" TASK 1 GAME
"""
import random
OPTIONS = ["r", "p", "s"]
CHOISE = ["Rock", "Paper", "Scissors"]
SCORE_CONTU = 0
SCORE_CONTP = 0
TRYS = 0
print("Paper, Scissors, Rock  GAME")
print("Think Fast!!!")
while True:
    USER = input("Choose your option ---> r (Rock) ---> p (Paper) ---> s (Scissors): ")
    USER = (USER.lower())
    X = random.choice(OPTIONS)
    if USER == 'r':
        print("Your Choice: %s "%CHOISE[0])
    elif USER == 'p':
        print("Your Choice: %s "%CHOISE[1])
    elif USER == 's':
        print("Your Choice: %s "%CHOISE[2])
    print("Computer choose: %s"%X)
    if USER == X:
        TRYS += 1
        print("Try Again")
        print("Socores: User:%d  Computer:%d"%(SCORE_CONTU, SCORE_CONTP))
    elif USER == 'p' and X == 'r':
        TRYS += 1
        print("YOU WIN")
        SCORE_CONTU += 1
        print("Socores: User:%d  Computer:%d"%(SCORE_CONTU, SCORE_CONTP))
    elif USER == 'r' and X == 's':
        TRYS += 1
        print("YOU WIN")
        SCORE_CONTU += 1
        print("Socores: User:%d  Computer:%d"%(SCORE_CONTU, SCORE_CONTP))
    elif USER == 's' and X == 'p':
        TRYS += 1
        print("YOU WIN")
        SCORE_CONTU += 1
        print("Socores: User:%d  Computer:%d"%(SCORE_CONTU, SCORE_CONTP))
    else:
        TRYS += 1
        print("Computer WIN")
        SCORE_CONTP += 1
        print("Socores: User:%d  Computer:%d"%(SCORE_CONTU, SCORE_CONTP))
    if SCORE_CONTU == 2:
        print("CONGRATULATIONS!!! YOU ARE THE WINER")
        print("FINAL SCORE: User:%d  Computer:%d"%(SCORE_CONTU, SCORE_CONTP))
        break
    elif SCORE_CONTP == 2:
        print("COMPUTER BEATS YOU")
        print("FINAL SCORE: User:%d  Computer:%d "%(SCORE_CONTU, SCORE_CONTP))
        break
    elif TRYS == 3:
        print("You reached Three intentd----Nobody WIN try again")
        break
    