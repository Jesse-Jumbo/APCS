import sys

id_dic = {}
number = 10
for i in range(ord("A"), ord("Z") + 1):
    if chr(i) == "I":
        id_dic[chr(i)] = "34"
    elif chr(i) == "O":
        id_dic[chr(i)] = "35"
    elif chr(i) == "W":
        id_dic[chr(i)] = "32"
    elif chr(i) == "X":
        id_dic[chr(i)] = "30"
    elif chr(i) == "Y":
        id_dic[chr(i)] = "31"
    elif chr(i) == "Z":
        id_dic[chr(i)] = "33"
    else:
        id_dic[chr(i)] = str(number)
        number += 1

id = sys.stdin.readline()[:10]
c = 9
output = int(id_dic[id[0]][0]) + int(id_dic[id[0]][1]) * c
for i in id[1:]:
    c -= 1
    if c >= 1:
        output += int(i) * c
    else:
        output += int(i)

if output % 10 == 0:
    print("real")
else:
    print("fake")
