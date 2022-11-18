sum = 0
i = 0
while i <5:
    user_input = input()
    if not user_input.isdigit():
        print("not a number")
        continue
    elif int(user_input) <10 or int(user_input) >5555:
        print("number is out of range")
        continue
    sum += int(user_input)
    i += 1
    print("your numbers combined are =", sum)