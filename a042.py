import sys

while True:
    try:
        n = int(sys.stdin.readline()[:-1])
        print(n**2 - n + 2)
    except ValueError:
        break
