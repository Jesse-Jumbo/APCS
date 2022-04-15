case_no = 0

try:
    while True:
        ord_problem = int(input())
        new_problem = [int(x) for x in input().split()]
        need_problem = [int(x) for x in input().split()]
        case_no += 1
        print(f"Case {case_no}:")
        problem = ord_problem
        for i in range(12):
            if problem >= need_problem[i]:
                print("No problem! :D")
                problem -= need_problem[i]
            else:
                print("No problem. :(")
            problem += new_problem[i]
except EOFError:
    pass
