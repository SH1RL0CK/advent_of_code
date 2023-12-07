import operator
import random
from collections import Counter
from functools import cmp_to_key

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=7)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()

cards_a = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def get_rank_a(hand):
    counter = Counter(hand).values()
    if 5 in counter:
        return 1
    if 4 in counter:
        return 2
    if 3 in counter and 2 in counter:
        return 3
    if 3 in counter:
        return 4
    if list(counter).count(2) == 2:
        return 5
    if 2 in counter:
        return 6
    return 7


def compare_hands_a(hand1, hand2):
    rank1 = get_rank_a(hand1[0])
    rank2 = get_rank_a(hand2[0])
    if rank1 != rank2:
        return 1 if rank1 < rank2 else -1
    for i in range(0, len(hand1[0])):
        if cards_a.index(hand1[0][i]) != cards_a.index(hand2[0][i]):
            return 1 if cards_a.index(hand1[0][i]) < cards_a.index(hand2[0][i]) else -1
    return 1


def part_a(data):
    result = 0
    values = []
    for value in data:
        hand, number = value.split(" ")
        values.append((hand, int(number)))
    values = sorted(values, key=cmp_to_key(compare_hands_a))
    for i, value in enumerate(values):
        result += value[1] * (i + 1)
    return result


cards_b = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_rank_b(hand):
    if hand == "JJJJJ":
        return 1

    counter = Counter(hand)
    if "J" in counter.keys():
        counter = dict(counter)
        counter.pop("J")
        most_common_letter = max(counter.items(), key=operator.itemgetter(1))[0]
        hand = hand.replace("J", most_common_letter)
        counter = Counter(hand)

    counter = counter.values()
    if 5 in counter:
        return 1
    if 4 in counter:
        return 2
    if 3 in counter and 2 in counter:
        return 3
    if 3 in counter:
        return 4
    if list(counter).count(2) == 2:
        return 5
    if 2 in counter:
        return 6
    return 7


def compare_hands_b(hand1, hand2):
    rank1 = get_rank_b(hand1[0])
    rank2 = get_rank_b(hand2[0])
    if rank1 != rank2:
        return 1 if rank1 < rank2 else -1
    for i in range(0, len(hand1[0])):
        if cards_b.index(hand1[0][i]) != cards_b.index(hand2[0][i]):
            return 1 if cards_b.index(hand1[0][i]) < cards_b.index(hand2[0][i]) else -1
    return 1


def part_b(data):
    result = 0
    values = []
    for value in data:
        hand, number = value.split(" ")
        values.append((hand, int(number)))
    values = sorted(values, key=cmp_to_key(compare_hands_b))
    for i, value in enumerate(values):
        result += value[1] * (i + 1)
    return result


if __name__ == "__main__":
    answer_a = part_a(input_data)
    # print(f"Answer A: {answer_a}")
    puzzle.answer_a = answer_a
    answer_b = part_b(input_data)
    print(f"Answer B: {answer_b}")
    puzzle.answer_b = answer_b
