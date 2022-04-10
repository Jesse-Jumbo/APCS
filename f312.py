import sys

plant_one = [int(x) for x in sys.stdin.readline()[:-1].split()]
plant_two = [int(x) for x in sys.stdin.readline()[:-1].split()]
best_gain = -10000000000
worker = int(sys.stdin.readline()[:-1])
for i in range(worker+1):
    one_gain = plant_one[0] * i**2 + plant_one[1] * i + plant_one[2]
    j = worker-i
    two_gain = plant_two[0] * j**2 + plant_two[1] * j + plant_two[2]
    best_gain = max(best_gain, one_gain + two_gain)

print(best_gain)


# import sys
#
#
# plant_one_gain_list = []
# plant_two_gain_list = []
# all_gain_set = []
# is_debug = False
#
# test_data = [["2", "-1", "3"]
#              , ["4", "-5", "2"]
#              , [2]]
#
# if is_debug:
#     plant_ont_list = test_data[0]
#     plant_two_list = test_data[1]
#     worker = test_data[2][0]
# else:
#     plant_ont_list = sys.stdin.readline()[:-1].split()
#     plant_two_list = sys.stdin.readline()[:-1].split()
#     worker = int(sys.stdin.readline()[:-1])
#
# for i in range(worker+1):
#     plant_one_gain = (int(plant_ont_list[0]) * (i**2)) + (int(plant_ont_list[1]) * i) + int(plant_ont_list[2])
#     plant_one_gain_list.append(plant_one_gain)
#     plant_two_gain = (int(plant_two_list[0]) * (i**2)) + (int(plant_two_list[1]) * i) + int(plant_two_list[2])
#     plant_two_gain_list.append(plant_two_gain)
#
# for i in range(worker+1):
#     all_gain_set.append(plant_one_gain_list[i]+plant_two_gain_list[worker-i])
#
# print(max(all_gain_set))
