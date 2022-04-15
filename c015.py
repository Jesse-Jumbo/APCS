times = int(input())
c = 0


for i in range(times):
    number = input()
    while True:
        number = int(number) + int(number[::-1])
        number = str(number)
        c += 1
        if number[:len(number)//2] == number[-1:-(len(number)//2)-1:-1]:
            print(c, int(number))
            c = 0
            break
