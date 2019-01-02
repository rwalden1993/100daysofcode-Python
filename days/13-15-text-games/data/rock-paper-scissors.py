from rps_model import Player, Roll

def main():

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2)

def get_players_name():
    print('----------------------')
    print(' Rock Paper Scissors!')
    print('----------------------')

    name = input("What is your name?")
    print("Hello {}!".format(name))

    return name

def game_loop(player1, player2):
    count = 1
    while count <= 3:
        p2_roll = Roll()  # TODO: get random roll
        p1_roll = Roll()  # TODO: have player choose a roll

        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        print("{} throws {}!".format(player1.name, p1_roll.roll))
        print("{} throws {}!".format(player2.name, p2_roll.roll))

        # display winner for this round
        if outcome:
            print("{} wins this round!".format(player1.name))
        else:
            print("{} wins this round!".format(player2.name))


        count += 1

    # Compute who won


if __name__ == '__main__':
    main()