from dice import make_test_dice, six_sided

INITIAL_HP = 100  # The starting HP of both players

######################
# Phase 1: Simulator #
######################


def magic_missile(spell_level, dice=six_sided):
    """Cast Advanced Magic Missile at the SPELL_LEVEL level. Return
    the sum of damages of all darts, unless a critical miss occurs, in
    which case return 1.

    spell_level: The level at which to cast the spell. Coincides with
        the number of dice rolled.
    dice: A function that simulates a single dice roll outcome. Defaults
        to the six sided dice.
    """
    # These assert statements ensure that spell_level is an integer in proper bounds.
    assert type(spell_level) == int, "spell_level must be an integer."
    assert 1 <= spell_level <= 10, "spell_level must be between 1 and 10."
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    # END PROBLEM 1


def heavy_tome(player_hp, opponent_hp):
    """Return the damage dealt by Heavy Tome.

    player_hp: The HP of the current player.
    opponent_hp: The HP of the other player.

    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2


def take_turn(spell_spec, player_hp, opponent_hp, dice=six_sided):
    """Return the damage dealt on a turn casting the spell specified by
    SPELL_SPEC when the player has PLAYER_HP points and the opponent
    has OPPONENT_HP points.

    If SPELL_SPEC is zero, we are casting Heavy Tome. If not, we are
    casting Advanced Magic Missile at level SPELL_SPEC.

    spell_spec: The specifier of the spell and its level.
    player_hp: The HP of the current player.
    opponent_hp: The HP of the other player.
    dice: A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(spell_spec) == int, "spell_spec must be an integer."
    assert 0 <= spell_spec <= 10, "spell_spec must be between 0 and 10."
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    # END PROBLEM 3


def simple_update(spell_spec, player_hp, opponent_hp, dice=six_sided):
    """Return the new HP of the opponent of the player who starts
    their turn with PLAYER_HP and then casts a spell as determined by
    SPELL_SPEC.
    """
    new_hp = opponent_hp - take_turn(spell_spec, player_hp, opponent_hp, dice)
    return new_hp


def num_factors(n):
    """Return the number of factors of N, including 1 and N itself."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4


def i_love_math(opponent_hp):
    """Returns the new HP of the opponent after the I Love Math spell."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4


def math_update(spell_spec, player_hp, opponent_hp, dice=six_sided):
    """Return the new HP of the opponent of the player who starts
    their turn with PLAYER_HP and then casts a spell as determined by
    SPELL_SPEC, *and* taking into account I Love Math."""
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4


def always_cast_5(hp, opponent_hp):
    """A strategy of always casting Advanced Magic Missile at level 5,
    regardless of the player's HP or the opponent's HP.
    """
    return 5


def fight(strategy0, strategy1, update, hp0=INITIAL_HP, hp1=INITIAL_HP, dice=six_sided):
    """Simulate a fight and return the final HPs of both players, with
    Player 0's HP first and Player 1's HP second.

    E.g., fight(always_cast_5, always_cast_5, math_update) simulates a
    game in which both players always choose to cast Advanced Magic
    Missile at level 5 on every turn and the I Love Math spell is in
    effect.

    A strategy function, such as always_cast_5, takes the current
    player's HP and their opponent's HP and returns the specifier of the
    spell the current player chooses to cast.

    An update function, such as math_update or simple_update, takes the
    spell specifier, the current player's HP, the opponent's HP, and the
    dice function used to simulate rolling dice. It returns the updated
    HP of the opponent of the current player after the player takes
    their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update: The update function (used for both players).
    hp0: Starting HP for Player 0
    hp1: Starting HP for Player 1
    dice: A function of zero arguments that simulates a dice roll.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    # END PROBLEM 5
    return hp0, hp1


#######################
# Phase 2: Strategies #
#######################


def always_cast(n):
    """Return a player strategy that always casts spell specifier N.

    A player strategy is a function that takes two HPs as arguments (the
    current player's HP, and the opponent's HP), and returns a specifier
    for the spell that the current player will cast this turn.

    >>> strategy = always_cast(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    "*** YOUR CODE HERE ***"
    # END PROBLEM 6


def catch_up(hp, opponent_hp):
    """A player strategy that always casts 5 unless the opponent has a
    higher hp, in which case it casts 6.

    >>> catch_up(9, 4)
    5
    >>> catch_up(17, 18)
    6
    """
    if hp < opponent_hp:
        return 6  # Cast one higher level to catch up
    else:
        return 5


def is_always_cast(strategy, initial_hp=INITIAL_HP):
    """Return whether STRATEGY always chooses the same spell given a
    fight with the initial INITIAL_HP health points.

    >>> is_always_cast(always_cast_5)
    True
    >>> is_always_cast(always_cast(3))
    True
    >>> is_always_cast(catch_up)
    False
    """
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    # END PROBLEM 7


def make_averaged(original_function, samples_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called SAMPLES_COUNT times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_missile = make_averaged(magic_missile, 40)
    >>> averaged_missile(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's 3.0
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8


def max_scoring_spell_level(dice=six_sided, samples_count=1000):
    """Return the spell level (1 to 10) that gives the maximum average
    damage for a turn.  Assume that the dice always return positive
    outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_spell_level(dice)
    1

    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    hp0, hp1 = fight(strategy0, strategy1, math_update)
    if hp0 > hp1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_cast(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_spell_level(six_sided)
    print("Max scoring num rolls for six-sided dice:", six_sided_max)

    print("always_cast(6) win rate:", average_win_rate(always_cast(6)))  # near 0.5
    print("catch_up win rate:", average_win_rate(catch_up))
    print("always_cast(3) win rate:", average_win_rate(always_cast(3)))
    print("always_cast(8) win rate:", average_win_rate(always_cast(8)))

    print("tome_strategy win rate:", average_win_rate(tome_strategy))
    print("math_strategy win rate:", average_win_rate(math_strategy))
    print("final_strategy win rate:", average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def tome_strategy(hp, opponent_hp, threshold=12, spell_level=6):
    """This strategy returns spell specifier 0 if Heavy Tome deals at
    least THRESHOLD damage, and returns SPELL_LEVEL otherwise. Ignore
    HP and I Love Math.
    """
    # BEGIN PROBLEM 10
    return spell_level  # Remove this line once implemented.
    # END PROBLEM 10


def math_strategy(hp, opponent_hp, threshold=12, spell_level=6):
    """This strategy returns spell specifier 0 when your opponent's HP
    would decrease by at least THRESHOLD."""
    # BEGIN PROBLEM 11
    return spell_level  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(hp, opponent_hp):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.


def main():
    """Read in the command-line argument and calls corresponding functions."""
    import argparse

    parser = argparse.ArgumentParser(description="Play DnD")
    parser.add_argument(
        "--run_experiments", "-r", action="store_true", help="Runs strategy experiments"
    )

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()


if __name__ == "__main__":
    main()
