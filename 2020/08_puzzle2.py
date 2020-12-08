commands = open('08_input.txt', 'r').read().splitlines()

executed_commands = []
acc = 0
works = False
commands_cpy = commands[:]


def execute_command(i):
  global acc, works, commands_cpy
  if i >= len(commands):
    return
  command = commands_cpy[i]
  if i in executed_commands:
    works = False
    return
  executed_commands.append(i)
  if command[:3] == 'acc':
    acc += int(command[4:])
    return execute_command(i+1)
  elif command[:3] == 'jmp':
    return execute_command(i + int(command[4:]))
  else:
    return execute_command(i+1)

for i, command in enumerate(commands):
  executed_commands = []
  acc = 0
  works = True
  commands_cpy = commands[:]
  if command[:3] == 'jmp':
    commands_cpy[i] = commands_cpy[i].replace('jmp', 'nop')
  elif command[:3] == 'nop':
    commands_cpy[i] = commands_cpy[i].replace('nop', 'jmp')
  execute_command(0)
  if works == True:
    print(acc)

