numbers = "1,2,3,4,5,6,7,8,9"
for text in numbers.split(","):
    num = int(text)
    print(num)
    for num in range(1,10):
        print()
