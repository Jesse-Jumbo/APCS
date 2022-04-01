import sys

COMMAND = "command"
INDEX_1 = "index_1"
INDEX_2 = "index_2"
INDEX_3 = "index_3"

memory = [0] * 8
register = [0] * 4

command_dic = {COMMAND: "", INDEX_1: 0, INDEX_2: 0, INDEX_3: None}

for i in range(8):
    memory[i] = int(sys.stdin.readline()[:-1])

command_times = int(sys.stdin.readline()[:-1])

for i in range(command_times):
    command_list = sys.stdin.readline()[:-1].split()
    command_dic[COMMAND] = command_list[0]
    command_dic[INDEX_1] = int(command_list[1])
    command_dic[INDEX_2] = int(command_list[2])
    if len(command_list) > 3:
        command_dic[INDEX_3] = int(command_list[3])

    if command_dic[COMMAND] == "LOAD":
        register[command_dic[INDEX_1]] = memory[command_dic[INDEX_2]]
    elif command_dic[COMMAND] == "STORE":
        memory[command_dic[INDEX_1]] = register[command_dic[INDEX_2]]
    elif command_dic[COMMAND] == "ADD":
        register[command_dic[INDEX_1]] = register[command_dic[INDEX_2]] + register[command_dic[INDEX_3]]
    elif command_dic[COMMAND] == "MOVE":
        register[command_dic[INDEX_1]] = register[command_dic[INDEX_2]]


print(register[0])
print(memory[0])
