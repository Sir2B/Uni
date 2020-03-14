import random
import matplotlib.pyplot as plt
from typing import List


def get_last_valid_dice(dice_array: List[int]) -> int:
    dice_idx = 0

    # print(dice_array)

    # go through the dice array
    while dice_idx < len(dice_array):
        dice = dice_array[dice_idx]
        dice_idx += dice

    # go back to last valid dice
    dice_idx -= dice
    # print(dice_idx)
    return dice_idx

def play_one_round() -> bool:
    dice_len = DICE_LENGTH

    # throw all dices
    dices = [random.randint(1, 6) for _ in range(dice_len)]

    # go through the dice array and get last last dice
    dice_idx = get_last_valid_dice(dices)

    # remove all dices after last valid dice
    dices = dices[:dice_idx + 1]

    # print(dices)

    # throw the first dice again
    dices[0] = random.randint(1, 6)

    # go through the dice array again and get last last dice
    dice_idx = get_last_valid_dice(dices)

    return dice_idx == (len(dices) - 1)


if __name__ == "__main__":
    # random.seed(2)
    GAME_CNT = 1000

    x_values = []
    y_values = []

    for length in range(1, 80):
        DICE_LENGTH = length

        wins = 0

        for _ in range(GAME_CNT):
            win = play_one_round()
            if win:
                wins += 1
        
        propability = 100*wins/GAME_CNT
        x_values.append(DICE_LENGTH)
        y_values.append(propability)
        print(f"dice length: {DICE_LENGTH};probability: {propability} %")

    plt.plot(x_values, y_values)
    plt.show()
