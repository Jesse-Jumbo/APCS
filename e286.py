def test(first_right, first_left, second_right, second_left):
    first_right_list = [int(x) for x in first_right.split()]
    first_left_list = [int(x) for x in first_left.split()]
    second_right_list = [int(x) for x in second_right.split()]
    second_left_list = [int(x) for x in second_left.split()]
    first = {"right": sum(first_right_list), "left": sum(first_left_list)}
    second = {"right": sum(second_right_list), "left": sum(second_left_list)}

    if first["right"] > first["left"] and second["right"] > second["left"]:
        res = "Win"
    elif first["right"] < first["left"] and second["right"] < second["left"]:
        res = "Lose"
    else:
        res = "Tie"

    print(f'{first["right"]}:{first["left"]}')
    print(f'{second["right"]}:{second["left"]}')
    print(res)


test(input(), input(), input(), input())
