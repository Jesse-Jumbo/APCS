import sys

# convert password characters to integers
ordinal_passwords = []
for i in sys.stdin.readline()[:-1]:
    ordinal_passwords.append(ord(i))

# get distance between ordinal of passwords
ans = ""
for i in range(len(ordinal_passwords) - 1):
    ans = f"{ans}{abs(ordinal_passwords[i + 1] - ordinal_passwords[i])}"

print(ans)
