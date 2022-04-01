import sys

def test(n):
    if n == 1:
        res = 2
    else:
        return test(n) + test(n)
    return res


while True:
    try:
        n = int(sys.stdin.readline()[:-1])
        print()
    except ValueError:
        break