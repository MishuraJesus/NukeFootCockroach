import random


def main():

    roundNumber = 0
    winNumber = 0
    tieNumber = 0

    while True:
        resultDict = {"foot": {"foot": "tie", "cockroach": "win", "nuke": "lose"},
                      "cockroach": {"foot": "lose", "cockroach": "tie", "nuke": "win"},
                      "nuke": {"foot": "tie", "cockroach": "lose", "nuke": "lose"}}

        playerChoice = input("Foot, Nuke or Cockroach? (Quit ends): ")
        AIChoice = ""

        if playerChoice == "Quit":
            print("You played", roundNumber, "rounds, and won", winNumber, "rounds, playing tie in", tieNumber,
                  "rounds.")
            break

        randomNumber = random.randint(0, 2)
        if randomNumber == 0:
            AIChoice = "foot"
        elif randomNumber == 1:
            AIChoice = "cockroach"
        elif randomNumber == 2:
            AIChoice = "nuke"

        print("You chose:", playerChoice)
        print("Computer chose:", AIChoice.capitalize())

        gameResult = resultDict[playerChoice.lower()][AIChoice.lower()]

        if gameResult == "win":
            print("You WIN!")
            winNumber += 1
        elif gameResult == "lose":
            print("You LOSE!")
        elif gameResult == "tie":
            print("It is a tie!")
            tieNumber += 1
        roundNumber += 1


if __name__ == '__main__':
    main()