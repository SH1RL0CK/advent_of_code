import math

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=8)
input_data = puzzle.input_data.splitlines()
example_input_data = puzzle.examples[0].input_data.splitlines()

def parse_instruction_and_nodes(data):
    instructions = data[0].replace("R", "1").replace("L", "0")
    nodes = dict()
    for node in data[2:]:
        node = node.split(" = ")
        nodes[node[0]] = node[1][1:-1].split(", ")
    return instructions, nodes

def part_a(data):
    instructions, nodes = parse_instruction_and_nodes(data)
    instruction_pos = 0
    steps = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        if instruction_pos >= len(instructions):
            instruction_pos = 0
        steps += 1
        current_node = nodes[current_node][int(instructions[instruction_pos])]
        instruction_pos += 1
    return steps
    

def part_b(data):
    instructions, nodes = parse_instruction_and_nodes(data)
    start_nodes = [value for value in nodes.keys() if value.endswith("A")]
    all_steps = []
    
    for node in start_nodes:
        instruction_pos = 0
        steps = 0
        while not node.endswith("Z"):
            if instruction_pos >= len(instructions):
                instruction_pos = 0
            steps += 1
            node = nodes[node][int(instructions[instruction_pos])]
            instruction_pos += 1
        all_steps.append(steps)
    return math.lcm(*all_steps)

if __name__ == '__main__':
    answer_a = part_a(input_data)
    print(f"Answer A: {answer_a}")
    puzzle.answer_a = answer_a
    answer_b = part_b(input_data)
    print(f"Answer B: {answer_b}")
    puzzle.answer_b = answer_b