content = open("2022/02_puzzle_input.txt", "r").read().splitlines()


possible_scores = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

total_score = 0

for line in content:
    total_score += possible_scores[line]

print(total_score)
