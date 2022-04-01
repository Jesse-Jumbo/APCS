array = input()

M = int(array.split[0])
D = int(array.split[1])

if (M*2 + D)%3 == 0:
   print("普通")

elif (M*2 + D)%3 == 1:
    print("吉")

elif (M*2 + D)%3 == 2:
    print("大吉")