"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
dice_swapped = False

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    # num_rolls is a positive integer that tells us how many times to roll the dic
    # num_rolls returns number of points scored by rolling the dice
    count, total = 0, 0 
    pigout = False
    while count < num_rolls:
        d = dice() 
        count += 1
        if d == 1:
            pigout = True
        total += d
    if pigout:
        return 1
    else:
        return total

    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    x = opponent_score % 10
    y = opponent_score // 10
    return max(x, y) + 1
    # END PROBLEM 2


# my prime functions! yee haw
def next_prime(score):
    if score != 2 and score < 7 or score == 11 or score == 17 or score == 29 or score == 41 or score == 59:
        return score + 2
    elif score == 2:
        return score + 1
    elif score == 23 or score == 31 or score == 53 or score == 47:
        return score + 6
    elif score == 7 or score == 19 or score == 13 or score == 43 or score == 37:
        return score + 4
    

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime rule.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls == 0:
        result = free_bacon(opponent_score)
    else:
        result = roll_dice(num_rolls, dice)
    prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
    if result in prime_number:
        result = next_prime(result)
    return result
    
    #returns the number of points scored by the current player
    # END PROBLEM 2


def select_dice(dice_swapped):
    """Return a six-sided dice unless four-sided dice have been swapped in due
    to Perfect Piggy. DICE_SWAPPED is True if and only if four-sided dice are in
    play.
    """
    # BEGIN PROBLEM 3
    if dice_swapped:
        return four_sided
    else:
        return six_sided  # Replace this statement
    # END PROBLEM 3

# Write additional helper functions here!
def is_perfect_piggy(turn_score):
    """Returns whether the Perfect Piggy dice-swapping rule should occur."""
    # BEGIN PROBLEM 4
    perfect = [4, 8, 9, 16, 25, 27, 36, 49, 64, 81, 100, 121, 125]
    if turn_score in perfect:
        return True
    else:
        return False
    # END PROBLEM 4

def is_swap(score0, score1):
    """Returns whether one of the scores is double the other."""
    # BEGIN PROBLEM 5
    if score0 == score1 * 2:
        return True
    elif score1 == score0 * 2:
        return True
    else:
        return False
    # END PROBLEM 5


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0:     The starting score for Player 0
    score1:     The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
     # Whether 4-sided dice have been swapped for 6-sided
    # BEGIN PROBLEM 6
    turn = 0 #turn goes up by 2 each time BOTH players have a turn **
    dice_swapped = False
    # take_turn(num_rolls, opponent_score, dice=six_sided)
    while score0 < goal and score1 < goal:
        if player == 0:
            turn_score0 = take_turn(strategy0(score0, score1), score1, select_dice(dice_swapped))
            score0 += turn_score0
            if is_perfect_piggy(turn_score0):
                dice_swapped = not dice_swapped
        else:
            turn_score1 = take_turn(strategy1(score1, score0), score0, select_dice(dice_swapped))
            score1 += turn_score1
            if is_perfect_piggy(turn_score1):
                dice_swapped = not dice_swapped

        if score0 != 0 and score1 != 0 and is_swap(score0, score1):
                score0, score1 = score1, score0

        player = other(player)
    return score0, score1



    
#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy #calling this function returns n which is the number of rolls


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls) '



def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the strategy
    returns a valid input. Use `check_strategy_roll` to raise an error with a
    helpful message if the strategy returns an invalid output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 7

    score = 0
    opponent_score = 0
    
    while score < goal:
        opponent_score = 0
        while opponent_score < goal:
            num_rolls = strategy(score, opponent_score)
            check_strategy_roll(score, opponent_score, num_rolls)
            opponent_score += 1
        score += 1
    return 
    # END PROBLEM 7
#checking one strategy of scores 

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """

    #(3, 1, 5, 6)
        #1, 11 = float(12 / 2) = 6.0
    # BEGIN PROBLEM 8
    def average(*arg):
        total, i = 0, 0
        while i < num_samples:
            total, i = total + fn(*arg), i + 1
        return total / num_samples
    return average
    


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    
    highest = 0
    for rolls in range (1, 11):
        ave = make_averaged(roll_dice, num_samples)(rolls, dice)
        if ave > highest:
            highest, highest_rolls = ave, rolls
    return highest_rolls

    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if free_bacon(opponent_score) >= (margin): 
        return 0 
    elif free_bacon(opponent_score) <= margin and free_bacon(opponent_score) in prime:
        if next_prime(free_bacon(opponent_score)) >= margin:
            return 0
        return num_rolls
    else:
        return num_rolls  
    # END PROBLEM 10 either 0 rolls if we will score at least 8, or 4 rolls for all else
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 11

    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if score != 0 and opponent_score != 0 and is_swap(score + margin, opponent_score) == True:
        score, opponent_score = opponent_score, score
        if score - opponent_score >= margin:
            return 0
        else:
            return num_rolls
    elif free_bacon(opponent_score) >= (margin): 
        return 0
    elif free_bacon(opponent_score) <= margin and free_bacon(opponent_score) in prime:
        if next_prime(free_bacon(opponent_score)) >= margin:
            return 0
        return num_rolls
    else:
        return num_rolls  

    # END PROBLEM 11
check_strategy(swap_strategy)

def till_swap(n, score, opponent_score):
    if opponent_score != 0 and score != 0:
        if (score + n) / opponent_score == 2:
            return True
        if (opponent_score + n) / score == 2:
            return True
        else:
            return False 

def final_strategy(score, opponent_score):
    """this code takes way to many if statements to get me to the correct win rate
    takes too long
    too much work
    annoying
    BUT I DID IT 
    
    """
    # BEGIN PROBLEM 12
    
    if score + free_bacon(opponent_score) >= 100:
        if score + free_bacon(opponent_score) != opponent_score * 2:
            # print('a')
            return 0
        # print('b')
        return 4
    if till_swap(1, score, opponent_score): 
        # print('c')
        return swap_strategy(score, opponent_score, 4, 4) # 0.7333657376654618
    if till_swap(2, score, opponent_score):
        # print('d')
        return swap_strategy(score, opponent_score, 6, 4) 
    if score + free_bacon(opponent_score) == opponent_score / 2:
        # print('e')
        return 0
    if score + free_bacon(opponent_score) == 2 * opponent_score:
        #print('f')
        return 5
    if score >= opponent_score and score + free_bacon(opponent_score) == 64:
        #print('g')
        return 0
    if score > 75 and score > opponent_score: 
        #print('h')
        return swap_strategy(score, opponent_score, 4, 7) 
    if score > 50:
        #print('i')
        return swap_strategy(score, opponent_score, 4, 8)
    else:
        #print('j')
        return swap_strategy(score, opponent_score, 8, 4) 

    # END PROBLEM 11
check_strategy(final_strategy)

#run calc.py in Downloads
##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()