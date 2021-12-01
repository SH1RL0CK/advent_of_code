commands = open("08_input.txt", "r").read().splitlines()

executed_commands = []
acc = 0


def execute_command(i):
    global acc
    command = commands[i]
    if i in executed_commands:
        return
    executed_commands.append(i)
    if command[:3] == "acc":
        acc += int(command[4:])
        return execute_command(i + 1)
    elif command[:3] == "jmp":
        return execute_command(i + int(command[4:]))
    else:
        return execute_command(i + 1)


execute_command(0)
print(acc)
