#!/usr/bin/env Python3

from random import randint
import statistics


class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []  # clears current dice
        for i in range(3):
            self.dice.append(randint(1, 6))

    def get_dice(self):
        return self.dice


class CheatSwapper(Player):
    def cheat(self):
        if min(self.dice) < 6:
            min_roll = self.dice[0]
            min_idx = 0
            for idx in range(len(self.dice)):
                if self.dice[idx] < min_roll:
                    min_roll = self.dice[idx]
                    min_idx = idx
            self.dice[min_idx] = 6


class CheatLoadedDice(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1


class CheatMeanDice(Player):
    def cheat(self):
        mean = int(statistics.mean(self.dice))
        for i in range(len(self.dice)):
            cur_die = self.dice[i]
            if cur_die < mean and cur_die < 6 - mean:
                self.dice[i] = cur_die + mean
