content = open("2021/03_puzzle_input.txt", "r").read().splitlines()

oxygen_generator_rating = ""
co2_scrubber_rating = ""


for i in range(len(content[0])):
    zeros1 = 0
    zeros2 = 0
    ones1 = 0
    ones2 = 0
    lines1 = []
    lines2 = []
    for line in content:
        if line.startswith(oxygen_generator_rating):
            lines1.append(line)
            if line[i] == "0":
                zeros1 += 1
            else:
                ones1 += 1
        if line.startswith(co2_scrubber_rating):
            lines2.append(line)
            if line[i] == "0":
                zeros2 += 1
            else:
                ones2 += 1
    if len(lines1) == 1:
        oxygen_generator_rating = lines1[0]
    elif ones1 >= zeros1:
        oxygen_generator_rating += "1"
    else:
        oxygen_generator_rating += "0"

    if len(lines2) == 1:
        co2_scrubber_rating = lines2[0]
    elif zeros2 <= ones2:
        co2_scrubber_rating += "0"
    else:
        co2_scrubber_rating += "1"

print(int(co2_scrubber_rating, 2) * int(oxygen_generator_rating, 2))
