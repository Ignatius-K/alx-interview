#!/usr/bin/python3
"""
Module defines the zero prime game implementation
played by Maria and Ben

Rules:
    Maria is the first to play

Assumptions:
    Both players are rational, making optimal moves

Notes:
    - For more info about this, check out some game theory
"""


def is_winner(x, nums):
    """Gets the winner

    Args:
        x (int): The number of rounds to play
        num (List[int]): The n of the game

    Return:
        (str): The winner
    """
    if x <= 0 or not isinstance(nums, list) or len(nums) == 0:
        return None

    wins = []
    possible_rounds = len(nums)
    for i in range(x):
        if i >= possible_rounds:
            break
        wins.append(get_winner_for_round(nums[i]))
    first_player_wins = wins.count(0)
    last_player_wins = wins.count(1)

    if first_player_wins > last_player_wins:
        return 'Maria'
    if last_player_wins > first_player_wins:
        return 'Ben'
    return None


def get_winner_for_round(n):
    """Gets winner for rounds

    Args:
        n (int): The n of the game

    Return:
        (int): The key of the player
    """
    winner = 1
    _nums = range(1, n + 1)
    while True:
        if len(_nums) <= 1:
            break
        optimal_choice = _nums[1]
        _nums = list(
            filter(
                lambda x: False if (x % optimal_choice == 0) else True, _nums
            )
        )
        winner = 1 if winner == 0 else 0
    return winner


isWinner = is_winner


if __name__ == '__main__':
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
    print("Winner: {}".format(isWinner(1, [7, 5, 1, 4])))
    print("Winner: {}".format(isWinner(5, [11, 5, 1, 4, 3])))
