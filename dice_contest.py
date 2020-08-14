from dice import *

swapper = CheatSwapper()
loaded_dice = CheatLoadedDice()
mean = CheatMeanDice()
swapper_score = 0
loaded_dice_score = 0
mean_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
    swapper.roll()
    loaded_dice.roll()
    mean.roll()

    swapper.cheat()
    loaded_dice.cheat()
    mean.cheat()
    # Remove # before print statements to see simulation running
    # Simulation takes approximately one hour to run with print
    # statements or ten seconds with print statements
    # commented out

    # print("Cheater 1 rolled" + str(swapper.get_dice()))
    # print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
    if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) == sum(mean.get_dice()):
        # print("Draw!")
        pass
    elif sum(swapper.get_dice()) > max(sum(loaded_dice.get_dice()), sum(mean.get_dice())):
        # print("Dice swapper wins!")
        swapper_score += 1

    elif sum(loaded_dice.get_dice()) > max(sum(swapper.get_dice()), sum(mean.get_dice())):
        # print("Loaded dice wins!")
        loaded_dice_score += 1
    else:
        mean_score += 1
    game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Mean dice won: " + str(mean_score))
if swapper_score == loaded_dice_score == mean_score:
    print("Game was drawn")
elif swapper_score > max(loaded_dice_score, mean_score):
    print("Swapper won most games")
elif loaded_dice_score > max(swapper_score, mean_score):
    print("Loaded dice won most games")
else:
    print("Mean dice won most games")
