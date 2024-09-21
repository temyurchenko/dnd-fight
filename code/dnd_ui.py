#####################################
# Optional: Adding a User Interface #
#####################################

from dnd import *

########################
# Printing game events #
########################


def play_and_print(strategy0, strategy1):
    """Simulate a game and print out what happened during the simulation."""
    final0, final1 = fight(
        printing_strategy(0, strategy0),
        printing_strategy(1, strategy1),
        math_update_and_print,
        dice=printing_dice(six_sided),
    )
    print(f"The fight's ended. Player 0: {final0} HP; Player 1: {final1} HP")


def printing_strategy(who, strategy):
    """Return a strategy that also prints the player's HP and choice.

    >>> strategy0 = printing_strategy(0, always_roll_5)
    >>> strategy0(10, 20)
    The HPs are 10 and 20 and Player 0 casts Advanced Magic Missile at level 5...
    5
    >>> strategy1 = printing_strategy(1, always_roll_5)
    >>> strategy1(8, 16)
    The HPs are 16 and 8 and Player 1 casts Advanced Magic Missile at level 5...
    5
    """
    assert who == 0 or who == 1, "the player must be 0 or 1"

    def choose_and_print(hp, opponent_hp):
        "A strategy function that also prints."
        if who == 0:
            hp0, hp1 = hp, opponent_hp
        else:
            hp0, hp1 = opponent_hp, hp
        spell_spec = strategy(hp, opponent_hp)
        if spell_spec == 0:
            spell_name = "Heavy Tome"
        else:
            spell_name = f"Advanced Magic Missile at level {spell_spec}"
        print(f"The HPs are {hp0} and {hp1} and Player {who} casts {spell_name}... ")
        return spell_spec

    return choose_and_print


def printing_dice(dice):
    """Return a dice function that also prints the outcome and a space."""

    def dice_and_print():
        "A dice function that also prints."
        outcome = dice()
        print(outcome, end=" ")
        return outcome

    return dice_and_print


def math_update_and_print(spell_spec, player_hp, opponent_hp, dice):
    """Return the updated HP, print out the HP update, and print when
    I Love Math is triggered.

    >>> d = printing_dice(make_test_dice(4, 5, 3))
    >>> math_update_and_print(3, 9, 99, d)
      [ 4 5 3 ] => 12; 99 - 12 = 87 triggering **I Love Math**, decreasing to 83
    83
    """
    print("  [", end=" ")
    # ↓ Prints dice outcomes
    damage = take_turn(spell_spec, player_hp, opponent_hp, dice)
    print("] =>", damage, end="; ")
    opponent_hp1 = opponent_hp - damage
    print(f"{opponent_hp} - {damage} = {opponent_hp1}", end="")
    opponent_hp2 = i_love_math(opponent_hp1)
    if opponent_hp2 != opponent_hp1:
        print(" triggering **I Love Math**, decreasing to", opponent_hp2, end="")
    print()  # This print completes the line without adding any additional text
    return opponent_hp2


########################
# Accepting User Input #
########################


def get_int(prompt, lower, upper):
    """Return an integer i such that i >= lower and i <= upper."""
    choice = input(prompt)
    while not choice.isnumeric() or int(choice) < lower or int(choice) > upper:
        print("Please enter an integer from", lower, "to", upper)
        choice = input(prompt)
    return int(choice)


def interactive_strategy(who):
    """Return a strategy for which the user provides the spell specifier."""

    def strategy(hp, opponent_hp):
        print(f"Player {who}, you have {hp} HP and your opponent has {opponent_hp} HP")
        choice = get_int(
            "Which spell do you choose? "
            "0 for Heavy Tome, "
            "any other number for the Advanced Magic Missile at that level. ",
            0,
            10,
        )
        return choice

    return strategy


####################
# Playing the game #
####################


def play_with(num_players):
    """Play a game with NUM_PLAYERS interactive (human) players."""
    if num_players == 0:
        play_and_print(always_cast_5, always_cast_5)
    elif num_players == 1:
        play_and_print(interactive_strategy(0), always_cast_5)
    elif num_players == 2:
        play_and_print(interactive_strategy(0), interactive_strategy(1))
    else:
        print("num_players must be 0, 1, or 2.")


def main():
    """Select number of players and play a game."""
    import argparse

    parser = argparse.ArgumentParser(description="Play DnD")
    parser.add_argument(
        "--num_players",
        "-n",
        type=int,
        default=0,
        help="How many interactive players (0, 1, or 2)",
    )
    args = parser.parse_args()
    play_with(args.num_players)


if __name__ == "__main__":
    main()
