content = open("2022/02_puzzle_input.txt", "r").read().splitlines()


possible_scores = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

total_score = 0

for line in content:
    total_score += possible_scores[line]

print(total_score)
