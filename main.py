import random


def play():

    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "You and the computer have both choosen {}. it's a tie.".format(computer)

    if winner(user, computer):
        return "You win! {} beats {}".format(user, computer)

    return "you lost! {} loses to {}".format(user, computer)


def winner(player, oppent):
    if (player == 'r' and oppent == 's') or (player == 's' and oppent == 'p') or (player == 'p' and oppent == 'r'):
        return True


print(play())
