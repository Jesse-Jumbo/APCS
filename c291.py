n_people = int(input())
friend_list = list(map(int, input().split()))
temp = []
count = 0
c = 0
for i in range(n_people):
    if i not in temp:
        temp.append(i)
        c = len(temp) - 1
        while True:
            j = temp[c]
            if friend_list[j] not in temp:
                temp.append(friend_list[j])
                c = len(temp)-1
            else:
                count += 1
                break

print(count)

