input_list = list(input().split())
conjunction = input_list[0]

[print(f"{word} {conjunction} ", end="") for word in input_list[1:-1]]
print(input_list[-1], end="")