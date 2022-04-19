import sys


while True:
    try:
        string_len = int(input())
        string_code = {"0 1 0 1": "A", "0 1 1 1": "B", "0 0 1 0": "C", "1 1 0 1": "D", "1 0 0 0": "E", "1 1 0 0": "F"}
        out_put = ""
        string = ""
        for i in range(string_len):
            string = sys.stdin.readline().strip()
            out_put += string_code[string]

        print(out_put)
    except EOFError:
        break